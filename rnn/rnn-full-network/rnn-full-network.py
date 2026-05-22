import numpy as np

class VanillaRNN:
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim

        # Xavier initialization
        self.W_xh = np.random.randn(hidden_dim, input_dim) * np.sqrt(2.0 / (input_dim + hidden_dim))
        self.W_hh = np.random.randn(hidden_dim, hidden_dim) * np.sqrt(2.0 / (2 * hidden_dim))
        self.W_hy = np.random.randn(output_dim, hidden_dim) * np.sqrt(2.0 / (hidden_dim + output_dim))
        self.b_h = np.zeros(hidden_dim)
        self.b_y = np.zeros(output_dim)

    def forward(self, X: np.ndarray, h_0: np.ndarray = None) -> tuple:
        """
        Forward pass through entire sequence.

        X shape: (batch, T, input_dim)

        Returns:
            y_seq: (batch, T, output_dim)
            h_final: (batch, hidden_dim)
        """
        # YOUR CODE HERE
        batch, T, _ = X.shape
        prev_h_t = h_0
        y_seq = np.zeros((batch, T, self.output_dim))
        
        for t in range(T):
            x = X[:, t, :]
                
            current_h_t = np.tanh(x @ self.W_xh.T + prev_h_t @ self.W_hh.T + self.b_h)
            y_t = current_h_t @ self.W_hy.T + self.b_y
            
            y_seq[:, t, :] = y_t
            prev_h_t = current_h_t
            
        return y_seq, prev_h_t