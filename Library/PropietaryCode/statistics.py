import statsmodels.tsa.stattools as ts
import statsmodels.api as sm
import numpy as np
from datetime import timedelta


def ApplyADFTest(self, price_series) -> bool:
    if len(price_series) > self.historical_data_days_backward * 0.5:
        adf_result = ts.adfuller(price_series)
        # Check if the test statistic is less than the 5% critical value
        is_mean_reverting = adf_result[0] < adf_result[4]['5%']
        if is_mean_reverting:
            self.Log(
                f"ADF test result for {price_series.name}: Statistic: {adf_result[0]}, 5% Critical Value: {adf_result[4]['5%']}, Mean Reverting: {is_mean_reverting}")
        return is_mean_reverting
    else:
        return False


def ApplyHurstTest(self, price_series):
    # Implement Hurst exponent calculation
    # it's another method to replace ADF to test for mean reversion time series
    pass


def FitOUProcess(self, price_series) -> (timedelta, float):
    """
    Fit an Ornstein-Uhlenbeck process to the given price series and
    calculate the expected time to reversion.
    """
    # function_time_start = self.Time
    try:
        # Calculate changes in the price series
        delta_prices = np.diff(price_series)

        # Prepare the lagged price series (X_t-1)
        lagged_prices = price_series[:-1]

        # Perform linear regression to estimate theta and mu
        X = sm.add_constant(lagged_prices)
        model = sm.OLS(delta_prices, X).fit()

        theta = -model.params[1]
        mu = model.params[0] / theta

        # Calculate expected time to reversion
        if theta > 0:
            self.int_days_to_reversion = theta
            expected_time_to_reversion = timedelta(days=1 / theta)
            self.Log(f"FOUP0 {self.security} Expected time to reversion: {expected_time_to_reversion} days")
            # function_time_emd = self.Time
            # total_time = function_time_emd-function_time_start
            # self.Debug(f'FitOUProcess took {total_time} seconds') # Debug
            return expected_time_to_reversion, mu
        else:
            self.Log("FOUP1 Theta is not positive. The series might not be mean-reverting.")
            return None, None

    except Exception as e:
        self.Log(f"FOUPE Error in fitting OU process: {str(e)}")
        return None, None