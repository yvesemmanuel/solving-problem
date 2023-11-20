"""
Module that implements the functions to be optimized.

Reference: https://www.sfu.ca/~ssurjano/optimization.html
"""

import numpy as np
import matplotlib.pyplot as plt


class BaseFunction:
    def __init__(self) -> None:
        self.domain = None

    def compute(self, **args):
        raise NotImplementedError(
            'Subclasses must implement the compute method.')

    def compute_n_show(self):
        assert self.d == 2, "Only a 2D function can be plotted."

        x = np.linspace(self.domain[0], self.domain[1], 100)
        y = np.linspace(self.domain[0], self.domain[1], 100)
        X, Y = np.meshgrid(x, y)
        Z = self.compute(np.array([X, Y]))

        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Value')
        plt.title(self.__class__.__name__)
        plt.show()


class Ackley(BaseFunction):
    def __init__(self, d=2):
        self.d = d
        self.domain = [-32.768, 32.768]

    def compute(self, x):
        return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x[0]**2 + x[1]**2))) \
            - np.exp(0.5 * (np.cos(2 * np.pi *
                                   x[0]) + np.cos(2 * np.pi * x[1]))) + np.exp(1) + 20


class Rastrigin(BaseFunction):
    def __init__(self, d=2):
        self.d = d
        self.domain = [-5.12, 5.12]

    def compute(self, x):
        return 10 * 2 + (x[0]**2 - 10 * np.cos(2 * np.pi * x[0])) + (x[1]**2 - 10 * np.cos(2 * np.pi * x[1]))


class Schwefel(BaseFunction):
    def __init__(self, d=2):
        self.d = d
        self.domain = [-500, 500]

    def compute(self, x):
        return -x[0] * np.sin(np.sqrt(np.abs(x[0]))) - x[1] * np.sin(np.sqrt(np.abs(x[1])))


class Rosenbrock(BaseFunction):
    def __init__(self, d=2):
        self.d = d
        self.domain = [-5, 10]

    def compute(self, x):
        return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2
