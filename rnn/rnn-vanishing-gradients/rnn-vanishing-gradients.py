import numpy as np

def compute_gradient_norm_decay(T: int, W_hh: np.ndarray) -> list:
    """
    Simulate gradient norm decay over T time steps.
    Returns list of gradient norms.
    """
    # YOUR CODE HERE
    spectral_norm = np.linalg.norm(W_hh, ord=2)
    gradiant_norm = 1.0
    gradiant_norms = [1.0]
    for i in range(T-1):
        gradiant_norm *= spectral_norm
        gradiant_norms.append(gradiant_norm)
    return gradiant_norms