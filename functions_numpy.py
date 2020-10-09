import numpy as np
import typing


def get_adjugate(matrix: np.ndarray) -> np.ndarray:
    """
    https://stackoverflow.com/a/6528024

    :param matrix: 3 x 3 matrix
    :return: adjugate
    """
    cofactor = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            minor = np.zeros((2, 2))
            minor[:i, :j] = matrix[:i, :j]
            minor[i:, :j] = matrix[i + 1:, :j]
            minor[:i, j:] = matrix[:i, j + 1:]
            minor[i:, j:] = matrix[i + 1:, j + 1:]
            cofactor[i, j] = (-1) ** (i + j) * np.linalg.det(minor)
    return cofactor.T
