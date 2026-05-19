import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)
    if np.sum(p) != 1:
        raise ValueError("Probabilities sum exceeded 1!")
        
    Ex = np.sum(x.T @ p)
    return Ex