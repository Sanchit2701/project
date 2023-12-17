# Calculate Returns
Returns = RawStockDataPivot.copy()
Returns[StockTickers] = Returns[StockTickers] / Returns[StockTickers].shift(12) - 1
Returns = Returns.dropna()

# Calculate Expected Returns
ExpectedReturns = Returns.mean()

# Calculate Excess Returns
ExcessReturns = Returns - ExpectedReturns

# Calculate Variance-Covariance Matrix
numPeriods = len(ExcessReturns)
VarCov = ExcessReturns.T.dot(ExcessReturns) / (numPeriods - 1)
