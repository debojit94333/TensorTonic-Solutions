import numpy as np

def single_node_gini_impurity(y, n):
    """
    Calculate gini impurity for a single node.
    """
    if n == 0: 
        return 0
        
    d = {}
    for i in y:
        if i not in d:
            d[i] = 0
        d[i] += 1

    gini = 1
    for i in d.values():
        p = i / n
        gini -= p**2
        
    return gini

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    n_l, n_r = len(y_left), len(y_right)
    n = n_l + n_r
    if n == 0:
        return 0.0

    gini_l = single_node_gini_impurity(y_left, n_l)
    gini_r = single_node_gini_impurity(y_right, n_r)
    gini_split = n_l/n * gini_l + n_r/n * gini_r

    return gini_split