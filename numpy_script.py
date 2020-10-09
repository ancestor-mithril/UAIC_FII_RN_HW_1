import numpy as np
import functions_numpy as fn
import functions as f


coefficients, results = f.part_1('equation_2.txt')
coefficients = np.array(coefficients)
results = np.array(results)

print(coefficients, 'Coefficients')
print(results, "Answer vector")


coefficients_determinant = np.linalg.det(coefficients)
coefficients_transpose = coefficients.T
coefficients_adjugate = fn.get_adjugate(coefficients)
coefficients_inverse = np.linalg.inv(coefficients)

print(coefficients_determinant, "Determinant")
print(coefficients_transpose, "Transpose")
print(coefficients_adjugate, "Adjugate")
print(coefficients_inverse, "Inverse")


answer = coefficients_inverse @ results
# answer = np.linalg.solve(coefficients, results)
print("x = ", answer[0])
print("y = ", answer[1])
print("z = ", answer[2])
