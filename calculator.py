import re

def main(input_str: str) -> str:
    a = input_str
    znakSearch = re.search(r"(?<=\d)[\+\-\*/]", a)
    try:
        znak = znakSearch.group()
        if znakSearch is None:
            raise AttributeError
    except AttributeError:
        return "throws Exception //т.к. строка не является математической операцией"
    chisla = a.split(znak)
    if len(chisla) > 2:
        return("throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один "
            "оператор (+, -, /, *)")
    try:
        num1 = int(chisla[0])
        num2 = int(chisla[1])
    except ValueError:
        return "throws Exception //т.к. калькулятор работает только с целыми числами"
    try:
        if not (1<=num1<=10 and 1<=num2<=10):
            raise ValueError("throws Exception")
    except ValueError as e:
        return str(e)
    if znak == "+":
        return str(num1 + num2)
    elif znak == "-":
        return str(num1 - num2)
    elif znak == "*":
        return str(num1 * num2)
    elif znak == "/":
        return str(num1 // num2)
    else:
        return("throws Exception //т.к. Неверная арифметичкеская операция")

if __name__ == "__main__":
    user_input = input("Введи выражения от 1 до 10 (например, 5+3): ")
    result = main(user_input)
    print(result)