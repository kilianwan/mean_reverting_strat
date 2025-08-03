import matplotlib.pyplot as plt 

def plot_equity_curve(equity):
    plt.figure(figsize=(10, 5))
    plt.plot(equity, label="Equity Curve", color='blue')
    plt.title("Equity Curve of Mean-Reversion Strategy")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()