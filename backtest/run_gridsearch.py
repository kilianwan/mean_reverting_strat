import pandas as pd
from strategy.optimization import optimal_strategy_list

def run_gridsearch(z_score, ret_1, ret_2, entry_threshold=None, exit_threshold=None):
    if entry_threshold is None:
        entry_threshold = [0.5, 1.0, 1.5, 2.0, 2.5]
    if exit_threshold is None:
        exit_threshold = [0.05, 0.1, 0.25, 0.5, 1.0]
    results_df = optimal_strategy_list(
        z_score=z_score,
        ret_1=ret_1,
        ret_2=ret_2,
        entry_thresholds=entry_threshold,
        exit_thresholds=exit_threshold
    )
    return results_df
        