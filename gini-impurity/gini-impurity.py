from collections import Counter

def gini_t(n, y):
    gini = 1
    for _, v in Counter(y).items():
        gini -= (v / n) ** 2
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
        
    gini_l, gini_r = gini_t(n_l, y_left), gini_t(n_r, y_right)
    gini_split = (n_l * gini_l + n_r * gini_r) / n
    return gini_split