import numpy as np
from sklearn.linear_model import LinearRegression


def regression(X, y):
    """
    Run simple linear regression of y on X.
    """
    reg = LinearRegression()
    reg.fit(X.values.reshape(-1,1), y)
    return reg.coef_[0]

def log_regression(X, y):
    """
    Run linear regression fo y on log(X).
    """
    reg = LinearRegression()
    reg.fit(np.log(X.values).reshape(-1, 1), y)
    return reg.coef_[0]

