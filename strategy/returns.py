import numpy as np

def returns(data):
    """
    Compute simple returns.
    
    Parameters:
        data (pd.Series or pd.DataFrame): price time series.
        
    Returns: 
        pd.Series or pd.DataFrame : simple returns
    """
    return data.pct_change()

def strategy_returns(ret_1, ret_2, positions): 
    """
    Compute the returns of the mean-reversion strategy
    
    Parameters: 
        ret_1: returns of asset 1
        ret_2: returns of asset 2
        
    Returns:
        np.ndarray: strategy returns
    """
    strat_return = []
    n = min(len(ret_1), len(ret_2), len(positions))
    
    # ensure array
    ret_1 = np.array(ret_1)
    ret_2 = np.array(ret_2)
    positions = np.array(positions)
    
    for t in range(1,n):
        if positions[t-1] == 1: 
            ret_t = ret_1[t] - ret_2[t]
        elif positions[t-1] == -1:
            ret_t = -ret_1[t] + ret_2[t]
        elif positions[t-1] == 0:
            ret_t = 0
        strat_return.append(ret_t)
    return np.array(strat_return)