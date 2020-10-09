import functions as f


coefficients, results = f.part_1('equation_2.txt')

print(coefficients, 'Coefficients')
print(results, "Answer vector")


coefficients_determinant, \
    coefficients_transpose, \
    coefficients_adjugate, \
    coefficients_inverse = f.part_2(coefficients)

print(coefficients_determinant, "Determinant")
print(coefficients_transpose, "Transpose")
print(coefficients_adjugate, "Adjugate")
print(coefficients_inverse, "Inverse")


if coefficients_inverse is not None:
    answer = f.part_3(coefficients_inverse, results)
    print("x = ", answer[0])
    print("y = ", answer[1])
    print("z = ", answer[2])
else:
    print("the system has either no nontrivial solutions or an infinite number of solutions")
