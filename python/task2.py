def main():
    # todo: Преобразуйте переменную age и foo в число
    age = "23"
    foo = "23abc"

    age_int = int(age)
    print(f"Integer value of age: {age_int}")

    try:
        foo_int = int(foo)
    except ValueError as e:
        print(f"Error converting foo to integer: {e}")
    
    # Преобразуйте переменную age в Boolean
    age_str = "123abc"
    age_bool = bool(age_str)
    print(f"Boolean value of age_str: {age_bool}")
    
    # Преобразуйте переменную flag в Boolean
    flag = 1
    flag_bool = bool(flag)
    print(f"Boolean value of flag: {flag_bool}")
    
    # Преобразуйте значение в Boolean
    str_one = "Privet"
    str_two = ""
    str_one_bool = bool(str_one)
    str_two_bool = bool(str_two)
    print(f"Boolean value of str_one: {str_one_bool}")
    print(f"Boolean value of str_two: {str_two_bool}")

    # Преобразуйте значение 0 и 1 в Boolean
    print(f"Boolean value of 0: {bool(0)}")
    print(f"Boolean value of 1: {bool(1)}")

    # Преобразуйте False в строку
    print(f"Stringified False: {str(False)}")

if __name__ == "__main__":
    main()