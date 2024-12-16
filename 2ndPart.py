import random
import numpy as np


def create_matrix_from_vectors():
#Создать матрицу из нескольких введенных векторов
    try:
        n = int(input("Введите количество строк матрицы: "))
        m = int(input("Введите количество столбцов матрицы: "))
        print("Введите элементы матрицы построчно через пробел:")
        matrix = []
        for i in range(n):
            row = list(map(int, input(f"Строка {i + 1}: ").split()))
            if len(row) != m:
                raise ValueError("Некорректное количество элементов в строке.")
            matrix.append(row)
        matrix = np.array(matrix)
        print("\nСозданная матрица:")
        print(matrix)
        return matrix
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None

def delete_column(matrix):
#Удалить столбец из матрицы по индексу
    try:
        col_index = int(input("Введите индекс столбца для удаления: "))
        if 0 <= col_index < matrix.shape[1]:
            matrix = np.delete(matrix, col_index, axis=1)
            print("\nМатрица после удаления столбца:")
            print(matrix)
        else:
            print("Ошибка: Некорректный индекс столбца.")
    except ValueError:
        print("Ошибка: Введите числовое значение.")
    return matrix


def transpose_matrix(matrix):
#ранспонировать матрицу
    transposed = np.transpose(matrix)
    print("\nТранспонированная матрица:")
    print(transposed)
    return transposed


def delete_main_diagonal(matrix):
#далить главную диагональ из матрицы
    for i in range(min(matrix.shape[0], matrix.shape[1])):
        matrix[i][i] = None
    matrix = np.array([[val for val in row if val is not None] for row in matrix], dtype=object)
    print("\nМатрица после удаления главной диагонали:")
    print(matrix)
    return matrix


def delete_secondary_diagonal(matrix):
#Удалить побочную диагональ из матрицы
    for i in range(min(matrix.shape[0], matrix.shape[1])):
        matrix[i][-1 - i] = None
    matrix = np.array([[val for val in row if val is not None] for row in matrix], dtype=object)
    print("\nМатрица после удаления побочной диагонали:")
    print(matrix)
    return matrix


def replace_row_with_random(matrix):
#Заменить указанную строку случайной строкой из матрицы
    try:
        row_index = int(input("Введите индекс строки для замены: "))
        if 0 <= row_index < matrix.shape[0]:
            random_row_index = random.randint(0, matrix.shape[0] - 1)
            matrix[row_index] = matrix[random_row_index]
            print(f"\nСтрока {row_index} заменена на строку {random_row_index}:")
            print(matrix)
        else:
            print("Ошибка: Некорректный индекс строки.")
    except ValueError:
        print("Ошибка: Введите числовое значение.")
    return matrix


def replace_column_with_other(matrix):
#Заменить столбец в матрице другим столбцом из новой матрицы
    try:
        col_index = int(input("Введите индекс столбца для замены: "))
        new_matrix = create_matrix_from_vectors()
        if new_matrix is not None and new_matrix.shape[0] == matrix.shape[0]:
            new_col_index = int(input("Введите индекс столбца из новой матрицы: "))
            if 0 <= new_col_index < new_matrix.shape[1] and 0 <= col_index < matrix.shape[1]:
                matrix[:, col_index] = new_matrix[:, new_col_index]
                print("\nМатрица после замены столбца:")
                print(matrix)
            else:
                print("Ошибка: Некорректный индекс столбца.")
    except ValueError:
        print("Ошибка: Введите числовое значение.")
    return matrix


def find_and_zero_matrix(matrix):
#Найти кратный элемент и заменить строку/столбец на нули
    try:
        value = int(input("Введите значение для поиска кратных элементов: "))
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j] % value == 0:
                    if j % 2 == 0:
                        matrix[i, :] = 0
                    else:
                        matrix[:, j] = 0
                    print("\nМатрица после обнуления строки или столбца:")
                    print(matrix)
                    return matrix
        print("\nЭлемент, кратный значению, не найден.")
    except ValueError:
        print("Ошибка: Введите числовое значение.")
    return matrix


def calculate_determinant():
#Вычислить детерминант квадратной матрицы
    matrix = create_matrix_from_vectors()
    if matrix is not None and matrix.shape[0] == matrix.shape[1]:
        det = np.linalg.det(matrix)
        print(f"\nДетерминант матрицы: {det}")
    else:
        print("Ошибка: Матрица должна быть квадратной.")


def multiply_matrices():
#Перемножить две матрицы
    print("\nСоздайте первую матрицу:")
    matrix1 = create_matrix_from_vectors()
    print("\nСоздайте вторую матрицу:")
    matrix2 = create_matrix_from_vectors()
    if matrix1 is not None and matrix2 is not None and matrix1.shape[1] == matrix2.shape[0]:
        result = np.dot(matrix1, matrix2)
        print("\nРезультат умножения матриц:")
        print(result)
    else:
        print("Ошибка: Несоответствующие размеры матриц.")


def swap_rows(matrix):
#Поменять местами две строки матрицы
    try:
        row1 = int(input("Введите индекс первой строки: "))
        row2 = int(input("Введите индекс второй строки: "))
        if 0 <= row1 < matrix.shape[0] and 0 <= row2 < matrix.shape[0]:
            matrix[[row1, row2]] = matrix[[row2, row1]]
            print("\nМатрица после замены строк:")
            print(matrix)
        else:
            print("Ошибка: Некорректные индексы строк.")
    except ValueError:
        print("Ошибка: Введите числовое значение.")
    return matrix


def main():
    matrix = None
    while True:
        print("Выберите действие:")
        print("1. Создать матрицу")
        print("2. Удалить столбец")
        print("3. Транспонировать матрицу")
        print("4. Удалить главную диагональ")
        print("5. Удалить побочную диагональ")
        print("6. Заменить строку случайной строкой")
        print("7. Заменить столбец из другой матрицы")
        print("8. Найти кратный элемент и обнулить строку")
        print("9. Вычислить детерминант квадратной матрицы")
        print("10. Перемножить 2 матрицы")
        print("11. Поменять местами две строки матрицы.")
        print("0. Выход")

        choice = input("Введите номер действия: ")
        if choice == "1":
            matrix = create_matrix_from_vectors()
        elif choice == "2" and matrix is not None:
            matrix = delete_column(matrix)
        elif choice == "3" and matrix is not None:
            matrix = transpose_matrix(matrix)
        elif choice == "4" and matrix is not None:
            matrix = delete_main_diagonal(matrix)
        elif choice == "5" and matrix is not None:
            matrix = delete_secondary_diagonal(matrix)
        elif choice == "6" and matrix is not None:
            matrix = replace_row_with_random(matrix)
        elif choice == "7" and matrix is not None:
            matrix = replace_column_with_other(matrix)
        elif choice == "8" and matrix is not None:
            matrix = find_and_zero_matrix(matrix)
        elif choice == "9":
            calculate_determinant()
        elif choice == "10":
            multiply_matrices()
        elif choice == "11" and matrix is not None:
            matrix = swap_rows(matrix)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод или матрица еще не создана. Попробуйте снова.")


if __name__ == "__main__":
    main()
