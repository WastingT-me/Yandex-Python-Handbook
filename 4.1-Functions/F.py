s = 0


def move(player, number):
    global s
    if player == 'Петя':
        s += number
    else:
        s -= number


def game_over():
    global s
    if s == 0:
        return 'Ничья'
    elif s < 0:
        return 'Ваня'
    else:
        return 'Петя'