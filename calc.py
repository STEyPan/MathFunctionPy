def calculate(example: str) -> (int, float):
    first = 0
    second = 0
    sign = ""
    temp = ""

    for char in example:
        if char in "+-/*^":
            sign = char
            first = int(temp)
            temp = ""
        else:
            temp += char
    second = int(temp)

    match sign:
        case "+": return first + second
        case "-": return first - second
        case "*": return first * second
        case "/": return first / second
        case "^": return first ** second

def evalExample():
    example = input("Введите математическое выражение: ")
    print(f"{example}={calculate(example)}")

def fibonacci_recursive(number):
    if number <= 1:
        return number
    return fibonacci_recursive(number-1) + fibonacci_recursive(number - 2)

def fibonacci_cycle(number):
    fib = 0
    num_first = 0
    num_second = 1

    for _ in range(1, number):
        fib = num_first + num_second
        num_second = num_first
        num_first = fib

    return fib

def choiceEvalFib():
    number = int(input("Введите, какое число Фибоначчи Вы хотите найти: "))
    print(f"1) Рекурсивно\n2) Циклом")
    choice = input("Выберете способ нахождения числа Фибоначчи: ")


    match choice:
        case "1": print(f"{number} число Фибоначчи - {fibonacci_recursive(number)}")
        case "2": print(f"{number} число Фибоначчи - {fibonacci_cycle(number)}")
        case _: print("нет такой команды")






# evalExample()