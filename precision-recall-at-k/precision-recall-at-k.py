def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    rec_set = set(recommended[:k])
    hits = 0
    for r in relevant:
        if r in rec_set:
            hits += 1

    precision = hits / k
    recall = hits / len(relevant)
    return [precision, recall]