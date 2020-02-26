field = []
field.append([])
field[0].append("  ")
for i in range(3):
    field[0].append(str(i))
    field[0].append(" ")
for i in range(1, 6):
    field.append([])
    if i % 2 == 1 :
        field[i].append(chr(ord("a") +(i // 2))+" ")
    else:
        field[i].append("  ")

    for ii in range(5):
        if i % 2 == 0:
            field[i].append("-")
        elif ii % 2 == 0:
            field[i].append(" ")
        else:
            field[i].append("|")


def game():
    while True:
        draw_field()
        if is_win(move("0")):
            print("zeros wins")
            break
        draw_field()
        if is_win(move("*")):
            print("crosses wins")
            break


def is_full_field():
    pass


def draw_field():
    for i in field:
        print("".join(i))


def move(who):
    def can_you_make_a_move(point):
        return field[point[0]][point[1]] == " "
    point = input("Введите точку")
    return


def is_win():
    pass

draw_field()