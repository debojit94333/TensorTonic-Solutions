import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    if not vocab:
        return np.array([], dtype=int)
        
    vocab_dict = {word: 0 for word in vocab}
    for token in tokens:
        if token in vocab_dict:
            vocab_dict[token] += 1

    return np.array(list(vocab_dict.values()))