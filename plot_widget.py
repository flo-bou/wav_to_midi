import random

from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget
# from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvas, FigureCanvasQTAgg, NavigationToolbar2QT
import matplotlib.figure as fig
# import matplotlib.pyplot as plt

# main window
class PlotWidget(QWidget):

    def __init__(self):
        super().__init__()
        
        # self.figure = plt.figure() # a figure instance to plot on
        self.figure = fig.Figure(figsize=(50, 3))
        # self.figure.
        print(id(self.figure), "figure", self.figure)
        # print(id(self.figure2), "figure2", self.figure)
        
        self.canvas = FigureCanvasQTAgg(self.figure)
        # static_canvas = FigureCanvas(self.figure)
        print(id(self), "canvas sizeHint:", str(self.canvas.sizeHint()))
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        print(id(self), "toolbar sizeHint:", str(self.toolbar.sizeHint()))
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.button)

        self.setLayout(layout)
        print(id(self), "plot widget size:", str(self.size()))

    # action called by the push button
    def plot(self):
        data = [random.random() for i in range(100)] # random data
        self.figure.clear() # clearing old figure
        ax = self.figure.add_subplot(111)
        ax.plot(data, '*-')
        self.canvas.draw() # refresh canvas