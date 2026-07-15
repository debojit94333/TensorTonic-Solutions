def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    users = len(ground_truth)
    hits = 0
    for i in range(users):
        top_k = set(recommendations[i][:k])
        for item in ground_truth[i]:
            if item in top_k:
                hits += 1
                break
    
    return hits / users    