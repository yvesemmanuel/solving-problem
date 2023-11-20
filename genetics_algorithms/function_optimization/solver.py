import numpy as np
import random
from statistics import mean

from functions import (
    Ackley,
    Rastrigin,
    Schwefel,
    Rosenbrock
)

class GA():

    def __init__(
        self,
        function: str,
        pop_size=100,
        chromosome_size=30,
        num_offspring=100,
        max_generations=1000,
        tournament_size=5,
        proba_crossover=0.9,
        proba_mutation=0.9,
        fitness_threshold=1e-4,
        patience=20,
        n_points=3,
        num_parents=2,
        crossover_type='single-point',
        parent_selection_type='TS',
        survivor_selection_type='Elitism',
        **kwargs
    ):
        self.set_function(function)
        self.set_crossover_type(crossover_type)
        self.pop_size = pop_size
        self.chromosome_size = chromosome_size
        self.max_generations = max_generations
        self.num_offspring = num_offspring
        self.tournament_size = tournament_size
        self.proba_crossover = proba_crossover
        self.proba_mutation = proba_mutation
        self.fitness_threshold = fitness_threshold
        self.n_points = n_points
        self.num_parents = num_parents
        self.parent_selection_type = parent_selection_type
        self.survivor_selection_type = survivor_selection_type
        
        self.wait_count = 0
        self.patience = patience

    def get_cost_type(self, cost_function_type):
        available_costs = [
            'function',
            'rmse'
        ]
        assert cost_function_type in available_costs,\
                f'Not a valid cost function type. Available to use: {available_costs}.'
        
        self.cost_function_type = cost_function_type

        if cost_function_type == 'function':
            cost_function = self.calculate_fitness
        elif cost_function_type == 'rmse':
            cost_function = self.calculate_solution_distance

        return cost_function


    def set_function(self, function):
        available_functions = [
            Ackley,
            Rastrigin,
            Schwefel,
            Rosenbrock
        ]
        func_names = [function.__name__ for function in available_functions]
        assert function in func_names,\
                f'Not a valid function. Available to use: {func_names}.'

        self.function = function

    def set_crossover_type(self, crossover_type):
        available_cross_overs = [
            'single-point',
            'n-points'
        ]
        assert crossover_type in available_cross_overs,\
                f'Not a valid cross-over type. Available to use: {available_cross_overs}.'

        self.crossover_type = crossover_type

    def generate_individual(self):
        if self.function == 'Ackley':
            individual = np.array([random.uniform(-32.768, 32.768)
                                   for _ in range(self.chromosome_size)])
        elif self.function == 'Rastrigin':
            individual = np.array([random.uniform(-5.12, 5.12)
                                   for _ in range(self.chromosome_size)])
        elif self.function == 'Schwefel':
            individual = np.array([random.uniform(-500, 500)
                                   for _ in range(self.chromosome_size)])
        elif self.function == 'Rosenbrock':
            individual = np.array([random.uniform(-5, 10)
                                   for _ in range(self.chromosome_size)])

        return individual.copy()
    
    def calculate_fitness(self, individual):
        if self.function == 'Ackley':
            term0 = -20 * \
                np.exp(-0.2*np.sqrt(np.sum(individual**2)) /
                       self.chromosome_size)
            term1 = np.exp(
                np.sum(np.cos(individual*2*np.pi)) / self.chromosome_size)
            fitness = term0 - term1 + 20 + np.exp(1)
        elif self.function == 'Rastrigin':
            fitness = 10*self.chromosome_size + \
                np.sum(individual**2 - 10*np.cos(individual*2*np.pi))
        elif self.function == 'Schwefel':
            fitness = 418.9829*self.chromosome_size - \
                np.sum(individual * np.sin(np.sqrt(np.abs(individual))))
        elif self.function == 'Rosenbrock':
            fitness = 0
            for i in range(self.chromosome_size - 1):
                fitness += 100 * \
                    (individual[i + 1] - individual[i]
                     ** 2)**2 + (individual[i] - 1)**2
                
        return fitness

    def generate_initial_population(self):
        return [self.generate_individual() for _ in range(self.pop_size)]
    
    def tournament_selection(self, items, k, cost_function):
        tournament_candidates = random.sample(items, self.tournament_size)
        winners = sorted(tournament_candidates, key=cost_function)[:k]
        return winners

    def rws_selection(self, items, k, cost_function):
        cost_values = map(cost_function, items)
        total_cost = sum(cost_values)
        probabilities = [cost / total_cost for cost in cost_values]
        
        winners = random.choices(items, probabilities, k=k)
        return winners
    
    def select_parents(self, population, cost_function):
        if self.parent_selection_type == 'TS':
            return self.tournament_selection(population, self.num_parents, cost_function)
        elif self.parent_selection_type == 'RWS':
            return self.rws_selection(population, self.num_parents, cost_function)

    def crossover_n_point(self, parent0, parent1):
        chromosome_size = len(parent0)
        crossover_points = sorted(random.sample(range(1, chromosome_size), self.n_points))
        child0, child1 = parent0.copy(), parent1.copy()
        
        for i in range(1, len(crossover_points), 2):
            start_point = crossover_points[i-1]
            end_point = crossover_points[i]
            child0[start_point:end_point], child1[start_point:end_point] = child1[start_point:end_point], child0[start_point:end_point]
        return child0, child1

    def crossover_single_point(self, parent0, parent1):
        if np.random.rand() < self.proba_crossover:
            crossover_point = random.randint(1, len(parent0) - 1)
            child0 = np.concatenate((parent0[:crossover_point], parent1[crossover_point:]))
            child1 = np.concatenate((parent1[:crossover_point], parent0[crossover_point:]))
            return child0, child1
        else:
            return parent0.copy(), parent1.copy()

    def crossover(self, parent0, parent1):
        if self.crossover_type == 'single-point':
            return self.crossover_single_point(parent0, parent1)
        elif self.crossover_type == 'n-points':
            return self.crossover_n_point(parent0, parent1)
        
    def get_normal_distribution(self, mu, sigma, k=1):
        return np.random.normal(mu, sigma, k)

    def mutate(self, individual):
        for i in range(self.chromosome_size):
            if random.random() < self.proba_mutation:
                mu, sigma = 0, 1 # mean, std
                if self.function == 'Ackley':
                    individual[i] = max(min(individual[i] * self.get_normal_distribution(mu, sigma), 32.768), -32.768)
                elif self.function == 'Rastrigin':
                    individual[i] = max(min(individual[i] * self.get_normal_distribution(mu, sigma), 5.12), -5.12)
                elif self.function == 'Schwefel':
                    individual[i] = max(min(individual[i] * self.get_normal_distribution(mu, sigma), 500), -500)
                elif self.function == 'Rosenbrock':
                    individual[i] = max(min(individual[i] * self.get_normal_distribution(mu, sigma), 10), -5)

        return individual
    
    def elitism_selection(self, items, k, cost_function, reverse=False):
        sorted_by_cost = sorted(items, key=cost_function, reverse=reverse)
        winners = sorted_by_cost[:k]

        return winners

    def select_suvivor(self, population, offspring, cost_function):
        new_pop = population + offspring

        if self.survivor_selection_type == 'TS':
            return self.tournament_selection(new_pop, self.pop_size, cost_function)
        elif self.survivor_selection_type == 'Elitism':
            return self.elitism_selection(new_pop, self.pop_size, cost_function)

    def get_population_mean_fitness(self, population, cost_function):
        return mean(list(map(cost_function, population)))
    
    def calculate_solution_distance(self, individual):
        if self.function in ['Ackley', 'Rastrigin']:
            function_minimum = np.array([0] * self.chromosome_size)
        elif self.function == 'Schwefel':
            function_minimum = np.array([420.9687] * self.chromosome_size)
        elif self.function == 'Rosenbrock':
            function_minimum = np.array([1] * self.chromosome_size)

        return self.calculate_rmse(individual, function_minimum)
    
    def calculate_rmse(self, array1, array2):
        squared_diff = (array1 - array2) ** 2
        mean_squared_error = np.mean(squared_diff)
        rmse = np.sqrt(mean_squared_error)
        return rmse
    
    def is_solution(self, best_fitness):
        decimal_places = len(str(self.fitness_threshold).split('.')[-1])
        rounded_best_fitness = round(best_fitness, decimal_places)

        return abs(rounded_best_fitness) <= self.fitness_threshold

    def optimize(self, cost_function_type='function', verbose=True, **kwargs):
        cost_function = self.get_cost_type(cost_function_type)

        population = self.generate_initial_population()

        best_individual = min(population, key=cost_function)
        best_fitness = cost_function(best_individual)

        generations = 0
        mean_fitness_per_generation = [
            self.get_population_mean_fitness(population, cost_function)
        ]
        best_fitness_per_generation = [best_fitness]

        is_timeout = (generations >= self.max_generations)
        is_zero = self.is_solution(best_fitness)
        while not is_timeout and not is_zero:

            offspring = []
            for _ in range(self.num_offspring // 2):
                parent0, parent1 = self.select_parents(population, cost_function)
                child0, child1 = self.crossover(parent0, parent1)
                child0, child1 = self.mutate(child0), self.mutate(child1)
                offspring.extend([child0, child1])

            population = self.select_suvivor(population, offspring, cost_function)

            curr_mean_fitness = self.get_population_mean_fitness(population, cost_function)

            best_individual = min(population, key=cost_function)
            best_fitness = cost_function(best_individual)

            if verbose:
                print(
                    f'Generation: {generations}, Best Fitness: {best_fitness},' \
                        f'Mutation Proba: {self.proba_mutation}, Population size: {len(population)}')

            # Updates for next generation
            is_timeout = (generations >= self.max_generations)
            generations += 1
            is_zero = self.is_solution(best_fitness)

            mean_fitness_per_generation.append(curr_mean_fitness)
            best_fitness_per_generation.append(best_fitness)

        best_individual = min(population, key=cost_function)
        best_fitness = cost_function(best_individual)

        if verbose:
            print('Optimization finished.')
            print(f'Best Individual: {best_individual}')
            print(f'Best Fitness: {best_fitness}')

        output_data = {
            'best_solution': best_individual,
            'best_fitness': best_fitness,
            'mean_fitness_per_generation': mean_fitness_per_generation,
            'best_fitness_per_generation': best_fitness_per_generation,
            'generations': generations,
            'solution_distance': self.calculate_solution_distance(best_individual)
        }

        return output_data


class ES():

    def __init__(
        self,
        function: str,
        pop_size=100,
        chromosome_size=30,
        num_offspring=100,
        max_generations=1000,
        tournament_size=5,
        proba_crossover=0.9,
        proba_mutation=0.9,
        fitness_threshold=1e-4,
        patience=20,
        n_points=3,
        num_parents=2,
        crossover_type='single-point',
        parent_selection_type='TS',
        survivor_selection_type='Elitism',
        learning_rate=0.42,
        sigma_threshold=0.2,
        **kwargs
    ):
        self.set_function(function)
        self.set_crossover_type(crossover_type)
        self.learning_rate = learning_rate
        self.pop_size = pop_size
        self.chromosome_size = chromosome_size
        self.max_generations = max_generations
        self.num_offspring = num_offspring
        self.tournament_size = tournament_size
        self.proba_crossover = proba_crossover
        self.proba_mutation = proba_mutation
        self.fitness_threshold = fitness_threshold
        self.n_points = n_points
        self.num_parents = num_parents
        self.parent_selection_type = parent_selection_type
        self.survivor_selection_type = survivor_selection_type
        self.sigma_threshold = sigma_threshold
        
        self.wait_count = 0
        self.patience = patience

    def get_cost_type(self, cost_function_type):
        available_costs = [
            'function',
            'rmse'
        ]
        assert cost_function_type in available_costs,\
                f'Not a valid cost function type. Available to use: {available_costs}.'
        
        self.cost_function_type = cost_function_type

        if cost_function_type == 'function':
            cost_function = self.calculate_fitness
        elif cost_function_type == 'rmse':
            cost_function = self.calculate_solution_distance

        return cost_function

    def set_function(self, function):
        available_functions = [
            Ackley,
            Rastrigin,
            Schwefel,
            Rosenbrock
        ]
        func_names = [function.__name__ for function in available_functions]
        assert function in func_names,\
                f'Not a valid function. Available to use: {func_names}.'

        self.function = function

    def set_crossover_type(self, crossover_type):
        available_cross_overs = [
            'single-point',
            'n-points'
        ]
        assert crossover_type in available_cross_overs,\
                f'Not a valid cross-over type. Available to use: {available_cross_overs}.'

        self.crossover_type = crossover_type

    def generate_individual(self):
        sigma = 20

        if self.function == 'Ackley':
            individual = np.array([random.uniform(-32.768, 32.768)
                                   for _ in range(self.chromosome_size)])
        elif self.function == 'Rastrigin':
            individual = np.array([random.uniform(-5.12, 5.12)
                                   for _ in range(self.chromosome_size)])
        elif self.function == 'Schwefel':
            individual = np.array([random.uniform(-500, 500)
                                   for _ in range(self.chromosome_size)])
        elif self.function == 'Rosenbrock':
            individual = np.array([random.uniform(-5, 10)
                                   for _ in range(self.chromosome_size)])

        return individual.copy(), sigma
    
    def calculate_fitness(self, individual):
        individual = individual[0]

        if self.function == 'Ackley':
            term0 = -20 * \
                np.exp(-0.2*np.sqrt(np.sum(individual**2)) /
                       self.chromosome_size)
            term1 = np.exp(
                np.sum(np.cos(individual*2*np.pi)) / self.chromosome_size)
            fitness = term0 - term1 + 20 + np.exp(1)
        elif self.function == 'Rastrigin':
            fitness = 10*self.chromosome_size + \
                np.sum(individual**2 - 10*np.cos(individual*2*np.pi))
        elif self.function == 'Schwefel':
            fitness = 418.9829*self.chromosome_size - \
                np.sum(individual * np.sin(np.sqrt(np.abs(individual))))
        elif self.function == 'Rosenbrock':
            fitness = 0
            for i in range(self.chromosome_size - 1):
                fitness += 100 * \
                    (individual[i + 1] - individual[i]
                     ** 2)**2 + (individual[i] - 1)**2
                
        return fitness

    def generate_initial_population(self):
        return [self.generate_individual() for _ in range(self.pop_size)]
    
    def tournament_selection(self, items, k, cost_function):
        tournament_candidates = random.sample(items, self.tournament_size)
        winners = sorted(tournament_candidates, key=cost_function)[:k]
        return winners

    def rws_selection(self, items, k, cost_function):
        cost_values = map(cost_function, items)
        total_cost = sum(cost_values)
        probabilities = [cost / total_cost for cost in cost_values]
        
        winners = random.choices(items, probabilities, k=k)
        return winners
    
    def select_parents(self, population, cost_function):
        if self.parent_selection_type == 'TS':
            return self.tournament_selection(population, self.num_parents, cost_function)
        elif self.parent_selection_type == 'RWS':
            return self.rws_selection(population, self.num_parents, cost_function)

    def crossover_n_point(self, parent0, parent1):
        parent0 = parent0[0].copy()
        sigma_0 = parent0[1]
        parent1 = parent1[0].copy()
        sigma_1 = parent1[1]

        chromosome_size = len(parent0)
        crossover_points = sorted(random.sample(range(1, chromosome_size), self.n_points))
        child0, child1 = parent0.copy(), parent1.copy()
        
        for i in range(1, len(crossover_points), 2):
            start_point = crossover_points[i-1]
            end_point = crossover_points[i]
            child0[start_point:end_point], child1[start_point:end_point] = child1[start_point:end_point], child0[start_point:end_point]
        return (child0, sigma_0), (child1, sigma_1)

    def crossover_single_point(self, parent0, parent1):
        if np.random.rand() < self.proba_crossover:
            parent0 = parent0[0].copy()
            sigma_0 = parent0[1]
            parent1 = parent1[0].copy()
            sigma_1 = parent1[1]
            crossover_point = random.randint(1, len(parent0) - 1)
            child0 = np.concatenate((parent0[:crossover_point], parent1[crossover_point:]))
            child1 = np.concatenate((parent1[:crossover_point], parent0[crossover_point:]))
            return (child0, sigma_0), (child1, sigma_1)
        else:
            return parent0, parent1

    def crossover(self, parent0, parent1):
        if self.crossover_type == 'single-point':
            return self.crossover_single_point(parent0, parent1)
        elif self.crossover_type == 'n-points':
            return self.crossover_n_point(parent0, parent1)
        
    def get_normal_distribution(self, mu, sigma, k=1):
        return np.random.normal(mu, sigma, k)

    def mutate(self, individual):
        individual = individual[0].copy()
        sigma = individual[1]

        for i in range(self.chromosome_size):
            if random.random() < self.proba_mutation:
                sigma = sigma * np.exp(self.learning_rate * np.random.normal(0, 1))

                if sigma <= self.sigma_threshold:
                    sigma = self.sigma_threshold

                # if self.function == 'Ackley':
                #     individual[i] = max(min(individual[i] * self.get_normal_distribution(mu, sigma), 32.768), -32.768)
                # elif self.function == 'Rastrigin':
                #     individual[i] = max(min(individual[i] * self.get_normal_distribution(mu, sigma), 5.12), -5.12)
                # elif self.function == 'Schwefel':
                #     individual[i] = max(min(individual[i] * self.get_normal_distribution(mu, sigma), 500), -500)
                # elif self.function == 'Rosenbrock':
                #     individual[i] = max(min(individual[i] * self.get_normal_distribution(mu, sigma), 10), -5)

                individual[i] = individual[i] + sigma * self.get_normal_distribution(0, 1)

        return individual, sigma
    
    def elitism_selection(self, items, k, cost_function, reverse=False):
        sorted_by_cost = sorted(items, key=cost_function, reverse=reverse)
        winners = sorted_by_cost[:k]

        return winners

    def select_suvivor(self, population, offspring, cost_function):
        new_pop = population + offspring

        if self.survivor_selection_type == 'TS':
            return self.tournament_selection(new_pop, self.pop_size, cost_function)
        elif self.survivor_selection_type == 'Elitism':
            return self.elitism_selection(new_pop, self.pop_size, cost_function)

    def get_population_mean_fitness(self, population, cost_function):
        return mean(list(map(cost_function, population)))
    
    def calculate_solution_distance(self, individual):
        individual = individual[0]
        if self.function in ['Ackley', 'Rastrigin']:
            function_minimum = np.array([0] * self.chromosome_size)
        elif self.function == 'Schwefel':
            function_minimum = np.array([420.9687] * self.chromosome_size)
        elif self.function == 'Rosenbrock':
            function_minimum = np.array([1] * self.chromosome_size)

        return self.calculate_rmse(individual, function_minimum)
    
    def calculate_rmse(self, array1, array2):
        squared_diff = (array1 - array2) ** 2
        mean_squared_error = np.mean(squared_diff)
        rmse = np.sqrt(mean_squared_error)
        return rmse
    
    def is_solution(self, best_fitness):
        decimal_places = len(str(self.fitness_threshold).split('.')[-1])
        rounded_best_fitness = round(best_fitness, decimal_places)

        return abs(rounded_best_fitness) <= self.fitness_threshold

    def optimize(self, cost_function_type='function', verbose=True, **kwargs):
        cost_function = self.get_cost_type(cost_function_type)

        population = self.generate_initial_population()

        best_individual = min(population, key=cost_function)
        best_fitness = cost_function(best_individual)

        generations = 0
        mean_fitness_per_generation = [
            self.get_population_mean_fitness(population, cost_function)
        ]
        best_fitness_per_generation = [best_fitness]

        is_timeout = (generations >= self.max_generations)
        is_zero = self.is_solution(best_fitness)
        while not is_timeout and not is_zero:

            offspring = []
            for _ in range(self.num_offspring // 2):
                parent0, parent1 = self.select_parents(population, cost_function)
                child0, child1 = self.crossover(parent0, parent1)
                child0, child1 = self.mutate(child0), self.mutate(child1)
                offspring.extend([child0, child1])

            population = self.select_suvivor(population, offspring, cost_function)

            curr_mean_fitness = self.get_population_mean_fitness(population, cost_function)

            best_individual = min(population, key=cost_function)
            best_fitness = cost_function(best_individual)

            if verbose:
                print(
                    f'Generation: {generations}, Best Fitness: {best_fitness},' \
                        f'Mutation Proba: {self.proba_mutation}, Population size: {len(population)}')

            # Updates for next generation
            is_timeout = (generations >= self.max_generations)
            generations += 1
            is_zero = self.is_solution(best_fitness)

            mean_fitness_per_generation.append(curr_mean_fitness)
            best_fitness_per_generation.append(best_fitness)

        best_individual = min(population, key=cost_function)
        best_fitness = cost_function(best_individual)

        if verbose:
            print('Optimization finished.')
            print(f'Best Individual: {best_individual}')
            print(f'Best Fitness: {best_fitness}')

        output_data = {
            'best_solution': best_individual,
            'best_fitness': best_fitness,
            'mean_fitness_per_generation': mean_fitness_per_generation,
            'best_fitness_per_generation': best_fitness_per_generation,
            'generations': generations,
            'solution_distance': self.calculate_solution_distance(best_individual)
        }

        return output_data