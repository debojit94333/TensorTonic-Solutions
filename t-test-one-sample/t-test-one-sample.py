import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    n = len(x)
    x = np.array(x)
    x_mean = np.mean(x)
    s = np.sqrt(np.sum(np.square(x - x_mean)) / (n-1))
    t = (x_mean - mu0) / (s / np.sqrt(n))
    return t