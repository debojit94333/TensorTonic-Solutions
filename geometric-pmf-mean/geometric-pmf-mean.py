import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    n = len(k)
    pmf = np.zeros(n)
    for i in range(n):
        P = (1 - p) ** (k[i] - 1) * p 
        pmf[i] = P
        
    mean = 1 / p 
    return pmf, mean