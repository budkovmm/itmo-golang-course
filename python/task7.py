def main():
    #todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
    # Примечание: все точки получаем через функцию input().
    
    try:
        # Считываем координаты точек
        A = float(input("Введите координату точки A: "))
        B = float(input("Введите координату точки B: "))
        C = float(input("Введите координату точки C: "))
        
        # Вычисляем длины отрезков
        AC = abs(C - A)
        BC = abs(C - B)
        
        # Вычисляем сумму длин
        sum_lengths = AC + BC
        
        # Выводим результаты
        print(f"\nРезультаты:")
        print(f"Длина отрезка AC: {AC}")
        print(f"Длина отрезка BC: {BC}")
        print(f"Сумма длин отрезков AC и BC: {sum_lengths}")
        
    except ValueError:
        print("Ошибка: введите корректные числа")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
