# TIC TAC TOE
import time
import random
import sys

User_Name = ""
Friend_Name = ""
Edition = ""
football_clubs = ['AC Milan         ',' Arsenal         ','Atletico Madrid  ','Barcelona FC     ',
                  'Bayern Munich    ','Chelsea FC       ','Borussia Dortmond','Tottenham Hotsupr',
                  'Inter Milan      ','Juventus         ','Real Madrid      ','Liverpool FC     ',
                  'Manchester City  ','Manchester United','PariSaint German ','Rome AC          '
                  ]

football_Data=[' South America  ',' North America  ',' Saudi League   ',
               '     Asia       ','     manager    ','    WorldCup    ',
               'Champions League','  Copa America  ','    AFCON       ',
               '     EURO       ','     SALAH      ','    Africa      ',
               '     ICON       ','     CR7        ','    Messi       ',
               '     Belgium    ','     Arab       ',' Saudi League   ',
               '     La liga    ',' Premier League ','    Seria A     '
               ]



def start_game():
    global User_Name, Friend_Name, Edition

    print("")
    print("Welcome to the Tic Tac Toe Game")
    print("Please enter your Name")
    User_Name = input('Your Name: ')
    if User_Name=='':
        User_Name='Player One'
    print('Enter your Friend Name')
    Friend_Name = input('Friend\'s Name: ')
    if Friend_Name=='':
        Friend_Name='Player Two'
    print('Do you wanna play it With Football Edition')
    while True:
        try:
            Football=input('Yes Or No: ')
            if Football.lower()=='yes':
                Edition= 'Football'
                print('30 sec Time for Each Turn')
                print('Starting Game')
                time.sleep(1)
                footbal_game()
                break
            elif Football.lower()=='no':
                Edition= 'Standard'
                print('Starting Game')
                time.sleep(1)
                play_game()
                break
            else:
                print('Invalid Entry Please Enter Yes or No')
        except ValueError:
            print("Invalid Entry")
    return Edition,User_Name,Friend_Name


def the_board(board):
    for row in board:
        print(*row)

def Check_Winner(board,player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_winner_football(board, symbol):
    for row in range(1, 4):
        if all(cell == symbol for cell in board[row][1:]):
            return True

    for col in range(1, 4):
        if all(board[row][col] == symbol for row in range(1, 4)):
            return True

    if all(board[i][i] == symbol for i in range(1, 4)) or all(board[i][4 - i] == symbol for i in range(1, 4)):
        return True

    return False

def check_tie_football(used_numbers):
    tie_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return all(number in used_numbers for number in tie_list)



def check_Tie(board):
    if all(isinstance(cell, str) for row in board for cell in row):
        return True
    return False

def play_again():
    while True:
        try:
            print('Do you want to Play again')
            choice = input("Yes or No: ")
            if choice.lower() == "yes":
                print('Starting new game...')
                time.sleep(1)
                return True
            elif choice.lower() == "no":
                print('Exiting game...')
                time.sleep(5)
                sys.exit()
                return False
        except ValueError:
            print("Please enter yes or no")

def play_game():
    global User_Name,Friend_Name

    board = [[3 * row + col + 1 for col in range(3)] for row in range(3)]

    player=[User_Name,Friend_Name]
    Symboll=['X','o']

    current_player = 0

    while True:
        the_board(board)
        print(f"{player[current_player]}'s turn. Enter a Number in The Board (or exit to end game)")

        try:
            number=(input())
            if number.lower()=='exit':
                print('Exiting....')
                time.sleep(5)
                break
            else:
                pass
            time.sleep(0.25)
            print(f'{player[current_player]} Chose {number}')

            if 1 <= int(number) <= 9 and board[(int(number) - 1) // 3][(int(number) - 1) % 3] == int(number):
                board[(int(number) - 1) // 3][(int(number) - 1) % 3] = Symboll[current_player]


                if Check_Winner(board,Symboll[current_player]):
                    the_board(board)
                    print(f"Congratulations! {player[current_player]} You are the Winner! ")
                    if play_again():
                        play_game()
                elif check_Tie(board):
                    the_board(board)
                    print('The Game is Tie')
                    if play_again():
                        play_game()
                else:
                    current_player = (current_player + 1) % 2
            else:
                print('Invalid input.')

        except ValueError:
            print("Invalid Entry. Please enter a valid number.")

def footbal_game():
    global football_clubs
    global football_Data
    Used_numbers=[]

    random_club_1 = random.choice(football_clubs)
    football_clubs.remove(random_club_1)
    random_club_2 = random.choice(football_clubs)
    football_clubs.remove(random_club_2)
    random_club_3 = random.choice(football_clubs)
    football_clubs.remove(random_club_3)

    random_data_1 = random.choice(football_Data)
    football_Data.remove(random_data_1)
    random_data_2 = random.choice(football_Data)
    football_Data.remove(random_data_2)
    random_data_3 = random.choice(football_Data)
    football_Data.remove(random_data_3)



    player = [User_Name, Friend_Name]
    Symboll = ['      X       ', '      O       ']

    current_player = 0

    board = [['                ',f' {random_club_1}|',f' {random_club_2}|',f" {random_club_3}"],
             [f'{random_data_1} : ','      1       ','      2       ','        3       '],
             [f'{random_data_2} : ','      4       ','      5       ','        6       '],
             [f'{random_data_3} : ','      7       ','      8       ','        9       ']
             ]

    while True:
        the_board(board)
        print(f"{player[current_player]}'s turn. Enter a Number in The Board (Or exit to end game)")

        start_time = time.time()


        try:
            number = input()
            if number.lower() == 'exit':
                print('Exiting...')
                time.sleep(5)
                break
            else:
                pass
            Used_numbers.append(int(number))

            elapsed_time = time.time() - start_time
            time.sleep(0.25)
            if elapsed_time <= 30:

                print(f'<<< {player[current_player]} chose {number} >>>')

                if int(number)==1 and board[1][1] =='      1       ':
                    board[1][1] = Symboll[current_player]

                    if check_winner_football(board, Symboll[current_player]):
                        the_board(board)
                        print(f"Congratulations! {player[current_player]} You are the Winner! ")
                        if play_again():
                            footbal_game()
                    elif check_tie_football(Used_numbers):
                        the_board(board)
                        print('The Game is Tie')
                        if play_again():
                            footbal_game()
                    else:
                        current_player = (current_player + 1) % 2

                elif int(number)==2 and board[1][2] == '      2       ':
                    board[1][2] = Symboll[current_player]

                    if check_winner_football(board, Symboll[current_player]):
                        the_board(board)
                        print(f"Congratulations! <{player[current_player]}> You are the Winner! ")
                        if play_again():
                            footbal_game()
                    elif check_tie_football(Used_numbers):
                        the_board(board)
                        print('The Game is Tie')
                        if play_again():
                            footbal_game()
                    else:
                        current_player = (current_player + 1) % 2

                elif int(number)==3 and board[1][3] == '        3       ':
                    board[1][3] = Symboll[current_player]

                    if check_winner_football(board, Symboll[current_player]):
                        the_board(board)
                        print(f"Congratulations! <{player[current_player]}> You are the Winner! ")
                        if play_again():
                            footbal_game()
                    elif check_tie_football(Used_numbers):
                        the_board(board)
                        print('The Game is Tie')
                        if play_again():
                            footbal_game()
                    else:
                        current_player = (current_player + 1) % 2

                elif int(number)==4 and board[2][1] == '      4       ':
                    board[2][1] = Symboll[current_player]

                    if check_winner_football(board, Symboll[current_player]):
                        the_board(board)
                        print(f"Congratulations! <{player[current_player]}> You are the Winner! ")
                        if play_again():
                            footbal_game()
                    elif check_tie_football(Used_numbers):
                        the_board(board)
                        print('The Game is Tie')
                        if play_again():
                            footbal_game()
                    else:
                        current_player = (current_player + 1) % 2

                elif int(number)==5 and board[2][2] == '      5       ':
                    board[2][2] = Symboll[current_player]

                    if check_winner_football(board, Symboll[current_player]):
                        the_board(board)
                        print(f"Congratulations! <{player[current_player]}> You are the Winner! ")
                        if play_again():
                            footbal_game()
                    elif check_tie_football(Used_numbers):
                        the_board(board)
                        print('The Game is Tie')
                        if play_again():
                            footbal_game()
                    else:
                        current_player = (current_player + 1) % 2

                elif int(number)==6 and board[2][3] == '        6       ':
                    board[2][3] = Symboll[current_player]

                    if check_winner_football(board, Symboll[current_player]):
                        the_board(board)
                        print(f"Congratulations! <{player[current_player]}> You are the Winner! ")
                        if play_again():
                            footbal_game()
                    elif check_tie_football(Used_numbers):
                        the_board(board)
                        print('The Game is Tie')
                        if play_again():
                            footbal_game()
                    else:
                        current_player = (current_player + 1) % 2

                elif int(number)==7 and board[3][1] == '      7       ':
                    board[3][1] = Symboll[current_player]

                    if check_winner_football(board, Symboll[current_player]):
                        the_board(board)
                        print(f"Congratulations! <{player[current_player]}> You are the Winner! ")
                        if play_again():
                            footbal_game()
                    elif check_tie_football(Used_numbers):
                        the_board(board)
                        print('The Game is Tie')
                        if play_again():
                            footbal_game()
                    else:
                        current_player = (current_player + 1) % 2

                elif int(number)==8 and board[3][2] == '      8       ':
                    board[3][2] = Symboll[current_player]

                    if check_winner_football(board, Symboll[current_player]):
                        the_board(board)
                        print(f"Congratulations! <{player[current_player]}> You are the Winner! ")
                        if play_again():
                            footbal_game()
                    elif check_tie_football(Used_numbers):
                        the_board(board)
                        print('The Game is Tie')
                        if play_again():
                            footbal_game()

                    else:
                        current_player = (current_player + 1) % 2

                elif int(number)==9 and board[3][3] == '        9       ':
                    board[3][3] = Symboll[current_player]

                    if check_winner_football(board, Symboll[current_player]):
                        the_board(board)
                        print(f"Congratulations! <{player[current_player]}> You are the Winner! ")
                        if play_again():
                            footbal_game()
                    elif check_tie_football(Used_numbers):
                        the_board(board)
                        print('The Game is Tie')
                        if play_again():
                            footbal_game()
                    else:
                        current_player = (current_player + 1) % 2

                else:
                    print('Invalid input.')

            else:
                print('Time Out')
                current_player = (current_player + 1) % 2

        except ValueError:
            print("Invalid Entry. Please enter a valid number.")

start_game()