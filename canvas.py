import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np


class Canvas(FigureCanvas):
    def __init__(self, parent):

        fig, self.ax = plt.subplots()
        super().__init__(fig)
        self.setParent(parent)


    def plotting(self):

        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)

        self.ax.plot(t, s)

        self.ax.set(xlabel='time (s)', ylabel='voltage (mV)',
                    title='About as simple as it gets, folks')
        self.ax.grid()

    def plotting1(self):
        s = np.arange(0.0, 2.0, 0.01)
        t = 1 + np.sin(2 * np.pi * s)

        self.ax.plot(t, s)

        self.ax.set(xlabel='time (s)', ylabel='voltage (mV)',
                    title='About as simple as it gets, folks')
        self.ax.grid()

    def destroyer(self):
        self.ax.clear()
        self.plotting1()
