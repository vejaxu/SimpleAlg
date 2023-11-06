import random
import math

def fitness(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                conflicts += 1
    return conflicts

def neighbor(board):
    # 随机交换两个皇后的位置
    new_board = board.copy()
    i, j = random.sample(range(len(board)), 2)
    new_board[i], new_board[j] = new_board[j], new_board[i]
    return new_board

def acceptance_probability(current_energy, new_energy, temperature):
    # 计算接受概率
    if new_energy < current_energy:
        return 1.0
    return math.exp((current_energy - new_energy) / temperature)

def simulated_annealing(board, initial_temperature, cooling_rate, max_iterations):
    current_energy = fitness(board)
    best_solution = board.copy()

    for iteration in range(max_iterations):
        temperature = initial_temperature * (1.0 - iteration / max_iterations)
        if current_energy == 0:
            return best_solution  # 找到解决方案

        new_board = neighbor(board)
        new_energy = fitness(new_board)

        if acceptance_probability(current_energy, new_energy, temperature) > random.random():
            board = new_board
            current_energy = new_energy

            if new_energy < current_energy:
                best_solution = new_board

    return best_solution

if __name__ == "__main__":
    board_size = 8
    initial_temperature = 1000.0
    cooling_rate = 0.95
    max_iterations = 1000

    initial_board = list(range(board_size))
    random.shuffle(initial_board)

    solution = simulated_annealing(initial_board, initial_temperature, cooling_rate, max_iterations)

    if solution:
        print("Solution found:")
        print(solution)
    else:
        print("No solution found within the maximum number of iterations.")
