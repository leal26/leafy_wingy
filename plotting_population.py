from xfoil_module import output_reader
from optimization_tools import plot_generations
import matplotlib.pyplot as plt
# Data = output_reader(filename = 'genetic_data.txt', header=['ng', 'g', 'k', 'N', 'delta'])

filename = 'genetic_data.txt'
plot_generations(filename, cost = None, g = None, p = None,
                     outputs_plotted = ['N', 'delta'], source = 'raw',
                     units = ['','m'], n_generation = 50,
                     color_scheme = 'individual', 
                     optimizers = ['NSGA2'], plot_type = 'all',
                     output_labels = ['Number of edges', 'Deflection'], label_size = None)


plt.show()