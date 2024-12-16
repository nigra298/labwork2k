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
#Транспонировать матрицу
    transposed = np.transpose(matrix)
    print("\nТранспонированная матрица:")
    print(transposed)
    return transposed


def delete_main_diagonal(matrix):
#Удалить главную диагональ из матрицы
    try:
        n, m = matrix.shape
        new_matrix = []
        for i in range(n):
            row = [int(matrix[i, j]) for j in range(m) if i != j]  # Преобразование к int
            new_matrix.append(row)

        print("\nМатрица после удаления главной диагонали:")
        for row in new_matrix:
            print(" ".join(map(str, row)))
        return np.array(new_matrix, dtype=int)  # Возвращаем матрицу с обычными int
    except Exception as e:
        print(f"Ошибка: {e}")
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
        print("5. Заменить столбец из другой матрицы")
        print("6. Найти кратный элемент и обнулить строку")
        print("7. Вычислить детерминант квадратной матрицы")
        print("8. Перемножить 2 матрицы")
        print("9. Поменять местами две строки матрицы.")
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
            matrix = replace_column_with_other(matrix)
        elif choice == "6" and matrix is not None:
            matrix = find_and_zero_matrix(matrix)
        elif choice == "7":
            calculate_determinant()
        elif choice == "8":
            multiply_matrices()
        elif choice == "9" and matrix is not None:
            matrix = swap_rows(matrix)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод или матрица еще не создана. Попробуйте снова.")


if __name__ == "__main__":
    main()
