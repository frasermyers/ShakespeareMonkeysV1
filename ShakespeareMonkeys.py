import random


class Monkey:
    target_string = "The Complete Works of Shakespeare"
    target_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
    best_fitness = 66

    def __str__(self):
        return "This monkey's name is {} and has a fitness of {} out of a possible {}. This is its string: {}".format(self.name, self.fitness(), Monkey.best_fitness, self.string)

    def __init__(self, name, string=None):
        self.name = name
        if string is None:
            self.string = self.random_string()
        else:
            self.string = string

    def fitness(self):
        points = 0
        for i in range(len(Monkey.target_string)):
            if self.string[i] == Monkey.target_string[i]:
                points += 2
            elif self.string[i].upper() == Monkey.target_string[i].upper():
                points += 1
        return points

    @staticmethod
    def random_string():
        initial_string = ''
        for i in range(len(Monkey.target_string)):
            random_number = random.randrange(0, len(Monkey.target_letters))
            initial_string += Monkey.target_letters[random_number]
        return initial_string


if __name__ == '__main__':
    monkey1 = Monkey('monkey1')
    print(monkey1)
