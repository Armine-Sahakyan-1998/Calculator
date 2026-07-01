def number():
    while True:
        try:
            number = float(input('number: '))
            return number
        except ValueError:
            print('write only number')

def choice():
    ch = ('+', '-', '/', '*')
    c = input("'+', '-', '/', '*'")
    try:
        if c not in ch:
            raise Exception
    except:
        print("only",ch)
    return c

def result():
    x = number()
    c = choice()
    y = number()
    if c == '+':
        res = x + y
        return f"{x} + {y} = {res}"
    elif c == '-':
        res = x - y
        return f"{x} - {y} = {res}"
    elif c == '*':
        res = x * y
        return f"{x} * {y} = {res}"
    elif c == '/':
        while True:
            try:
                res = x / y
                return f"{x} / {y} = {res}"
            except ZeroDivisionError:
                print("Cannot divide by zero: ")
                y = number()
                
                





        
