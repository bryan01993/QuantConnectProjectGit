from AlgorithmImports import *
from hmmlearn import hmm

class HMMRegimeDetection(QCAlgorithm):
    def initialize(self):
        self.set_start_date(2019, 1, 1)
        self.add_universe(lambda fundamental: [f.symbol for f in sorted(fundamental, key=lambda x: x.market_cap, reverse=True)[:10]])
        self.set_portfolio_construction(EqualWeightingPortfolioConstructionModel(timedelta(minutes=5)))
        self.settings.rebalance_portfolio_on_insight_changes = False
        self.set_warm_up(timedelta(3))

    def on_securities_changed(self, changes):
        for added in changes.added_securities:
            added.roc = RateOfChange(1)
            added.roc.window.size = self.get_parameter("roc_window", 150)
            added.model = hmm.GaussianHMM(n_components=3, n_iter=100, random_state=100)
            added.model_month = -1
            added.consolidator = TradeBarConsolidator(timedelta(minutes=self.get_parameter("bar_size", 5)))
            added.consolidator.data_consolidated += self.on_consolidated
            self.subscription_manager.add_consolidator(added.symbol, added.consolidator)

    def on_consolidated(self, _, bar):
        security = self.securities[bar.symbol]
        security.roc.update(bar.end_time, bar.price)
        if security.roc.window.is_ready:
            if security.model_month != bar.end_time.month:
                security.model.fit(np.array([point.value for point in security.roc.window])[::-1].reshape(-1, 1))
                security.model_month = bar.end_time.month
            post_prob = security.model.predict_proba(np.array([security.roc.current.value]).reshape(1, -1)).flatten()
            direction = InsightDirection.UP if post_prob[2] > post_prob [0] else InsightDirection.DOWN
            self.emit_insights(Insight.price(bar.symbol, timedelta(minutes=self.get_parameter("bar_size", 5)), direction))
