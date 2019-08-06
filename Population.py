from ShakespeareMonkeys import Monkey
import random
from matplotlib import pyplot as plt


class Population:
    pop_size = 1500

    def __init__(self):
        self.current_population = [None for i in range(Population.pop_size)]
        self.new_population = []

    def initial_population(self):
        for i in range(Population.pop_size):
            monkey = Monkey('monkey{}'.format(i))
            self.current_population[i] = monkey

    def print_population(self):
        for monkey in self.current_population:
            print(monkey)

    def fittest_monkey(self):
        best = 0
        best_monkey = None
        for monkey in self.current_population:
            if monkey.fitness() > best:
                best = monkey.fitness()
                best_monkey = monkey
        return best_monkey

    def mating(self):
        fitness_array = []

        for monkey in self.current_population:
            fitness_array.append(monkey.fitness())

        total_sum = sum(fitness_array)

        for i in range(int(Population.pop_size/2)):
            cumulative_fitness = 0
            r_male = random.randrange(0, total_sum)
            r_female = random.randrange(0, total_sum)
            for j, number in enumerate(fitness_array):
                cumulative_fitness += number
                if cumulative_fitness > r_male:
                    male = self.current_population[j]
                    break
            cumulative_fitness = 0
            for j, number in enumerate(fitness_array):
                cumulative_fitness += number
                if cumulative_fitness > r_female:
                    female = self.current_population[j]
                    break

            for j in range(2):
                point_1 = random.randrange(0, len(Monkey.target_string))
                point_2 = random.randrange(0, len(Monkey.target_string))
                point_1 = min(point_1, point_2)
                point_2 = max(point_1, point_2)
                new_string = ''
                for j in range(3):
                    if j == 0:
                        start = 0
                        end = point_1
                    elif j == 1:
                        start = point_1
                        end = point_2
                    else:
                        start = point_2
                        end = len(Monkey.target_string)
                    gender = random.randrange(0,2)
                    if gender == 0:
                        new_string += male.string[start:end]
                    else:
                        new_string += female.string[start:end]
                self.new_population.append(Monkey('baby', new_string))

        for monkey in self.new_population:
            mutation_num = random.randrange(0, 2)
            for i in range(mutation_num):
                mutation_pos = random.randrange(0, len(monkey.target_string))
                monkey.string = monkey.string[0:mutation_pos] + Monkey.target_letters[random.randrange(0, len(Monkey.target_letters))] + monkey.string[mutation_pos+1:]

        self.current_population = self.new_population
        self.new_population = []


class Generation:

    def __init__(self, gen_number):
        self.gen_number = gen_number

    def run(self):
        population = Population()
        fitness_array = []
        best_ever = 0
        best_ever_monkey = None

        for i in range(self.gen_number):

            best_fitness = 0
            if i == 0:
                population.initial_population()
                monkeys = population.current_population
                for monkey in monkeys:
                    if monkey.fitness() > best_fitness:
                        best_fitness = monkey.fitness()
                        best_monkey = monkey
                    if monkey.fitness() > best_ever:
                        best_ever = monkey.fitness()
                        best_ever_monkey = monkey
                fitness_array.append(best_fitness)
            elif i > 0:
                population.mating()
                monkeys = population.current_population
                for monkey in monkeys:
                    if monkey.fitness() > best_fitness:
                        best_fitness = monkey.fitness()
                        best_monkey = monkey
                    if monkey.fitness() > best_ever:
                        best_ever = monkey.fitness()
                        best_ever_monkey = monkey
                fitness_array.append(best_fitness)
            if i%100 == 0:
                print(i, best_ever, best_ever_monkey.string, best_fitness, best_monkey.string)
            if best_ever == Monkey.best_fitness:
                print(i, best_ever, best_ever_monkey.string, best_fitness, best_monkey.string)
                break

        return fitness_array


gen = Generation(100000)
fitness_array = gen.run()
plt.plot(fitness_array)
plt.show()







#if __name__ == '__main__':
    #current_pop = Population()
    #current_pop.initial_population()
    #current_pop.mating()




