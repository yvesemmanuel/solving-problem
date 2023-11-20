
import random
from statistics import mean
from typing import List, Tuple
from encoders import BinaryEncoder

def calculate_clashes(chromosome: List[str]) -> int:
    clashes = 0
    size = len(chromosome)
    queen_clashes = {queen: [] for queen in range(size)}
    for i in range(size):
        for j in range(i + 1, size):
            diff = BinaryEncoder.binary_to_int(
                chromosome[i]) - BinaryEncoder.binary_to_int(chromosome[j])
            if chromosome[i] == chromosome[j] or diff == j - i or diff == i - j:
                queen_clashes[i].append(j)
                queen_clashes[j].append(i)
                clashes += 1

    return clashes, queen_clashes


def calculate_fitness(chromosome: List[str]) -> float:
    clashes, _ = calculate_clashes(chromosome)

    return 1 / (1 + clashes)


def get_mean_fitness(population: List[List[str]]) -> float:
    mean_fitness = mean(map(calculate_fitness, population))
    return mean_fitness


def generate_chromosome(size: int) -> List[str]:
    width = BinaryEncoder.minimum_bits(size - 1)
    permutations = [BinaryEncoder.int_to_binary(i, width) for i in range(size)]

    for _ in range(random.randint(0, 4)):
        random.shuffle(permutations)
    return permutations


def generate_initial_population(
    chromosome_size: int,
    population_size: int
) -> List[List[str]]:
    return [generate_chromosome(chromosome_size) for _ in range(population_size)]


def select_parents(population, tournament_size):
    if len(population) < tournament_size:
        return population

    candidates = random.sample(population, tournament_size)

    candidates.sort(key=lambda x: calculate_fitness(x), reverse=True)
    return candidates[:2]


def crossover(parent_0, parent_1, recombination_probability, cross_over_type):
    if cross_over_type == 'cut_n_crossfill':
        child_0, child_1 = cut_n_crossfill(parent_0, parent_1, recombination_probability)
        return child_0, child_1, None
    elif cross_over_type == 'heuristic_crossover':
        return heuristic_crossover(parent_0, parent_1, recombination_probability)


def heuristic_crossover(parent_0, parent_1, recombination_probability):
    num_clashes_0, _ = calculate_clashes(parent_0)
    num_clashes_1, _ = calculate_clashes(parent_1)

    child_0, child_1, _ = crossover(parent_0, parent_1, recombination_probability, 'cut_n_crossfill')
    child_fit_0 = calculate_fitness(child_0)
    child_fit_1 = calculate_fitness(child_1)

    if num_clashes_0 == 1 and num_clashes_1 == 1:
        return parent_0, parent_1, 'both'
    elif num_clashes_0 == 1 or num_clashes_1 == 1:
        if child_fit_0 > child_fit_1:
            best_child = child_0
        else:
            best_child = child_1

        if num_clashes_0 == 1:
            return parent_0, best_child, 'first'
        else:
            return parent_1, best_child, 'first'
    else:
        return child_0, child_1, None


def cut_n_crossfill(parent_0, parent_1, recombination_probability):
    if random.random() < recombination_probability:
        size = len(parent_0)
        cutting_point = random.randint(1, size - 1)

        child_0 = parent_0[:cutting_point]
        child_1 = parent_1[:cutting_point]

        index = 0
        while len(child_0) < size:
            curr_element = parent_1[index % len(parent_1)]

            if curr_element not in child_0:
                child_0.append(curr_element)

            index += 1

        index = 0
        while len(child_1) < size:
            curr_element = parent_0[index % len(parent_0)]

            if curr_element not in child_1:
                child_1.append(curr_element)

            index += 1

        return child_0, child_1
    else:
        return parent_0, parent_1


def mutate_heuristic(parent_0):
    _, queen_clashes = calculate_clashes(parent_0)
    queens_clashing = []
    for queen, clashes in queen_clashes.items():
        if len(clashes) > 0:
            queens_clashing.append(queen)
    
    clashed_queen_0 = random.sample(queens_clashing, 1)[0]
    clashed_queen_1 = list(set(queens_clashing) - {clashed_queen_0})[0]

    swap_queen = random.randint(0, len(parent_0) - 1)
    while clashed_queen_1 == swap_queen:
        swap_queen = random.randint(0, len(parent_0) - 1)

    parent_0[clashed_queen_0], parent_0[swap_queen] = \
        parent_0[swap_queen], parent_0[clashed_queen_0]

    return parent_0


def mutate(chromosome, mutation_proba):
    size = len(chromosome)
    for i in range(size):
        if random.random() < mutation_proba:
            j = random.randint(0, size - 1)
            while j == i:
                j = random.randint(0, size - 1)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

    return chromosome


def select_suvivors(
    population: List[List[str]],
    offspring: List[List[str]],
    population_size: int,
    seletion_type: str
) -> List[List[str]]:
    
    if seletion_type == 'generational':
        return offspring
    elif 'substitution':
        combined_population = population + offspring
        sorted_population = sorted(
            combined_population, key=calculate_fitness, reverse=True)
        return sorted_population[:population_size]


def experiment(
    chromosome_size: int,
    num_offspring: int,
    population_size: int,
    tournament_size: int,
    max_iterations: int,
    recombination_prob: float,
    mutation_prob: float,
    seletion_type: str,
    cross_over_type: str
) -> Tuple[List[List[str]], float, float, List[float], List[float], int]:

    population = generate_initial_population(
        chromosome_size, population_size)
    initial_mean_fit = get_mean_fitness(population)

    best_chromosome = max(population, key=calculate_fitness)
    best_fitness = calculate_fitness(best_chromosome)

    mean_fit_per_ite = [initial_mean_fit]
    best_fit_per_ite = [best_fitness]
    iterations = 1

    solution_found_on = 'initially_found'
    while iterations < max_iterations and best_fitness != 1:
        iterations += 1

        parents_0, parents_1 = select_parents(population, tournament_size)

        offspring = []
        for _ in range(num_offspring // 2):
            child_0, child_1, is_heuristic = crossover(
                parents_0, parents_1, recombination_prob, cross_over_type)
            
            is_solution = max(
                [calculate_fitness(child_0),
                calculate_fitness(child_1)]
            ) == 1

            if is_solution:
                solution_found_on = 'recombination'
            else:
                if is_heuristic == 'first':
                    child_0 = mutate_heuristic(child_0)
                    child_1 = mutate(child_1, mutation_prob)
                elif is_heuristic == 'both':
                    child_0 = mutate_heuristic(child_0)
                    child_1 = mutate_heuristic(child_1)
                else:
                    child_0 = mutate(child_0, mutation_prob)
                    child_1 = mutate(child_1, mutation_prob)

                is_solution = max(
                    [calculate_fitness(child_0),
                    calculate_fitness(child_1)]
                ) == 1

                if is_solution:
                    solution_found_on = 'mutate'

            offspring.extend([child_0, child_1])

        population = select_suvivors(population, offspring, population_size, seletion_type)

        mean_fitness = get_mean_fitness(population)
        mean_fit_per_ite.append(mean_fitness)

        best_chromosome = max(population, key=calculate_fitness)
        best_fitness = calculate_fitness(best_chromosome)

        best_fit_per_ite.append(best_fitness)

    if best_fitness < 1:
        solution_found_on = 'not_found'

    final_mean_fit = get_mean_fitness(population)

    return population, initial_mean_fit, final_mean_fit, mean_fit_per_ite, \
                        best_fit_per_ite, iterations, solution_found_on
