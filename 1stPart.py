import random
import os
import math
from functools import reduce

def input_and_print():
#Считать информацию с клавиатуры и вывести на экран.
    try:
        data = input("Введите данные: ")
        print(f"Введенные данные: {data}")
    except Exception as e:
        print(f"Ошибка: {e}")

def input_to_file(filename):
#Считать информацию с клавиатуры и записать в файл
    try:
        data = input("Введите данные для записи в файл: ")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"Данные записаны в файл {filename}")
    except Exception as e:
        print(f"Ошибка: {e}")

def read_from_file(filename):
#Считать информацию из файла и вывести на экран
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
        print(f"Содержимое файла {filename}:\n{data}")
    except FileNotFoundError:
        print("Файл не найден!")
    except Exception as e:
        print(f"Ошибка: {e}")

def input_to_start_of_file(filename):
#Считать информацию с клавиатуры и записать в начало файла.
    try:
        data = input("Введите данные для записи в начало файла: ")
        with open(filename, "r+", encoding="utf-8") as f:
            old_data = f.read()
            f.seek(0)
            f.write(data + "\n" + old_data)
        print(f"Данные добавлены в начало файла {filename}")
    except FileNotFoundError:
        print("Файл не найден!")
    except Exception as e:
        print(f"Ошибка: {e}")

def create_vector():
#Создать массив (вектор) и вывести на экран.
    try:
        n = int(input("Введите количество элементов в векторе: "))
        vector = [int(input(f"Введите элемент {i + 1}: ")) for i in range(n)]
        print("Созданный вектор:", vector)
        return vector
    except ValueError:
        print("Ошибка: введите числовое значение.")
        return []

def read_vector_from_input():
#Считать вектор с клавиатуры, оформить и вывести на экран
    try:
        vector = list(map(int, input("Введите элементы вектора через пробел: ").split()))
        print("Считанный вектор:", vector)
        return vector
    except ValueError:
        print("Ошибка: введите числовые значения через пробел.")
        return []

def random_vector(size):
#Создать вектор, заполненный случайными значениями, и вывести на экран
    vector = [random.randint(0, 100) for _ in range(size)]
    print("Сгенерированный случайный вектор:", vector)
    return vector

def random_vector_with_range(size, min_val, max_val, filename):
#Создать вектор с генератором случайных значений в заданном диапазоне и записать в файл
    global vector
    try:
        vector = [random.randint(min_val, max_val) for _ in range(size)]
        print("Сгенерированный вектор:", vector)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(" ".join(map(str, vector)))
        print(f"Вектор записан в файл {filename}")
        return vector
    except Exception as e:
        print(f"Ошибка: {e}")
        return []

def reverse_vector(vector):
#Вывести вектор в обратной последовательности
    if vector:
        print("Вектор в обратном порядке:", vector[::-1])
    else:
        print("Ошибка: Вектор еще не был создан.")

def sort_vector(vector, order):
#Отсортировать вектор по возрастанию или убыванию в зависимости от ключа
    if order == "asc":
        print("Отсортированный вектор (по возрастанию):", sorted(vector))
    elif order == "desc":
        print("Отсортированный вектор (по убыванию):", sorted(vector, reverse=True))
    else:
        print("Ошибка: неверный ключ сортировки. Используйте 'asc' или 'desc'.")

def find_min_max(vector, key):
#Найти минимальное или максимальное значение в векторе в зависимости от ключа
    if key == "min":
        print("Минимальное значение вектора:", min(vector))
    elif key == "max":
        print("Максимальное значение вектора:", max(vector))
    else:
        print("Ошибка: неверный ключ поиска. Используйте 'min' или 'max'.")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_gcd_in_vector(vector):
#Найти НОД всех элементов вектора
    result = reduce(gcd, vector)
    print("НОД всех элементов вектора:", result)

def compare_vectors():
#Считать 2 вектора и сравнить их сумму, вывести вектор с наименьшей суммой
    print("Введите первый вектор:")
    vector1 = read_vector_from_input()
    print("Введите второй вектор:")
    vector2 = read_vector_from_input()

    sum1, sum2 = sum(vector1), sum(vector2)
    if sum1 < sum2:
        print("Первый вектор имеет меньшую сумму:", vector1)
    elif sum2 < sum1:
        print("Второй вектор имеет меньшую сумму:", vector2)
    else:
        print("Суммы векторов равны.")

def main_menu():
    while True:
        print("\nВыберите действие:")
        print("1. Ввод данных и вывод на экран")
        print("2. Запись данных в файл")
        print("3. Чтение данных из файла")
        print("4. Запись данных в начало файла")
        print("5. Создать и вывести вектор")
        print("6. Считать и вывести вектор")
        print("7. Генерация случайного вектора")
        print("8. Генерация случайного вектора с диапазоном и запись в файл")
        print("9. Вектор в обратном порядке")
        print("10. Сортировка вектора")
        print("11. Минимальное/максимальное значение вектора")
        print("12. НОД элементов вектора")
        print("13. Сравнить два вектора")
        print("0. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            input_and_print()
        elif choice == "2":
            input_to_file("data.txt")
        elif choice == "3":
            read_from_file("data.txt")
        elif choice == "4":
            input_to_start_of_file("data.txt")
        elif choice == "5":
            create_vector()
        elif choice == "6":
            read_vector_from_input()
        elif choice == "7":
            size = int(input("Размер вектора: "))
            random_vector(size)
        elif choice == "8":
            size = int(input("Размер вектора: "))
            min_val = int(input("Минимальное значение: "))
            max_val = int(input("Максимальное значение: "))
            random_vector_with_range(size, min_val, max_val, "vector.txt")
        elif choice == "9":
            vector = read_vector_from_input()
            reverse_vector(vector)
        elif choice == "10":
            vector = read_vector_from_input()
            order = input("Введите ключ сортировки (asc/desc): ")
            sort_vector(vector, order)
        elif choice == "11":
            vector = read_vector_from_input()
            key = input("Введите 'min' или 'max': ")
            find_min_max(vector, key)
        elif choice == "12":
            vector = read_vector_from_input()
            find_gcd_in_vector(vector)
        elif choice == "13":
            compare_vectors()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()