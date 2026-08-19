-- QuantConnect BigQuery Data Warehouse DDL for Lucidchart / Database Tools
-- Project: bav-personal-cloud | Dataset: develop

CREATE TABLE BTOPResults (
    backtestId VARCHAR(32) PRIMARY KEY,
    name VARCHAR(255),
    note TEXT,
    organizationId VARCHAR(64),
    projectId INT,
    completed BOOLEAN,
    optimizationId VARCHAR(64),
    tradeableDates INT,
    backtestStart TIMESTAMP,
    backtestEnd TIMESTAMP,
    created TIMESTAMP,
    snapshotId INT,
    status VARCHAR(64),
    error TEXT,
    stacktrace TEXT,
    progress FLOAT,
    hasInitializeError BOOLEAN,
    nodeName VARCHAR(64),
    outOfSampleMaxEndDate DATETIME,
    outOfSampleDays INT,
    _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE BTOPBatchChunks (
    batch_id VARCHAR(128),
    chunk_index INT,
    backtest_id VARCHAR(32) REFERENCES BTOPResults(backtestId),
    algo_code VARCHAR(32),
    start_date DATE,
    end_date DATE,
    status VARCHAR(32),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    PRIMARY KEY (batch_id, chunk_index)
);

CREATE TABLE BTOPTrades (
    pk VARCHAR(255) PRIMARY KEY,
    backtest_run_id VARCHAR(32) REFERENCES BTOPResults(backtestId),
    batch_id VARCHAR(128),
    algo_code VARCHAR(32),
    timestamp TIMESTAMP,
    underlying VARCHAR(32),
    action VARCHAR(16),
    qty INT,
    strike FLOAT,
    near_expiry DATE,
    far_expiry DATE,
    vol_ratio FLOAT,
    slope FLOAT,
    ivrv_ratio FLOAT,
    entry_price FLOAT,
    exit_price FLOAT,
    pnl FLOAT,
    parameters TEXT,
    exit_reason VARCHAR(64),
    chunk_index INT,
    _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE BTOPOrders (
    order_pk VARCHAR(255) PRIMARY KEY,
    backtestId VARCHAR(32) REFERENCES BTOPResults(backtestId),
    id INT,
    contingentId INT,
    symbol VARCHAR(64),
    limitPrice FLOAT,
    stopPrice FLOAT,
    price FLOAT,
    quantity FLOAT,
    value FLOAT,
    time TIMESTAMP,
    type INT,
    status INT,
    securityType INT,
    direction INT,
    tag VARCHAR(255),
    _ingestedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE BTOPTotalPerformancePortfolioStats (
    portfolioStatId VARCHAR(255) PRIMARY KEY,
    backtestId VARCHAR(32) UNIQUE REFERENCES BTOPResults(backtestId),
    averageWinRate FLOAT,
    averageLossRate FLOAT,
    profitLossRatio FLOAT,
    winRate FLOAT,
    lossRate FLOAT,
    expectancy FLOAT,
    startEquity FLOAT,
    endEquity FLOAT,
    compoundingAnnualReturn FLOAT,
    drawdown FLOAT,
    totalNetProfit FLOAT,
    sharpeRatio FLOAT,
    probabilisticSharpeRatio FLOAT,
    sortinoRatio FLOAT,
    alpha FLOAT,
    beta FLOAT,
    annualStandardDeviation FLOAT,
    annualVariance FLOAT,
    informationRatio FLOAT,
    trackingError FLOAT,
    treynorRatio FLOAT,
    portfolioTurnover FLOAT,
    valueAtRisk99 FLOAT,
    valueAtRisk95 FLOAT,
    _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE BTOPTotalPerformanceTradeStats (
    tradeStatId VARCHAR(255) PRIMARY KEY,
    backtestId VARCHAR(32) UNIQUE REFERENCES BTOPResults(backtestId),
    startDateTime TIMESTAMP,
    endDateTime TIMESTAMP,
    totalNumberOfTrades INT,
    numberOfWinningTrades INT,
    numberOfLosingTrades INT,
    totalProfitLoss FLOAT,
    totalProfit FLOAT,
    totalLoss FLOAT,
    largestProfit FLOAT,
    largestLoss FLOAT,
    averageProfitLoss FLOAT,
    averageProfit FLOAT,
    averageLoss FLOAT,
    profitFactor FLOAT,
    sharpeRatio FLOAT,
    sortinoRatio FLOAT,
    totalFees FLOAT,
    _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE BTOPTotalPerformanceClosedTrades (
    tradeId VARCHAR(255) PRIMARY KEY,
    backtestId VARCHAR(32) REFERENCES BTOPResults(backtestId),
    symbol VARCHAR(64),
    entryTime TIMESTAMP,
    entryPrice FLOAT,
    direction INT,
    quantity FLOAT,
    exitTime TIMESTAMP,
    exitPrice FLOAT,
    profitLoss FLOAT,
    totalFees FLOAT,
    mae FLOAT,
    mfe FLOAT,
    duration VARCHAR(64),
    isWin BOOLEAN,
    _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE BTOPRollingWindowPortfolioStats (
    portfolioStatId VARCHAR(255) PRIMARY KEY,
    backtestId VARCHAR(32) REFERENCES BTOPResults(backtestId),
    rollingWindowId VARCHAR(32),
    compoundingAnnualReturn FLOAT,
    drawdown FLOAT,
    sharpeRatio FLOAT,
    sortinoRatio FLOAT,
    _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE BTOPRollingWindowTradeStats (
    tradeStatId VARCHAR(255) PRIMARY KEY,
    backtestId VARCHAR(32) REFERENCES BTOPResults(backtestId),
    rollingWindowId VARCHAR(32),
    totalNumberOfTrades INT,
    winRate FLOAT,
    profitFactor FLOAT,
    _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE BTOPParameterSet (
    parameterId VARCHAR(255) PRIMARY KEY,
    backtestId VARCHAR(32) UNIQUE REFERENCES BTOPResults(backtestId),
    parameters TEXT,
    _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE BTOPResearchGuide (
    guideId VARCHAR(255) PRIMARY KEY,
    backtestId VARCHAR(32) UNIQUE REFERENCES BTOPResults(backtestId),
    minutes INT,
    backtestCount INT,
    _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE BTOPRuntimeStatistics (
    runtimeStatId VARCHAR(255) PRIMARY KEY,
    backtestId VARCHAR(32) UNIQUE REFERENCES BTOPResults(backtestId),
    equity VARCHAR(64),
    fees VARCHAR(64),
    netProfit VARCHAR(64),
    return VARCHAR(64),
    _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE BTOPCharts (
    chartId VARCHAR(255) PRIMARY KEY,
    backtestId VARCHAR(32) REFERENCES BTOPResults(backtestId),
    name VARCHAR(255),
    seriesName VARCHAR(255),
    _ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);