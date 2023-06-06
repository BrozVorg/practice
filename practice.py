def calculate_determinant(matrix):
    n = len(matrix)

    # Базовый случай: матрица 1x1
    if n == 1:
        return matrix[0][0]

    determinant = 0

    for column in range(n):
        submatrix = [[matrix[i][j] for j in range(n) \
                      if j != column] for i in range(1, n)]
        coefficient = (-1) ** column
        determinant += coefficient * matrix[0][column] \
                       * calculate_determinant(submatrix)

    return determinant

# Ввод размерности матрицы
# r - размерность мтарицы
r = int(input("Введите размерность квадратной матрицы: "))

# Ввод элементов матрицы
# m - матрица
m = []
for i in range(r):
    row = []
    for j in range(r):
        element = int(input(f"Введите элемент [{i+1},{j+1}]: "))
        row.append(element)
    m.append(row)

# Вычисление определителя
determinant = calculate_determinant(m)

print("Определитель матрицы:", determinant)
