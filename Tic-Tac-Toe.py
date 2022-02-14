# Board will be created by using a dictionary
# top left of board will take position '1' with position numbers increasing left to right
board = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
board_keys = []
for key in board:
    board_keys.append(key)


def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


# print_board(board)

# functionality for gameplay
def game():
    turn = 'X'
    counter = 0

    for i in range(9):
        print_board(board)
        print('It\'s your turn,' + turn + '. Where would you like to move?')

        move = input()
        valid_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        if move not in valid_moves:
            print("Not a valid input, please enter a number from 1 to 9!")

        else:
            if board[move] == ' ':
                board[move] = turn
                counter += 1
                turn = switch_turn(turn)
            else:
                print('That position is already taken. Please choose another.')

            if counter >= 5:
                if board['1'] == board['2'] == board['3'] != ' ':  # across the top
                    print_board(board)
                    print("\nGame Over.\n")
                    print(" **** " + switch_turn(turn) + " won. ****")
                    break
                elif board['4'] == board['5'] == board['6'] != ' ':  # across the middle
                    print_board(board)
                    print("\nGame Over.\n")
                    print(" **** " + switch_turn(turn) + " won. ****")
                    break
                elif board['7'] == board['8'] == board['9'] != ' ':  # across the bottom
                    print_board(board)
                    print("\nGame Over.\n")
                    print(" **** " + switch_turn(turn) + " won. ****")
                    break
                elif board['1'] == board['4'] == board['7'] != ' ':  # down the left side
                    print_board(board)
                    print("\nGame Over.\n")
                    print(" **** " + switch_turn(turn) + " won. ****")
                    break
                elif board['2'] == board['5'] == board['8'] != ' ':  # down the middle
                    print_board(board)
                    print("\nGame Over.\n")
                    print(" **** " + switch_turn(turn) + " won. ****")
                    break
                elif board['3'] == board['6'] == board['9'] != ' ':  # down the right side
                    print_board(board)
                    print("\nGame Over.\n")
                    print(" **** " + switch_turn(turn) + " won. ****")
                    break
                elif board['7'] == board['5'] == board['3'] != ' ':  # diagonal
                    print_board(board)
                    print("\nGame Over.\n")
                    print(" **** " + switch_turn(turn) + " won. ****")
                    break
                elif board['1'] == board['5'] == board['9'] != ' ':  # diagonal
                    print_board(board)
                    print("\nGame Over.\n")
                    print(" **** " + switch_turn(turn) + " won. ****")
                    break

            if counter == 9:
                print("It's a tie! Play again?")

    # if turn == 'X':
    #  turn = 'O'
    # else:
    # turn = 'X'

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            board[key] = " "

        game()


def switch_turn(turn):
    next_turn = 'X'
    if turn == 'X':
        next_turn = 'O'
    else:
        next_turn = 'X'
    return next_turn


game()
