import random

def print_board_3x3(board):
    """Поле 3x3"""
    print("\n    1 2 3")
    print(f"1 | {board[0]} {board[1]} {board[2]} |")
    print(f"2 | {board[3]} {board[4]} {board[5]} |")
    print(f"3 | {board[6]} {board[7]} {board[8]} |")

def print_board_4x4(board):
    #Поле 4x4
    print("\n    1 2 3 4")
    print(f"1 | {board[0]} {board[1]} {board[2]} {board[3]} |")
    print(f"2 | {board[4]} {board[5]} {board[6]} {board[7]} |")
    print(f"3 | {board[8]} {board[9]} {board[10]} {board[11]} |")
    print(f"4 | {board[12]} {board[13]} {board[14]} {board[15]} |")

def check_winner_3x3(board):
    #Проверка победителя для поля 3x3
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтали
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикали
        [0, 4, 8], [2, 4, 6]              # диагонали
    ]
    
    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != " ":
            return board[line[0]]
    return None

def check_winner_4x4(board):
    #Проверка победителя для поля 4x4
    lines = [
        # горизонтали
        [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15],
        # вертикали
        [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15],
        # диагонали
        [0, 5, 10, 15], [3, 6, 9, 12]
    ]
    
    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]] == board[line[3]] != " ":
            return board[line[0]]
    return None

def play_with_human():
    "Игра против человека"
    print("\n    Выберите размер поля:")
    print("    1. 3x3 (классические крестики-нолики)")
    print("    2. 4x4 (4 для победы нужно)")
    
    field_choice = input("    Вы выбираете: ")
    
    if field_choice == "1":
        play_3x3_with_human()
    elif field_choice == "2":
        play_4x4_with_human()
    else:
        print("    Такого варианта нету:(")

def play_3x3_with_human():
    #Игра 3x3 против человека
    board = [" "] * 9
    current_player = "X"
    
    print("\n    3x3 с человеком")
    print_board_3x3(board)
    
    while True:
        print(f"\n    Ходит игрок у которого символ {current_player}")
        
        while True:
            try:
                move = int(input("    Выберите клетку (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == " ":
                    board[move] = current_player
                    break
                else:
                    print("    Выберите клетку (1-9)")
            except ValueError:
                print("    Выберите клетку (1-9)")
        
        print_board_3x3(board)
        
        # Проверка победы
        winner = check_winner_3x3(board)
        if winner:
            print(f"    Игрок {winner} победждает")
            break
        
        # Проверка ничьи
        if " " not in board:
            print("     Ничья")
            break
        
        # Смена игрока
        current_player = "O" if current_player == "X" else "X"

def play_4x4_with_human():
    #Игра 4x4 против человека
    board = [" "] * 16
    current_player = "X"
    
    print("\n    4x4 с человеком")
    print("    Нужно собрать 4 в ряд")
    print_board_4x4(board)
    
    while True:
        print(f"\n    Ходит игрок {current_player}")
        
        while True:
            try:
                move = int(input("    Выберите клетку (1-16): ")) - 1
                if 0 <= move <= 15 and board[move] == " ":
                    board[move] = current_player
                    break
                else:
                    print("    Такого варианта нету:(")
            except ValueError:
                print("    Введите число от 1 до 16")
        
        print_board_4x4(board)
        
        # Проверка победы
        winner = check_winner_4x4(board)
        if winner:
            print(f"     Игрок {winner} забирает победу")
            break
        
        # Проверка ничьи
        if " " not in board:
            print("     Ничья")
            break
        
        # Смена игрока
        current_player = "O" if current_player == "X" else "X"

def play_with_bot(): 
    #Игра против бота 
    board = [" "] * 9
    current_player = "X"

    print("\n    Игра против бота")
    print("    Вы играете за X")
    print_board_3x3(board)
    
    while True:
        if current_player == "X":
            # Ход игрока
            while True:
                try:
                    move = int(input("    Выберите куда поставить крестик (1-9): ")) - 1
                    if 0 <= move <= 8 and board[move] == " ":
                        board[move] = "X"
                        break
                    else:
                        print("    Такого варианта нету:(")
                except ValueError:
                    print("    Введите число от 1 до 9")
        else:
            # Ход бота
            print("    Бот в размышлениях")
            move = bot_move(board)
            board[move] = "O"
            print(f"    Бот пошел на поле {move + 1}")

        print_board_3x3(board)

        # Проверяем победу со стороны игрока и бота
        winner = check_winner_3x3(board)
        if winner:
            if winner == "X":
                print("    Вам удалось победить искусственный интеллект. Однажды он вернется с реваншем")
            else:
                print("    Искусственный интеллект одержал победу. Думаю стоит попробовать еще раз и исход игры поменяется")
            break
        
        # Проверяем на наличие ничьи
        if " " not in board:
            print("    Клетки закончились, победителей нет. Может в следующий раз исход игры изменится")
            break 

        # Смена игрока
        current_player = "O" if current_player == "X" else "X"

def bot_move(board):
    #Ход бота для поля 3x3
    # Бот анализирует выигрышный ход
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner_3x3(board) == "O":
                board[i] = " "
                return i
            board[i] = " "

    # Блокировка победной комбинации игрока
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner_3x3(board) == "X":
                board[i] = " "
                return i
            board[i] = " "

    # Занимаем центр если свободен
    if board[4] == " ":
        return 4
    
    # Занимаем углы
    corners = [0, 2, 6, 8]
    empty_corners = [c for c in corners if board[c] == " "]
    if empty_corners:
        return random.choice(empty_corners)
    
    # Выбираем случайное место для хода
    empty_cells = [i for i in range(9) if board[i] == " "]
    return random.choice(empty_cells)

def main():
    while True:
        print()
        print("    Крестики-нолики")
        print("    1. Играть против робота")
        print("    2. Играть против человека") 
        print("    3. Выход")
        
        choice = input("    Выберите пункт меню: ")
        
        if choice == "1":
            print("    Вы выбрали опцию сыграть против робота")
            play_with_bot()
        elif choice == "2":
            print("    Вы выбрали опцию сыграть с человеком")
            play_with_human()
        elif choice == "3":
            print("    Выход из программы:(")
            break
        else:
            print("    Такого выбора нету(, а может в дальнейшем появятся")

if __name__ == "__main__":
    main()