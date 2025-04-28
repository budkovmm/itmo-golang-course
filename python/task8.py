def main():
    # todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо и справа налево".
    
    try:
        # Считываем четырехзначное число
        number = input("Введите четырехзначное число: ")
        
        # Проверяем, что введено четырехзначное число
        if not number.isdigit() or len(number) != 4:
            print("Ошибка: введите корректное четырехзначное число")
            return
        
        # Проверяем, является ли число палиндромом
        # is_palindrome = number == number[::-1]
        is_palindrome = is_polindrome(number)
        
        # Выводим результат
        if is_palindrome:
            print(f"Число {number} является палиндромом")
        else:
            print(f"Число {number} не является палиндромом")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def is_polindrome(n: int) -> bool:
    # Проверяем, является ли число палиндромом используя два указателя
    left = 0
    right = len(n) - 1
    is_palindrome = True
        
    while left < right:
        if n[left] != n[right]:
            is_palindrome = False
            break
        left += 1
        right -= 1

    return is_palindrome

if __name__ == "__main__":
    main()
