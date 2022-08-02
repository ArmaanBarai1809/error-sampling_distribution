import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import random

csv = pd.read_csv("data.csv")
data = csv["average"].to_list()
dataset = []

for i in range(0, 100):
    random_number = random.randint(0, len(data))
    value = data[random_number]
    dataset.append(value)
    # data.append(random_number(100))

mean = statistics.mean(dataset)
standard_deviation = statistics.stdev(dataset)

print(mean)
print(standard_deviation)

def random_mean(counter):

    dataset = []

    for i in range(0, counter):
        random_number = random.randint(0, len(data))
        value = data[random_number]
        dataset.append(value)

    mean = statistics.mean(dataset)

    return mean

def show_graph(mean_list):

    var = mean_list
    graph = ff.create_distplot(var, ['Average'], show_hist=False)
    graph.show()

def main():

    mean_list = []

    for i in range(0, 1000):
        mean_list.append(random_mean(100))
    
    show_graph(mean_list)

    sampling_mean = statistics.mean(mean_list)
    print(sampling_mean)

main()

population_mean = statistics.mean(data)

print(population_mean)

def standard_deviation():
    
    mean_list = []

    for i in range(0, 1000):
        mean_list.append(random_mean(100))

    std = statistics.stdev(mean_list)
    print(std)

standard_deviation()