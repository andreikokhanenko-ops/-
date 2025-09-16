print("1. Доступные опции:")
print("2. Сложение")
print("3. Вычитание")
print("4. Умножение")
print("5. Деление")
print("6. Целочисленное деление")
print("7. Остаток от деления")
print("8. Возведение в степень")


num1 = float(input("Введите первое число: "))
operation = input("Введите операцию (+, -, *, /, //, %, **): ")
num2 = float(input("Введите второе число: "))


if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Ошибка: деление на ноль!")

elif operation == '//':
    if num2 != 0:
        result = num1 // num2
        print(f"{num1} // {num2} = {result}")
    else:
        print("Ошибка: деление на ноль!")

elif operation == '%':
    if num2 != 0:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    else:
        print("Ошибка: деление на ноль!")

elif operation == '**':
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result}")

else:
    print("Ошибка: это обвчный калькулятор, а ваш запрос слишком сложный для него. Пожалуйста, выберите из списка: +, -, *, /, //, %, **")