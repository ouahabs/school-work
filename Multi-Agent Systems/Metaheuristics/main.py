from metaheuristics import GBO, DGO, RTBGO, TWO
from utils import SVM, fitness
from ludo import Player, LudoGame

if __name__ == "__main__":
    # Number of tokens
    NT = 32

    # Number of players
    NP = 4

    game = LudoGame(NT, NP)
    game.players[0] = GBO.GBO(NT/4, NT/8, fitness.rastrigin(SVM.SvmOptimizedProblem()))
    game.players[1] = DGO.DGO(NT, 2, fitness.ackley(SVM.SvmOptimizedProblem()))
    game.players[2] = RTBGO.RTBGO(NT, fitness.schwefel(SVM.SvmOptimizedProblem()))
    game.players[3] = TWO.TWO(NT, fitness.rosenbrock(SVM.SvmOptimizedProblem()))

    # Run the ludo game
    game.run()
    