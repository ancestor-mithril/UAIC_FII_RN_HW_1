from typing import List


def split_equation(string: str) -> List[str]:
    """
    :param string: an equation
    :return: a list containing only integers and their signs, or empty string
    """
    import re
    max_split = 0
    string = string.replace(" ", "")
    delimiters = "x", "y", "z", "="
    regex_pattern = "|".join(map(re.escape, delimiters))
    return re.split(regex_pattern, string, max_split)


def get_equation_coefficients(equation_string: str, coefficient_list: List[str]) -> List[float]:
    """
    :param equation_string: string containing system line
    :param coefficient_list: list of system numbers and their signs
    :return: vector of exactly 3 float coefficients
    """
    position = 0
    coefficient_list = [(x + '1') if x == '-' or x == '+' else 0 if x == '' else x for x in coefficient_list]
    coefficients = []
    for i in "xyz":
        if i in equation_string:
            coefficients.append(float(coefficient_list[position]))
            position += 1
        else:
            coefficients.append(0)
    return coefficients


def get_3x3_determinant(matrix: List[List[float]]) -> float:
    """
    :param matrix: 3 x 3 matrix
    :return: determinant of given  matrix
    """
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def get_2x2_determinant(matrix: List[List[float]]) -> float:
    """
    :param matrix: 2 x 2 matrix
    :return: determinant
    """
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def get_transpose(matrix: List[List[float]]) -> List[List[float]]:
    """
    :param matrix: a 3 x 3 matrix
    :return: the transpose
    """
    return list(map(list, zip(*matrix)))


def get_adjugate(matrix: List[List[float]]) -> List[List[float]]:
    """
    :param matrix: a 3 x 3 matrix
    :return: the adjugate
    """
    cofactor = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            minor = [[matrix[row][col] for row in range(3) if row != i] for col in range(3) if col != j]
            cofactor[i][j] = (-1) ** (i + j) * get_2x2_determinant(minor)
    return get_transpose(cofactor)


def part_1(target_file: str) -> (List[List[float]], List[float]):
    """
    Transformarea sub forma de matrice:

    :param target_file: path to file
    :return: the linear system matrix and results array
    """
    with open(target_file, 'r') as fd:
        equations = fd.read().splitlines()
    coefficients = []
    results = []
    for equation in equations:
        data = split_equation(equation)
        coefficients.append(get_equation_coefficients(equation, data))
        results.append(float(data[-1]))
    return coefficients, results


def part_2(coefficients) -> (float, List[List[float]], List[List[float]], List[List[float]]):
    """
    Calcularea inversei unei matrici
        a. Calcularea determinantului (se verifica sa nu fie 0)
        b. Scrierea matricei transpuse
        c. Calcularea matricei A*
        d. Impartim fiecare element din matricea A* la determinant

    :param coefficients: 3 x 3 matrix
    :return: determinant, transpose, adjugate and inverse of matrix (if possible, else none)
    """
    coefficients_determinant = get_3x3_determinant(coefficients)
    coefficients_transpose = get_transpose(coefficients)
    coefficients_adjugate = get_adjugate(coefficients)
    if coefficients_determinant == 0:
        return 0, coefficients_transpose, coefficients_adjugate, None
    coefficients_inverse = [[x / coefficients_determinant for x in row] for row in coefficients_adjugate]
    return coefficients_determinant, coefficients_transpose, coefficients_adjugate, coefficients_inverse


def part_3(coefficients_inverse: List[List[float]], results: List[float]) -> List[float]:
    """
    :param coefficients_inverse: 3 x 3 matrix
    :param results: 3 - elements array representing 3 x 1 matrix
    :return: array representing 1 x 3 result of multiplication
    """
    return [sum([x * y for x, y in zip(row, results)]) for row in coefficients_inverse]
