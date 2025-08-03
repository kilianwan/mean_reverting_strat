import pandas as pd
from utils.adftest import adftest
from strategy.returns import returns, strategy_returns
from strategy.position import position_change
from strategy.optimization import optimal_strategy_list, optimal_parameters
from metrics.performance import equity_curve, sharpe_ratio
from visuals.equity_plot import plot_equity_curve
from visuals.heatmap import heatmap_sr
from backtest.run_gridsearch import run_gridsearch
from utils.z_score import z_score
from utils.regression import regression

# load prices (preprocessed from load_data.py)
df = pd.read_csv("data/pair_ko_pep.csv", index_col="date", parse_dates=True)
price_1 = df["KO"]
price_2 = df["PEP"]
print("Data loaded!")

# Step 0 : Check cointegration
hedge_ratio = regression(X=price_2, y=price_1)
spread = price_1 - hedge_ratio * price_2
adf_result = adftest(data=spread, level=0.05)

if adf_result['conclusion'] != "reject null hypothesis":
    print("The spread is not stationary. KO and PEP are likely not cointegrated")
    exit()
else: print("The spread is stationary, we can proceed with the strategy.")

# Step 1 : Build z_score
z = z_score(spread, window_size=30)

# Step 2 : Asset Returns
ret_1 = returns(price_1)
ret_2 = returns(price_2)

# Step 3 : Run parameter grid search
results = run_gridsearch(z_score=z,
                         ret_1=ret_1,
                         ret_2=ret_2)

# Step 4 : Visualize heatmap (not displayed for simplicity)
#heatmap_sr(results) 

# Step 5 : Best parameters
best = optimal_parameters(results)
print("Best strategy parameters:")
print(best)

# Step 6 : Final equity curve
positions = position_change(z_score=z,
                            entry_threshold=best[0],
                            exit_threshold=best[1])

best_strat_ret = strategy_returns(ret_1=ret_1,
                                ret_2=ret_2,
                                positions=positions)

equity = equity_curve(best_strat_ret)
plot_equity_curve(equity)
