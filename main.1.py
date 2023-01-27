try:
    print("Ноль в качестве знака операции"
          "\nзавершит работу программы")
    while True:
        s = input("Знак (+,-,*,/): ")
        if s == '0':
            break
        if s in ('+', '-', '*', '/'):
            x = float(input("x="))
            y = float(input("y="))
            c = float(input("c="))
            if s == '+':
                print("%.2f" % (x + y + c))
            elif s == '-':
                print("%.2f" % (x - y - c))
            elif s == '*':
                print("%.2f" % (x * y * c))
            elif s == '/':
                if y != 0:
                    print("%.2f" % (x / y / c))
                else:
                    print("Деление на ноль!")
        else:
            print("Неверный знак операции!")
except Exception as ex:
            print(f'Error [{ex.__class__.__name__}]: {ex}')