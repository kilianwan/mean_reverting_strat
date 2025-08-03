import pandas as pd
from itertools import product
from strategy.returns import strategy_returns
from strategy.position import position_change

def equity_curve(returns):
    """
    Computes cumulative equity curve from strategy returns.
    """
    return (1 + returns).cumprod()



def sharpe_ratio(returns, r_f=0.0):
    """
    Computes Sharpe Ratio with r_f = 0
    """
    excess_returns = returns - r_f
    return excess_returns.mean() / excess_returns.std()