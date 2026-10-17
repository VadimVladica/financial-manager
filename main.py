# Начальные суммы доходов и расходов
income = 0
consumption = 0
while True:
    print("-Financial Manager-")
    print("Выберите действие:")
    print("доход - добавить доход")
    print("расход - добавить расход")
    print("баланс - посмотреть баланс")
    print("выход - завершить программу")

    operation_type = input("Введите команду: ")
    if operation_type == "выход":
        break
    if operation_type == "баланс":
        print("Текущий баланс: ", income - consumption)
        continue
    if (
        operation_type != "доход"
        and operation_type != "расход"
        and operation_type != "баланс"
        and operation_type != "выход"
    ):
        print("Неизвестная команда")
        continue
    # Повторяем ввод, пока сумма не станет положительной
    amount = int(input("Введите число больше 0: "))
    while amount <= 0:
        amount = int(input("Введите число больше 0: "))

    if operation_type == "доход":
        income += amount
        print("Доход добавлен: ", income)
    elif operation_type == "расход":
        consumption += amount
        print("Расход добавлен: ", consumption)
