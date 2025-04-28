def main():
    # todo: Данные две переменные:
    age = 36.6
    temperature = 25

    # Нужно обменять значения переменных местами. В итого age
    # должен равнятся 25 а temperature – 36.6:
    age, temperature = temperature, age
    print(f"Age: {age}")
    print(f"Temperature: {temperature}")


if __name__ == "__main__":
    main()