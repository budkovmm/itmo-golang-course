def main():
    #todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
    # результат целочисленного деления, результат деления с остатком, результат возведения в степень.
    
    try:
        # Считываем два числа
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        # Выполняем арифметические операции
        sum_result = num1 + num2
        difference = num1 - num2
        product = num1 * num2
        
        # Проверяем деление на ноль
        if num2 != 0:
            quotient = num1 / num2
            floor_division = num1 // num2
            remainder = num1 % num2
        else:
            quotient = "не определено (деление на ноль)"
            floor_division = "не определено (деление на ноль)"
            remainder = "не определено (деление на ноль)"
        
        # Возведение в степень
        power = num1 ** num2
        
        # Выводим результаты
        print(f"\nРезультаты операций:")
        print(f"Сумма: {sum_result}")
        print(f"Разность: {difference}")
        print(f"Частное: {quotient}")
        print(f"Произведение: {product}")
        print(f"Целочисленное деление: {floor_division}")
        print(f"Остаток от деления: {remainder}")
        print(f"Возведение в степень: {power}")
        
    except ValueError:
        print("Ошибка: Введите корректные числа")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()

