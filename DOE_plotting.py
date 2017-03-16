from optimization_tools import plot_generations

import matplotlib.pyplot as plt

fileObject = open('DOE_FullFactorial','wb')
original_problem = pickle.load(fileObject)
fileObject.close()

problem = DOE(levels=5, driver='Full Factorial')
problem.load(original_problem)

problem.plot()
plt.show()
