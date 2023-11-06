import random

# 计算冲突数量的适应度函数
def fitness(board):
    conflicts = 0
    for i in range(len(board)):#i-row,board[i]-column
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                conflicts += 1
    return conflicts

# 初始化种群，每一个个体是一副棋盘
def initialize_population(pop_size, board_size): #board_size = 8
    population = []
    for _ in range(pop_size):
        individual = list(range(board_size))
        random.shuffle(individual)
        population.append(individual)
    return population

# 交叉操作，产生子代
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
    return child

# 变异操作
def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]

# 遗传算法主程序
def genetic_algorithm(pop_size, board_size, mutation_rate, max_generations):
    # 初始化种群
    population = initialize_population(pop_size, board_size)
    for generation in range(max_generations):
        # 对种群按适应度排序，找到最优个体
        population = sorted(population, key=lambda x: fitness(x))
        if fitness(population[0]) == 0:
            return population[0]  # 找到解决方案
        new_population = [population[0]]  # 精英主义：保留最优个体
        while len(new_population) < pop_size:
            # 从种群中选择两个父母
            parent1, parent2 = random.choices(population[:pop_size // 2], k=2)
            # 交叉操作
            child = crossover(parent1, parent2)
            # 变异操作
            mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    return None  # 未找到解决方案

if __name__ == "__main__":
    pop_size = 100
    board_size = 8
    mutation_rate = 0.1
    max_generations = 1000

    solution = genetic_algorithm(pop_size, board_size, mutation_rate, max_generations)

    if solution:
        print("Solution found:")
        print(solution)
    else:
        print("No solution found within the maximum number of generations.")
