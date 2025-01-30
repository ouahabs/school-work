import numpy as np
from mealpy import Optimizer, FloatVar
import math


class GBO(Optimizer):
    """
    Golden Ball Optimizer, from:
    Eneko Osaba, Fernando Díaz, Enrique Onieva, 
    Golden Ball: A Novel Meta-Heuristic to Solve Combinatorial Optimization Problems Based on Soccer Concepts
    """

    def __init__(self, epoch=1000, m_solution=5, m_clusters=4, p1=0.75, **kwargs):
        super().__init__(**kwargs)
        self.epoch = self.validator.check_int("epoch", epoch, [1, 100000])
        self.m_solution = self.validator.check_int("m_solution", m_solution, [5, 10])
        self.m_clusters = self.validator.check_int("m_clusters", m_clusters, [2, 5])
        self.pop_size = self.m_solution * self.m_clusters
        self.p1 = self.validator.check_float("p1", p1, (0, 1.0))

        self.sort_flag = True
        # Determine to sort the problem or not in each epoch
        ## if True, the problem always sorted with fitness value increase
        ## if False, the problem is not sorted

    def initialize_variables(self):
        """
        This is method is called before initialization() method.
        """
        ## Support variables
        self.space = self.problem.ub - self.problem.lb

    def initialization(self):
        ### Required code
        if self.pop is None:
            self.pop = self.generate_population(self.pop_size)
        self.pop_group = self.generate_group_population(self.pop, self.m_clusters, self.m_solution)
        
        # self.pop = self.update_weight__(self.pop)

        ### Your additional code can be implemented here
        # self.mean_pos = np.mean([agent[self.ID_POS] for agent in self.pop])

    def evolve(self, epoch):
        """
        Loop through the population multiple times

        Args:
            epoch (int): The current iteration
        """
        epsilon = 1.0 - epoch / self.epoch      # The epsilon in each epoch is changing based on this equation
        # for season in range(2):
        #     for matchday in range(math.factorial(self.m_clusters)):
        #         for team in self.pop_group:
        #             for player in team:
        #                 pass
        #                 pos_new = player.solution + self.generator.normal(0, 1, self.problem.n_dims)
        #                 if pos_new == player.solution: # Receive Custom Training
        #                     captain = get_best_agent(team, self.problem.minmax)
        #                     player, _ = crossover_arithmetic(captain, player)
        #             team.mean_pos = np.mean(team)
                            


        # ## 1. Replace the almost worst agent by random agent
        # if self.generator.uniform() < self.p1:
        #     idx = self.generator.integers(self.n_agents, self.pop_size)
        #     self.pop[idx] = self.generate_agent()

        # ## 2. Replace all bad solutions by current_best + noise
        # for idx in range(self.n_agents, self.pop_size):
        #     pos_new = self.pop[0].solution + epsilon * self.space * self.generator.normal(0, 1)
        #     pos_new = self.correct_solution(pos_new)
        #     agent = self.generate_agent(pos_new)
        #     if self.compare_target(agent.target, self.pop[idx].target, self.problem.minmax):
        #         self.pop[idx] = agent

        # ## 3. Move all good solutions toward current best solution
        # for idx in range(0, self.n_agents):
        #     if idx == 0:
        #         pos_new = self.pop[idx].solution + epsilon * self.space * self.generator.uniform(0, 1)
        #     else:
        #         pos_new = self.pop[idx].solution + epsilon * self.space * (self.pop[0].solution - self.pop[idx].solution)
        #     pos_new = self.correct_solution(pos_new)
        #     agent = self.generate_agent(pos_new)
        #     if self.compare_target(agent.target, self.pop[idx].target, self.problem.minmax):
        #         self.pop[idx] = agent

        # ## Do additional works here if needed.



## Time to test our new optimizer
def objective_function(solution):
    return np.sum(solution**2)

problem_dict1 = {
    "obj_func": objective_function,
    "bounds": FloatVar(lb=[-100, ]*100, ub=[100, ]*100),
    "minmax": "min",
}

epoch = 2
players_per_team = 5
number_of_teams = 4
model = GBO(epoch, players_per_team, number_of_teams)
g_best = model.solve(problem_dict1)
print(f"Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")