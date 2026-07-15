import math


HUMAN = "X"
AI = "O"
EMPTY = " "


def print_board(board):
    print()
    for row in range(3):
        print(f" {board[row][0]} | {board[row][1]} | {board[row][2]} ")
        if row < 2:
            print("---+---+---")
    print()


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)


def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 10 - depth

    if check_winner(board, HUMAN):
        return depth - 10

    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf

        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = AI
                    score = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY
                    best_score = max(best_score, score)

        return best_score

    best_score = math.inf

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = HUMAN
                score = minimax(board, depth + 1, True)
                board[row][col] = EMPTY
                best_score = min(best_score, score)

    return best_score


def get_best_move(board):
    best_score = -math.inf
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = AI
                score = minimax(board, 0, False)
                board[row][col] = EMPTY

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move


def human_move(board):
    while True:
        try:
            position = int(input("Enter your move (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

            row = (position - 1) // 3
            col = (position - 1) % 3

            if board[row][col] != EMPTY:
                print("That position is already occupied.")
                continue

            board[row][col] = HUMAN
            break

        except ValueError:
            print("Please enter a valid number.")


def display_positions():
    print("Position Guide")
    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()


def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]

    print("=" * 42)
    print("        TIC-TAC-TOE AI GAME")
    print("=" * 42)
    print(f"You are {HUMAN} and the AI is {AI}.")
    display_positions()

    while True:
        print_board(board)
        human_move(board)

        if check_winner(board, HUMAN):
            print_board(board)
            print("Congratulations! You won the game.")
            break

        if is_board_full(board):
            print_board(board)
            print("The game ended in a draw.")
            break

        print("AI is making its move...")

        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = AI

        if check_winner(board, AI):
            print_board(board)
            print("AI won the game. Better luck next time!")
            break

        if is_board_full(board):
            print_board(board)
            print("The game ended in a draw.")
            break


if __name__ == "__main__":
    play_game()
