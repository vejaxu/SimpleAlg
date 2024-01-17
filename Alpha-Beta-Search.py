def print_board(board):
    for row in board:
        print(" ".join(row))

def evaluate(board):
    # 检查每一行
    for row in board:
        if row.count('X') == 3:
            return 1
        elif row.count('O') == 3:
            return -1

    # 检查每一列
    for col in range(3):
        if [board[row][col] for row in range(3)].count('X') == 3:
            return 1
        elif [board[row][col] for row in range(3)].count('O') == 3:
            return -1

    # 检查对角线
    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
        return 1
    if board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        return -1

    return 0

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def max_min_alpha_beta(board, depth, is_max, alpha, beta):
    result = evaluate(board)

    if result == 1:
        return 1
    if result == -1:
        return -1
    if is_full(board):
        return 0

    if is_max:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, max_min_alpha_beta(board, depth + 1, not is_max, alpha, beta))
                    board[i][j] = ' ' #回溯算法
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, max_min_alpha_beta(board, depth + 1, not is_max, alpha, beta))
                    board[i][j] = ' '
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_move = None
    best_val = -float('inf')
    alpha = -float('inf')
    beta = float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = max_min_alpha_beta(board, 0, False, alpha, beta)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

if __name__ == "__main__":
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player_row, player_col = map(int, input("Enter your move (row and column, e.g., 0 1): ").split())
        if board[player_row][player_col] != ' ':
            print("Invalid move. Try again.")
            continue

        board[player_row][player_col] = 'O'
        print_board(board)

        if evaluate(board) == -1:
            print("You win!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        print("Computer's turn:")
        computer_move = find_best_move(board)
        if computer_move:
            board[computer_move[0]][computer_move[1]] = 'X'
            print_board(board)

        if evaluate(board) == 1:
            print("Computer wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break
