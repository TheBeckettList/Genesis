import numpy as np

class SubstratePhysics:
    def __init__(self, epsilon=1.0, J=0.1, lmbda=0.01):
        self.epsilon = epsilon  # Bit cost
        self.J = J              # Gravity/Clustering
        self.lmbda = lmbda      # Mass/Hub Penalty

    def calculate_energy(self, adjacency_matrix):
        """
        Calculates the Hamiltonian H(G) for a given lattice state.
        """
        nodes = adjacency_matrix.shape[0]
        degrees = np.sum(adjacency_matrix, axis=1)
        
        # H = ε(nodes) - J(edges) + λ(degree sum squared)
        existence_cost = self.epsilon * nodes
        clustering_incentive = self.J * (np.sum(adjacency_matrix) / 2)
        hub_penalty = self.lmbda * np.sum(degrees**2)
        
        return existence_cost - clustering_incentive + hub_penalty

print("--- 01/10 Substrate Hamiltonian Initialized ---")
