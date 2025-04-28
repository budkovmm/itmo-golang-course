def main():
    # todo: Заданы три числа в переменных x, y, z.
    # Напечатать наибольшее из этих чисел.
    # Пример:
    x = 10
    y = 15
    z = 2
    # Ответ:
    # Наибольшее число 15
    print(f"Largest number from {x, y, z}: {find_max(x, y, z)}")

    # Пример:
    x = 77
    y = 9
    z = 130
    # Ответ:
    # Наибольшее число 130
    print(f"Largest number from {x, y, z}: {find_max(x, y, z)}")

    # Задачу решить без функций max и прочих.
    return

def find_max(x:float , y: float, z: float) -> float:
    largest = x

    if y > largest:
        largest = y

    if z > largest:
        largest = z

    return largest

if __name__ == "__main__":
    main()