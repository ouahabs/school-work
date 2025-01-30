import random
import numpy as np

class Player:
    def init(self, fitness_function):
        self.strategies = [random.randint(1, 10) for _ in range(10)]
        self.fitness_function = fitness_function

    def fitness(self):
        return self.fitness_function(self.strategies)

class RTBGO:
    def init(self, population_size, fitness_function, num_rings=10, num_bars=10, max_iterations=1000):
        self.population = [Player(fitness_function) for _ in range(population_size)]
        self.num_rings = num_rings
        self.num_bars = num_bars
        self.max_iterations = max_iterations

    def run(self):
        for i in range(self.max_iterations):
            self.population.sort(key=lambda x: x.fitness(), reverse=True)
            top_10_percent = self.population[:int(0.1 * len(self.population))]

            score_bars = [player.fitness() for player in top_10_percent]

            for player in self.population:
                for _ in range(self.num_rings):
                    bar = random.choice(score_bars)
                    if player.fitness() >= bar:
                        player.strategies = [random.randint(1, 10) for _ in range(10)]

        self.population.sort(key=lambda x: x.fitness(), reverse=True)
        return self.population[0]

# Create a fitness function
# Distace between nearest score bar and ring (agent)
def fitness_function(strategies):
    return sum(strategies)

# Create an RTBGO instance with a population size of 100
rtbgo = RTBGO(100, fitness_function)

# Run the RTBGO
best_player = rtbgo.run()

# Print the fitness of the best player
print(f"Best player fitness: {best_player.fitness()}")