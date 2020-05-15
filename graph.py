"""author:  Nathan Ormond                       """
"""License: MIT                                 """
"""Simple tool for plotting graphs using python """

# Required modules 
import numpy as np
import matplotlib.pyplot as plt 

#Test Code
#graph = Graph()
#graph.add_coordinate_series([1,2,3], [2,4,1])
#graph.set_x_label("x axis")
#graph.set_y_label("y axis")
#graph.set_title("Test Graph")

#Graph class, simply runs/draws graph
class Graph:
    def __init__(self):
        self.num_lines = 0
        self.x_series = []
        self.y_series = []
        self.xlabel = ""
        self.ylabel = ""
        self.title = ""

    def draw_graph(self):
        for index in self.num_lines:
            plt.plot(self.x_series.get(index), self.y_series.get(index))
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.show()

    def add_coordinate_series(self, x_series, y_series):
        self.x_series.append(x_series)
        self.y_series.append(y_series)
        self.num_lines += 1

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_x_series(self):
        return self.x_series

    def set_x_series(self, x_series):
        self.x_series = x_series

    def get_y_series(self):
        return self.y_series
    
    def set_y_series(self, y_series):
        self.y_series = y_series

    def get_X_label(self):
        return self.xlabel

    def set_X_label(self, xlabel):
        self.xlabel = xlabel

    def get_y_label(self):
        return self.ylabel

    def set_y_label(self, ylabel):
        self.ylabel = ylabel
        
######################################################### 

# Dunder
# Run code if compiled as python script from command line
# Otherwise import module.
#if __name__ == '__main__':
    #TODO
