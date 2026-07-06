def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here
    n = len(values)
    if n == 1:
        return [0.0]
        
    def quartiles(n, mid, mid2):
        sorted_values = sorted(values)
        if n % 2 != 0:
            Q2 = sorted_values[mid]
        else:
            Q2 = (sorted_values[mid-1] + sorted_values[mid]) / 2
            
        if mid % 2 != 0:
            Q1 = sorted_values[mid2]
            Q3 = sorted_values[n-mid2-1]
        else:
            Q1 = (sorted_values[mid2-1] + sorted_values[mid2]) / 2
            Q3 = (sorted_values[n-mid2-1] + sorted_values[n-mid2]) / 2
            
        return Q1, Q2, Q3
        
    mid = n // 2
    mid2 = mid // 2
    Q1, Q2, Q3 = quartiles(n, mid, mid2)
    
    IQR = Q3 - Q1
    if IQR == 0:
        IQR += 1

    if IQR == 0: IQR += 1
    values_scaled = [0.0] * n
    for i in range(n):
        values_scaled[i] = (values[i] - Q2) / IQR 
            
    return values_scaled