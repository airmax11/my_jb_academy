
enter_cell = list('_________')

def schema():
    print("---------")
    print("| " + enter_cell[0] + " " + enter_cell[1] + " " + enter_cell[2] + " |")
    print("| " + enter_cell[3] + " " + enter_cell[4] + " " + enter_cell[5] + " |")
    print("| " + enter_cell[6] + " " + enter_cell[7] + " " + enter_cell[8] + " |")
    print("---------")
schema()

def check_status():
    global start
    if ((enter_cell[0] == 'X' and enter_cell[1] == 'X' and enter_cell[2] == 'X' ) or
        (enter_cell[3] == 'X' and enter_cell[4] == 'X' and enter_cell[5] == 'X') or
        (enter_cell[6] == 'X' and enter_cell[7] == 'X' and enter_cell[8] == 'X') or
        (enter_cell[0] == 'X' and enter_cell[3] == 'X' and enter_cell[6] == 'X') or
        (enter_cell[1] == 'X' and enter_cell[4] == 'X' and enter_cell[7] == 'X') or
        (enter_cell[2] == 'X' and enter_cell[5] == 'X' and enter_cell[8] == 'X') or
        (enter_cell[0] == 'X' and enter_cell[4] == 'X' and enter_cell[8] == 'X') or
        (enter_cell[6] == 'X' and enter_cell[4] == 'X' and enter_cell[2] == 'X')):
        print("X wins")
        return "X wins"

    elif ((enter_cell[0] == 'O' and enter_cell[1] == 'O' and enter_cell[2] == 'O' ) or
        (enter_cell[3] == 'O' and enter_cell[4] == 'O' and enter_cell[5] == 'O') or
        (enter_cell[6] == 'O' and enter_cell[7] == 'O' and enter_cell[8] == 'O') or
        (enter_cell[0] == 'O' and enter_cell[3] == 'O' and enter_cell[6] == 'O') or
        (enter_cell[1] == 'O' and enter_cell[4] == 'O' and enter_cell[7] == 'O') or
        (enter_cell[2] == 'O' and enter_cell[5] == 'O' and enter_cell[8] == 'O') or
        (enter_cell[0] == 'O' and enter_cell[4] == 'O' and enter_cell[8] == 'O') or
        (enter_cell[6] == 'O' and enter_cell[4] == 'O' and enter_cell[2] == 'O')):
        print("O wins")
        return "O wins"


maps = [['1', '3'], ['2', '3'], ['3', '3'],
        ['1', '2'], ['2', '2'], ['3', '2'],
        ['1', '1'], ['2', '1'], ['3', '1']]


def user_input_check():
    coordinates = None
    while coordinates is None:
        enter_coordinates = input("Enter coordinates: ").split()
        if enter_coordinates in maps:
            if enter_cell[maps.index(enter_coordinates)] == '_':
                coordinates = maps.index(enter_coordinates)
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            for i in enter_coordinates:
                if not i.isnumeric():
                    print("You should enter numbers!")
                    break
                elif i not in ('1', '2', '3'):
                    print("Coordinates should be from 1 to 3!")
                    break

    return coordinates



# while start not in ["X wins", "O wins", "Draw", "Game not finished", "Impossible"]:
while True:
    if "_" in enter_cell:
        enter_cell[user_input_check()] = 'X'
        schema()
        if check_status() == 'X wins':
            break

    if "_" in enter_cell:
        enter_cell[user_input_check()] = 'O'
        schema()
        if check_status() == 'O wins':
            break

    if "_" not in enter_cell:
        print("Draw")
        break
