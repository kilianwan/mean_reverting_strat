import pandas as pd 

def z_score(data, window_size : int):
    """
    Compute rolling z-score of a time series.
    
    Returns: 
        pd.Series of z-scores
    """
    mean = data.rolling(window=window_size).mean()
    std  = data.rolling(window=window_size).std()
    zscore = (data - mean) / std 
    return zscore.dropna()

