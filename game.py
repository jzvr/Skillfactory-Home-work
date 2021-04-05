field_ = [[" "] * 3 for i in range(3)]
n = 0


def print_():  # Field visualization
    print("  0 1 2")
    for i, raw in enumerate(field_, start=0):
        line_ = str(i) + " " + " ".join(raw)
        print(line_)


def input_():  # User input
    while True:
        a = input("Ваш ход (введите две координаты через пробел): ").split()
        if len(a) != 2:
            print("Введите 2 координаты!")
            continue
        x, y = a
        if not x.isdigit() or not y.isdigit():
            print("Введите число!")
            continue
        x, y = int(x), int(y)
        if (0 <= x <= 2) and (0 <= y <= 2):
            if field_[x][y] == " ":
                return x, y
            else:
                print("Клетка занята!")
                print_()
        else:
            print("Координаты вне поля!")
            print_()


def vin():  # Winner combinations check

    for i in range(3):  # Raws checking
        symbols_ = []
        for j in range(3):
            symbols_.append(field_[i][j])
        if symbols_ == ["X", "X", "X"]:
            print("Победил Крестик!")
            return True
        elif symbols_ == ["0", "0", "0"]:
            print("Победил Нолик!")
            return True
    for i in range(3):  # Columns  checking
        symbols_ = []
        for j in range(3):
            symbols_.append(field_[j][i])
        if symbols_ == ["X", "X", "X"]:
            print("Победил Крестик!")
            return True
        elif symbols_ == ["0", "0", "0"]:
            print("Победил Нолик!")
            return True
    symbols_ = []
    for i in range(3):  # Diagonals checking
        symbols_.append(field_[i][2 - i])
        if symbols_ == ["X", "X", "X"]:
            print("Победил Крестик!")
            return True
        elif symbols_ == ["0", "0", "0"]:
            print("Победил Нолик!")
            return True
    symbols_ = []
    for i in range(3):  # Diagonals checking
        symbols_.append(field_[i][i])
        if symbols_ == ["X", "X", "X"]:
            print("Победил Крестик!")
            return True
        elif symbols_ == ["0", "0", "0"]:
            print("Победил Нолик!")
            return True


while True:  # Program body
    n += 1
    if n % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')
    x, y = input_()
    if n % 2 == 1:
        field_[x][y] = "X"
    else:
        field_[x][y] = "0"
    print_()
    vin_check = vin()
    if vin_check:
        break
    if n == 9:
        print("Ничья")
        break

