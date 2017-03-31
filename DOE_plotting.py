from optimization_tools import plot_generations
from DOE_FullFactorial import DOE

import pickle

fileObject = open('DOE_FullFactorial.p','r')
original_problem = pickle.load(fileObject)
fileObject.close()

problem = DOE(levels=4, driver='Full Factorial')
# problem.load(original_problem, filetype = 'object')
problem.load('DOE_data.txt' , variables_names = ['g', 'k', 'N'],
         outputs_names = ['displacement', 'nodes', 'stress'],
         header = ['g', 'k', 'N', 'displacement', 'nodes', 'stress'], filetype = 'file')

problem.find_influences()
problem.something = 0

print problem.something
print problem.output_names
print problem.variables_names
print problem.influences
print problem.levels
print 'n_var: ', problem.n_var

convert_to_MPa = lambda x: x/1e6
convert_to_abs = lambda x: abs(x)
problem.plot(xlabel = ['$d_k$', '$d_g$', '$N$'],
             ylabel = ['TE displacement (m)', 'N edges', 'Max stress (Mpa)'],
             process = {'stress':convert_to_MPa, 'displacement':convert_to_abs})
