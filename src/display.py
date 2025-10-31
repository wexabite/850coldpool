from matplotlib import pyplot as plt
import numpy as np

title = ""
xlabel = ""
ylabel = ""

def plot_line(data: [float], color = (1., 0., 0.), lw = .75):
    plt.plot(data, color=color, lw=lw)

def color_series(number: int):
    colors = [(0., 0., 0.)] * number
    for i in range(number):
        alpha = (number - i) / number
        colors[i] = (alpha, 0, 1 - alpha)
    return colors

def plot_series(series: [[float]], colors=None, lw=.75):
    l = len(series)
    if colors is None:
        colors = color_series(l)
    for i in range(l):
        plot_line(series[i], colors[i], lw)

    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

def plot_cmap(data_field: np.ndarray):
    plt.imshow(data_field)
    plt.show()

def set_title(text: str):
    global title
    title = text

def set_ylabel(text: str):
    global ylabel
    ylabel = text

def set_xlabel(text: str):
    global xlabel
    xlabel = text

def show():
    plt.show()