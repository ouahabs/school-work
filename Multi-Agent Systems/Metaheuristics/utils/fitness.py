import numpy as np

def rastrigin(solution):
    x, y, z = solution[0], solution[1], solution[2]
    return 20 + x**2 - 10*np.cos(2*np.pi*x) + y**2 - 10*np.cos(2*np.pi*y) + z**2 - 10*np.cos(2*np.pi*z)

def ackley(solution):
    x, y, z = solution[0], solution[1], solution[2]
    return -20*np.exp(-0.2*np.sqrt(0.5*(x**2 + y**2 + z**2))) - np.exp(0.5*(np.cos(2*np.pi*x) + np.cos(2*np.pi*y) + np.cos(2*np.pi*z))) + np.e + 20

def schwefel(solution):
    x, y, z = solution[0], solution[1], solution[2]
    return x**2 + y**2 + z**2

def rosenbrock(solution):
    x, y, z = solution[0], solution[1], solution[2]
    return 100*(y - x**2)**2 + (1 - x)**2 + 100*(z - y**2)**2 + (1 - y)**2
