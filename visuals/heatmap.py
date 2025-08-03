import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

def heatmap_sr(strategy):
    df_strategy = pd.DataFrame(strategy)
    df_pivot = df_strategy.pivot(index="Entry", columns="Exit", values="Sharpe Ratio")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_pivot, annot=True, fmt=".4f", cmap="coolwarm", center=0)
    plt.title("Heatmap of Sharpe Ratios")
    plt.xlabel("Exit Threshold")
    plt.ylabel("Entry Threshold")
    plt.tight_layout()
    plt.show()
    