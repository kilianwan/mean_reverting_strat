from statsmodels.tsa.stattools import adfuller

def adftest(data, level=0.05, verbose=True):
    """
    Perform ADF test on a time series. 
    
    Returns: 
        results (dict): t-stat, p-val and conclusion as string
    """
    adf = adfuller(data)
    t_stat, p_val = adf[0], adf[1]
    conclusion = "reject null hypothesis" if p_val < level else "fail to reject null hypothesis"
    
    if verbose:
        print(f"t-stat : {t_stat:.4f} \np-val : {p_val:.4f} ==> {conclusion}")
    return {
        't_stat': t_stat,
        'p_val': p_val,
        'conclusion': conclusion
    }
    
    