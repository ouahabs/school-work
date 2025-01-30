import random
import numpy as np
from operator import attrgetter

class Player:
    def init(self, solution):
        self.solution = solution
        self.fitness = None

    def calculate_fitness(self, fitness_func):
        self.fitness = fitness_func(self.solution)

class Team:
    def init(self, players):
        self.players = players
        self.captain = max(self.players, key=attrgetter('fitness'))

class GBO:
    def init(self, NT, PT, fitness_func, crossover_func):
        self.NT = NT
        self.PT = PT
        self.fitness_func = fitness_func
        self.crossover_func = crossover_func
        self.teams = []

    def generate_population(self):
        for _ in range(self.NT):
            players = [Player(np.random.rand(10)) for _ in range(self.PT)]
            for player in players:
                player.calculate_fitness(self.fitness_func)
            self.teams.append(Team(players))

    def normal_training(self):
        for team in self.teams:
            for player in team.players:
                if player.fitness == team.captain.fitness:
                    player.solution = self.crossover_func(player.solution, team.captain.solution)
                    player.calculate_fitness(self.fitness_func)

    def custom_training(self):
        for team in self.teams:
            for player in team.players:
                if player.fitness == team.captain.fitness:
                    player.solution = self.crossover_func(player.solution, team.captain.solution)

    def match_day(self):
        for i in range(len(self.teams)):
            for j in range(i+1, len(self.teams)):
                team1 = self.teams[i]
                team2 = self.teams[j]
                team1.players.sort(key=attrgetter('fitness'), reverse=True)
                team2.players.sort(key=attrgetter('fitness'), reverse=True)
                for k in range(self.PT):
                    if team1.players[k].fitness > team2.players[k].fitness:
                        team1.captain = team1.players[k]
                    elif team2.players[k].fitness > team1.players[k].fitness:
                        team2.captain = team2.players[k]

    def transfer_period(self):
        self.teams.sort(key=lambda x: sum(player.fitness for player in x.players), reverse=True)
        for i in range(self.NT//2):
            self.teams[i], self.teams[-(i+1)] = self.teams[-(i+1)], self.teams[i]

    def run(self):
        self.generate_population()
        for _ in range(2):
            self.normal_training()
            self.custom_training()
            self.match_day()
            self.transfer_period()
        return [team.captain.solution for team in self.teams]