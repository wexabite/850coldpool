from matplotlib import pyplot as plt
import numpy as np


def plot_line(data: [float], color = (1., 0., 0.)):
    plt.plot(data, color=color)

def color_series(number: int):
    colors = [(0., 0., 0.)] * number
    for i in range(number):
        alpha = (number - i) / number
        colors[i] = (alpha, 0, 1 - alpha)
    return colors

def plot_series(series: [[float]]):
    l = len(series)
    colors = color_series(l)
    for i in range(l):
        plot_line(series[i], colors[i])
    plt.show()
