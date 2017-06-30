from xfoil_module import output_reader
from optimization_tools import plot_generations
import matplotlib.pyplot as plt
# Data = output_reader(filename = 'genetic_data.txt', header=['ng', 'g', 'k', 'N', 'delta'])

data = 'multi'

if data == 'single':
	filename = 'genetic_data.txt'
	plot_generations(filename, cost = None, g = None, p = None,
						 outputs_plotted = ['N', 'delta'], source = 'raw',
						 units = ['','m'], n_generation = 50,
						 color_scheme = 'individual', 
						 optimizers = ['NSGA2'], plot_type = 'all',
						 output_labels = ['Number of edges', 'Deflection'], label_size = None)


	plt.show()
	
elif data == 'multi':
	filename = 'genetic_multi_data.txt'
	plot_generations(filename, cost = None, g = None, p = None,
						 outputs_plotted = ['N', 'delta'], source = 'raw',
						 units = ['','m'], n_generation = 27,
						 color_scheme = 'individual',  last_best = False,
						 optimizers = ['NSGA2'], plot_type = 'all',
						 output_labels = ['Number of edges', 'Deflection'], label_size = None,
						 pareto = True)
	plt.show()
	plot_generations(filename, cost = None, g = None, p = None,
						 outputs_plotted = ['k', 'delta'], source = 'raw',
						 units = ['m','m'], n_generation = 27,
						 color_scheme = 'individual',  last_best = False,
						 optimizers = ['NSGA2'], plot_type = 'all',
						 output_labels = ['Kill distance', 'Deflection'], label_size = None)
	plt.show()
	
	plot_generations(filename, cost = None, g = None, p = None,
						 outputs_plotted = ['g', 'delta'], source = 'raw',
						 units = ['m','m'], n_generation = 27,
						 color_scheme = 'individual',  last_best = False,
						 optimizers = ['NSGA2'], plot_type = 'all',
						 output_labels = ['Growth distance', 'Deflection'], label_size = None)
	plt.show()
	
	plot_generations(filename, cost = None, g = None, p = None,
						 outputs_plotted = ['Ng', 'delta'], source = 'raw',
						 units = ['','m'], n_generation = 27,
						 color_scheme = 'individual',  last_best = False,
						 optimizers = ['NSGA2'], plot_type = 'all',
						 output_labels = ['Grid size', 'Deflection'], label_size = None)
	plt.show()