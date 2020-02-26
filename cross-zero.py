

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