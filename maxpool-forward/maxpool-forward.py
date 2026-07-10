def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    H, W = len(X), len(X[0])
    H_out, W_out = int((H - pool_size) / stride) + 1, int((W - pool_size) / stride) + 1
    X_out = [[0] * W_out for _ in range(H_out)]
    
    for i in range(H_out):
        for j in range(W_out):
            max_val = -float('inf')
            
            for k in range(pool_size):
                for l in range(pool_size):
                    max_val = max(max_val, X[i * stride + k][j * stride + l])
                    
            X_out[i][j] = max_val

    return X_out