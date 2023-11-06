import random

#评估函数，相互攻击的皇后对数
def evaluate(board):
    conflicts = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1

    return conflicts

def hill_climbing(n, max_iterations):
    current_board = list(range(n))
    random.shuffle(current_board)
    current_cost = evaluate(current_board)

    for _ in range(max_iterations):
        for i in range(n):
            for j in range(n):
                if i != j:
                    new_board = current_board.copy()
                    new_board[i], new_board[j] = new_board[j], new_board[i]
                    new_cost = evaluate(new_board)

                    if new_cost < current_cost:
                        current_board = new_board
                        current_cost = new_cost

        if current_cost == 0:
            return current_board  # Found a solution

    return None  # No solution found within max_iterations

#随机重启爬山法
def random_restart_hill_climbing(n, max_restarts, max_iterations):
    for _ in range(max_restarts):
        solution = hill_climbing(n, max_iterations)
        if solution is not None:
            return solution  # Found a solution

    return None  # No solution found within max_restarts

def print_solution(board):
    n = len(board)
    for row in range(n):
        line = ["Q" if i == board[row] else "." for i in range(n)]
        print(" ".join(line))

if __name__ == "__main__":
    n = 8  # 8皇后问题
    max_restarts =100
    max_iterations = 1000  # 最大迭代次数

    #solution = hill_climbing(n, max_iterations)
    solution = random_restart_hill_climbing(n, max_restarts, max_iterations)
    if solution is not None:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found within the specified number of iterations.")
