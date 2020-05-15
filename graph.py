"""author:  Nathan Ormond                       """
"""License: MIT                                 """
"""Simple tool for plotting graphs using python """

# Required modules 
import numpy as np
import matplotlib.pyplot as plt 

#GraphRenderer class, simply runs/draws graph
class GraphRenderer:
    def __init__(self):
        self.all_series = []

    def draw_graph(self, title, xlabel, ylabel):
        for series in self.all_series:
            #Format: plt.plot(x series, y series, colour e.g. 'b' , label='blue')
            print(series[2])
            plt.plot(series[0], series[1],label=series[2])
        plt.title(title)
        plt.xlabel(ylabel)
        plt.ylabel(xlabel)
        plt.legend()
        plt.show()

    def add_coordinate_series(self, x_series, y_series, label):
        self.all_series.append([x_series, y_series, label])


def engineer_cost_f():
    xarray = []
    yarray = []
    for x in range((52 * 1)):
        yarray.append(50 * 5.7 * x)
        xarray.append(x)
    return [xarray, yarray]

def api_call_cost_f(n):
    xarray = []
    yarray = []
    for x in range(52 * 1):
        yarray.append(0.01 * 12 * 24 * 7 * x * n)
        xarray.append(x)
    return  [xarray, yarray]

######################################################### 
# Run code if compiled as python script from command line
# Otherwise import module.
if __name__ == '__main__':
    graph = GraphRenderer()
    #Format: plt.plot(x series, y series, colour e.g. 'b' , label='blue')
    arr1 = engineer_cost_f()
    graph.add_coordinate_series(arr1[0], arr1[1], "engineer costs")

    arr2 = api_call_cost_f(1)
    graph.add_coordinate_series(arr2[0], arr2[1], "one ship API")

    arr3 = api_call_cost_f(15)
    graph.add_coordinate_series(arr3[0], arr3[1], "fifteen ships API")

    graph.draw_graph("Cost and Revenue Predictions", "revenue / £", "time / weeks")
