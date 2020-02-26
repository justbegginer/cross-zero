field = []
for i in range(5):
    field.append([])
    for ii in  range(5):
        if i%2==1:
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
    pass

def move(who):
    pass

def is_win():
    pass

game()