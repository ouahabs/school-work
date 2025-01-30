import random
import numpy as np

class Dart:
    def init(self, value):
        self.value = value

class Player:
    def init(self, P):
        self.P = P
        self.darts = [Dart(random.randint(1, 20)) for _ in range(3)]


    # Two suggestions here, distance from center in millimeters
    # Or the value of points (non normalized, out of 180)
    def fitness(self):
        return sum(dart.value for dart in self.darts)

    def calculate_score(self, S):
        C = round(82 * (1 - self.P))
        score = 0
        for _ in range(C):
            if random.random() < self.P:
                score += random.choice(S)
        return score / 180

class DGO:
    def init(self, population_size, S):
        self.population = [Player(random.random()) for _ in range(population_size)]
        self.S = S

    def run(self):
        for player in self.population:
            player.darts = [Dart(random.randint(1, 20)) for _ in range(3)]

        self.population.sort(key=lambda x: x.fitness(), reverse=True)

        best_player = self.population[0]
        best_score = best_player.calculate_score(self.S)

        return best_player, best_score

# Create a DGO instance with a population size of 10 and a score matrix S
S = np.random.randint(1, 20, size=82)
S = np.sort(S)[::-1]  # Sort S from high to low
dgo = DGO(10, S)

# Run the DGO
best_player, best_score = dgo.run()

# Print the fitness and score of the best player
print(f"Best player fitness: {best_player.fitness()}")
print(f"Best player score: {best_score}")