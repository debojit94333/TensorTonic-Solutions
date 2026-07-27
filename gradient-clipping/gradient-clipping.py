import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    g = np.asarray(g)
    if max_norm <= 0:
        return g
        
    g_norm = np.linalg.norm(g)
    if g_norm > max_norm:
        g_clipped = g * (max_norm / g_norm)
    else:
        g_clipped = g.copy()
        
    return g_clipped