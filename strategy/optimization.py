import pandas as pd
from itertools import product

from strategy.position import position_change
from strategy.returns import strategy_returns
from metrics.performance import equity_curve, sharpe_ratio

def optimal_strategy_list(z_score, ret_1, ret_2, entry_thresholds, exit_thresholds):
    results = []
    for entry_t, exit_t in product(entry_thresholds, exit_thresholds):
        positions = pd.Series(position_change(z_score, entry_t, exit_t), index=z_score.index)
        ret_array = strategy_returns(ret_1, ret_2, positions)
        strategy_ret = pd.Series(ret_array, index=z_score.index[1:])
        
        strat_ret_clean = strategy_ret.dropna()
        
        equity = equity_curve(strat_ret_clean)
        sharpe = sharpe_ratio(strat_ret_clean)
        total_return = equity.iloc[-1] - 1
        
        results.append({
            'Entry': entry_t,
            'Exit': exit_t,
            'Sharpe Ratio': sharpe,
            'Total Return': total_return
        })
    return pd.DataFrame(results)


def optimal_parameters(optimal_strat: pd.DataFrame):
    """
    Returns the optimal entry and exit thresholds when maximizing the Sharpe Ratio.
    """
    optimal_sorted = optimal_strat.sort_values(by='Sharpe Ratio', ascending=False)
    optimal_params = optimal_sorted[['Entry', 'Exit']].iloc[0].values
    return optimal_params