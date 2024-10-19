def save_calculation_to_file(result):
    with open('calculations.txt', 'a') as file:
        file.write(f"{result}\n")


def view_history():
    try:
        with open('calculations.txt', 'r') as file:
            history = file.readlines()
            print("История вычислений:")
            for line in history:
                print(line.strip())
    except FileNotFoundError:
        print("История пуста.")


def calculate():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Просмотр истории вычислений")
        choice = input("Введите номер операции (1/2/3/4/5): ")

        if choice == '5':
            view_history()
            continue

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            result = num1 + num2
            operation = f"{num1}+{num2}={result}"
        elif choice == '2':
            result = num1 - num2
            operation = f"{num1}-{num2}={result}"
        elif choice == '3':
            result = num1 * num2
            operation = f"{num1}*{num2}={result}"
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                operation = f"{num1}/{num2}={result:.2f}"
            else:
                print("Ошибка: деление на ноль.")
                continue
        else:
            print("Неверный выбор. Попробуйте снова.")
            continue

        print(f"Результат: {operation}")
        save_calculation_to_file(f"Результат: {operation}")


if __name__ == "__main__":
    calculate()