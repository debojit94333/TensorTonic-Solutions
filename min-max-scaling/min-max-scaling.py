def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    m, n = len(data), len(data[0])
    data_norm = [[0] * n for _ in range(m)]
    
    for i in range(n):
        Max, Min = -float('inf'), float('inf')
        for j in range(m):
            Max = max(Max, data[j][i])
            Min = min(Min, data[j][i])
            
        Range = Max - Min
        for j in range(m):
            if Range:
                x = (data[j][i] - Min) / Range
            else:
                x = 0.0
            data_norm[j][i] = x

    return data_norm