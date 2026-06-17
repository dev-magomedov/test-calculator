import re

a = input("Введи числа от 1 до 10, используй только +, -, *, /")
znakSearch = re.search(r"(?<=\d)[\+\-\*/]", a)
try:
    znak = znakSearch.group()
    if znakSearch is None:
        raise AttributeError
except AttributeError:
    print("throws Exception //т.к. строка не является математической операцией")
    exit()
chisla = a.split(znak)
if len(chisla) > 2:
    print("throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один "
          "оператор (+, -, /, *)")
    exit()
try:
    num1 = int(chisla[0])
    num2 = int(chisla[1])
except ValueError:
    print("throws Exception //т.к. калькулятор работает только с целыми числами")
    exit()
try:
    if not (1<=num1<=10 and 1<=num2<=10):
        raise ValueError("throws Exception")
except ValueError as e:
    print(e)
    exit()
if znak == "+":
    print(num1 + num2)
elif znak == "-":
    print(num1 - num2)
elif znak == "*":
    print(num1 * num2)
elif znak == "/":
    print(num1 // num2)
else:
    print("throws Exception //т.к. Неверная арифметичкеская операция")