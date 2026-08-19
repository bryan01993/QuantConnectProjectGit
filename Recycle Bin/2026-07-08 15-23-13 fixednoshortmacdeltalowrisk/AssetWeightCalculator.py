import numpy as np
from scipy.cluster import hierarchy
import pandas as pd 
from AlgorithmImports import *

class AssetWeightCalculator:
    def __init__(self, algorithm: QCAlgorithm):
        
        self.algorithm = algorithm
        self.risk_free = self.algorithm.add_equity("BIL", Resolution.DAILY)

        
    def coarse_selection(self, coarse):
        """
        Available CoarseFundamental properties:
        - symbol: Symbol object
        - price: Current price
        - volume: Daily volume
        - dollar_volume: Daily dollar volume (price * volume)
        - has_fundamental_data: Boolean indicating if fundamental data exists
        - market_cap: Market cap (but only updated monthly)
        - adjustment_factor: Stock split adjustment factor
        """

        # First basic filtering
        filtered = [x for x in coarse if (
            x.price > 10 and                     # Price filter to avoid penny stocks
            x.volume > 500000 and                # Minimum daily volume for liquidity
            x.has_fundamental_data and           # Must have fundamental data
            x.dollar_volume > 5000000            # Minimum $5M daily dollar volume
        )]
        
        # Sort by dollar volume (most liquid first)
        sorted_by_volume = sorted(filtered, 
                                key=lambda x: x.dollar_volume, 
                                reverse=True)
        
        # Take top 200 most liquid stocks
        top_liquid = sorted_by_volume[:500]
        
        # Loggin some statistics
        if top_liquid:
            self.algorithm.log("\nCoarse Selection Statistics:")
            self.algorithm.log(f"Avg Price: ${np.mean([x.price for x in top_liquid]):.2f}")
            self.algorithm.log(f"Avg Volume: {np.mean([x.volume for x in top_liquid]):,.0f}")
            self.algorithm.log(f"Avg Dollar Volume: ${np.mean([x.dollar_volume for x in top_liquid]):,.2f}")
            
            # Loggin top 5 most liquid stocks
            self.algorithm.log("\nTop 5 Most Liquid Stocks:")
            for stock in top_liquid[:5]:
                self.algorithm.log(f"{stock.symbol}: ${stock.dollar_volume:,.2f} daily volume")
        
        return [x.symbol for x in top_liquid]

    def fine_selection(self, fine):
        """
        Comprehensive long-term stock selection
        """
        market_cap_filtered = [x for x in fine if x.market_cap is not None and x.market_cap > 10e9]

        # Examine the fundamental data of the first few companies
        for i, company in enumerate(market_cap_filtered[:5]):
            pass

        qualified_companies = []

        for company in market_cap_filtered:
            try:
                financial_score = 0
                growth_score = 0
                quality_score = 0
                value_score = 0
                
                # Financial Strength
                if (company.financial_statements is not None and 
                    company.financial_statements.balance_sheet is not None):
                    
                    current_assets = company.financial_statements.balance_sheet.current_assets.value
                    current_liabilities = company.financial_statements.balance_sheet.current_liabilities.value
                    total_debt = company.financial_statements.balance_sheet.total_debt.value
                    total_equity = company.financial_statements.balance_sheet.total_equity.value
                    
                    current_ratio = current_assets / current_liabilities if current_liabilities != 0 else 0
        
                    # Modified debt-equity handling
                    if total_equity <= 0:
                        # Negative equity is a red flag
                        financial_score -= 1  # Penalty for negative equity
                    else:
                        debt_equity = total_debt / total_equity
                        if debt_equity < 1.5:
                            financial_score += 1

                    if current_ratio > 1.5:
                        financial_score += 1
                
                if hasattr(company, 'valuation_ratios'):
                    # Debug valuation ratios for first few companies
                    if len(qualified_companies) < 5:
                        self.algorithm.debug(f"\nGrowth Metrics for {company.symbol.value}:")
                        self.algorithm.debug(f"First Year Est. EPS Growth: {getattr(company.valuation_ratios, 'first_year_estimated_eps_growth', 'Not Available')}")
                        self.algorithm.debug(f"Sustainable Growth Rate: {getattr(company.valuation_ratios, 'sustainable_growth_rate', 'Not Available')}")

                    # Growth checks with null handling
                    eps_growth = getattr(company.valuation_ratios, 'first_year_estimated_eps_growth', None)
                    sustainable_growth = getattr(company.valuation_ratios, 'sustainable_growth_rate', None)

                    if eps_growth is not None and not np.isnan(eps_growth) and eps_growth > 0.10:
                        growth_score += 1
                        if len(qualified_companies) < 5:
                            self.algorithm.debug(f"Added growth score for EPS growth: {eps_growth:.2%}")

                    if sustainable_growth is not None and not np.isnan(sustainable_growth) and sustainable_growth > 0.10:
                        growth_score += 1
                        if len(qualified_companies) < 5:
                            self.algorithm.debug(f"Added growth score for sustainable growth: {sustainable_growth:.2%}")
                
                    # Quality (Profitability and Efficiency)
                    if company.valuation_ratios.earning_yield > 0.06:  # 6% earnings yield
                        quality_score += 1
                    if company.valuation_ratios.fcf_yield > 0.05:  # 5% free cash flow yield
                        quality_score += 1
                    
                    # Value
                    if company.valuation_ratios.pe_ratio is not None:
                        if (company.valuation_ratios.pe_ratio < 
                            company.valuation_ratios.pe_ratio_5_year_average):
                            value_score += 1
                            
                    if company.valuation_ratios.ev_to_ebitda < 12:  # Common threshold
                        value_score += 1
                
                total_score = (financial_score + growth_score + quality_score + value_score)
                
                if total_score > 3:
                    qualified_companies.append((company, total_score))
                    
            except Exception as e:
                self.algorithm.debug(f"Error processing company {company.symbol}: {str(e)}")
                continue

        self.algorithm.debug(f"Companies with scores > 3: {len(qualified_companies)}")
        
        # Sort by total score
        sorted_companies = sorted(qualified_companies, 
                                key=lambda x: x[1], 
                                reverse=True)
        
        # Return symbols for top companies
        filtered = [company.symbol for company, _ in sorted_companies]
        
        return self.low_corr_assets(filtered)

    def calculate_sharpe_ratio(self, symbol, period=756): # This is 3 yrs worth of trading days
        """
        Calculates the sharpe
        """
        try:
            # If a KeyValuePair was recieved only take the symbol
            if hasattr(symbol, "Key"):
                symbol = symbol.Key

            history = self.algorithm.history([symbol], period, Resolution.DAILY) 

            if history.empty:
                self.algorithm.debug(f"No history for {symbol.value}")
                return None
            
            # Get risk-free rate
            rf_history = self.algorithm.history(self.risk_free.symbol, 1, Resolution.DAILY)
            risk_free_rate = rf_history['close'].iloc[-1]/100 if not rf_history.empty else 0.02  # Default to 2% if no data

            # Sharpe ratio logic
            returns = history['close'].pct_change().dropna()
            excess_returns = returns - (risk_free_rate/252)
            mean_excess_return = excess_returns.mean() * 252
            std_dev = excess_returns.std() * np.sqrt(252)
            return mean_excess_return / std_dev if std_dev != 0 else None
            
        except Exception as e:
            self.algorithm.debug(f"Error calculating Sharpe for {symbol.value}: {str(e)}")
            return None
            
    
    def low_corr_assets(self, symbols):
        """
        Selects assets with low correlation using hierarchical clustering.
        Returns a list of symbols sorted by their Sharpe ratios within clusters.
        
        Parameters:
        symbols: list of symbols to analyze
        """

        try:
            
            correlation_period = 252 * 3
            all_returns = {}
        
            # Fetch returns
            for symbol in symbols:
                history = self.algorithm.history([symbol], correlation_period, Resolution.DAILY)
                if not history.empty:
                    close_prices = history.loc[symbol]['close']
                    returns = close_prices.pct_change().dropna()
                    if len(returns) > 0:
                        all_returns[symbol] = returns

            
            if not all_returns:
                return []

            # Create DataFrame with proper alignment
            returns_df = pd.DataFrame(all_returns)
            
            # Remove any columns with all NaN values
            returns_df = returns_df.dropna(axis=1, how='all')
            
            # Fill any remaining NaN values with 0 or forward fill
            returns_df = returns_df.fillna(method='ffill')
            
            
            # Calculate correlation matrix
            corr_matrix = returns_df.corr()
            
            # Replace any remaining NaN values in correlation matrix with 0
            corr_matrix = corr_matrix.fillna(0)
            
            # Convert correlations to distances
            distance_matrix = np.sqrt(2 * (1 - corr_matrix))
            
            # Ensure distance matrix contains only finite values
            if not np.all(np.isfinite(distance_matrix)):
                self.algorithm.debug("Warning: Distance matrix contains non-finite values")
                # Replace non-finite values with maximum finite value
                max_finite = np.nanmax(distance_matrix[np.isfinite(distance_matrix)])
                distance_matrix[~np.isfinite(distance_matrix)] = max_finite
            
            # Convert to condensed form for linkage
            condensed_dist = []
            for i in range(len(distance_matrix)):
                for j in range(i + 1, len(distance_matrix)):
                    dist = distance_matrix.iloc[i, j]
                    if np.isfinite(dist):  # Only add finite distances
                        condensed_dist.append(dist)
                    else:
                        condensed_dist.append(0)  # or some other appropriate value
            
            
            # Verify we have valid data for clustering
            if not condensed_dist:
                self.algorithm.debug("No valid distances for clustering")
                return list(symbols)[:30]
                
            # Perform hierarchical clustering
            linkage = hierarchy.linkage(condensed_dist, method='complete')
            clusters = hierarchy.fcluster(linkage, t=0.5, criterion='distance')
            
            # Select best assets from each cluster
            selected_assets = []
            cluster_ids = np.unique(clusters)
            
            for cluster_id in cluster_ids:
                cluster_mask = clusters == cluster_id
                cluster_assets = returns_df.columns[cluster_mask]
                
                # Calculate Sharpe ratios for this cluster
                cluster_sharpes = {}
                for asset in cluster_assets:
                    sharpe = self.calculate_sharpe_ratio(asset)
                    if sharpe is not None:
                        cluster_sharpes[asset] = sharpe
                
                # Select asset with highest Sharpe from cluster
                if cluster_sharpes:
                    best_asset = max(cluster_sharpes.items(), key=lambda x: x[1])[0]
                    selected_assets.append(best_asset)
            
            # Take top 20 assets
            final_assets = selected_assets[:30]
            
            # Get correlation matrix for final selection
            final_returns = returns_df[[symbol for symbol in final_assets]]
            final_corr = final_returns.corr()
            
            # Log correlation statistics
            self.algorithm.debug("\nCorrelation Statistics for Final 30 Assets:")
            
            # Average correlation
            corr_values = final_corr.values[np.triu_indices_from(final_corr.values, k=1)]
            avg_corr = np.mean(corr_values)
            self.algorithm.debug(f"Average Correlation: {avg_corr:.3f}")
            
            # Correlation range
            min_corr = np.min(corr_values)
            max_corr = np.max(corr_values)
            self.algorithm.debug(f"Correlation Range: {min_corr:.3f} to {max_corr:.3f}")
            
            # Most correlated pair
            max_corr_idx = np.unravel_index(np.argmax(final_corr.values * (1 - np.eye(len(final_assets)))), final_corr.shape)
            self.algorithm.debug(f"Most correlated pair: {final_assets[max_corr_idx[0]].value} - {final_assets[max_corr_idx[1]].value} ({final_corr.iloc[max_corr_idx]:.3f})")
            
            # Least correlated pair
            min_corr_idx = np.unravel_index(np.argmin(final_corr.values + np.eye(len(final_assets))), final_corr.shape)
            self.algorithm.debug(f"Least correlated pair: {final_assets[min_corr_idx[0]].value} - {final_assets[min_corr_idx[1]].value} ({final_corr.iloc[min_corr_idx]:.3f})")
            
            # Print full correlation matrix for final selection
            self.algorithm.debug("\nFinal Correlation Matrix:")
            for i in range(len(final_assets)):
                row = [f"{final_corr.iloc[i,j]:.3f}" for j in range(len(final_assets))]
                self.algorithm.debug(f"{final_assets[i].value}: {', '.join(row)}")
            
            self.algorithm.debug(f"\nSelected {len(final_assets)} low-correlation assets")
            return final_assets
            
        except Exception as e:
            self.algorithm.debug(f"Error in low_corr_assets: {str(e)}")
            return list(symbols)[:30]

    def normalize_scores(self, scores):
        """
        The list of scores from the ranking method are
        normalized using a z score so that an additive
        operation may be used in WeightCombiner()
        """
        values = np.array(list(scores.values()))
        mean = np.mean(values)
        std_dev = np.std(values)

        if std_dev == 0:
            # If no variation in scores, assign equal normalized scores
            return {symbol: 0 for symbol in scores.keys()}

        normalized_scores = {symbol: (score - mean) / std_dev for symbol, score in scores.items()}
        return normalized_scores

