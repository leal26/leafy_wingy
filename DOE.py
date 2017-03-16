import pickle

from DOE_FullFactorial import DOE
from main_script import run

# Create DOE problem
problem = DOE(levels=5, driver='Full Factorial')
problem.add_variable('k', lower=0.04, upper=0.2, type=float)
problem.add_variable('g', lower=-0.4, upper=0.1, type=float)
problem.add_variable('N', lower=-0.4, upper=0.1, type=int)
problem.define_points()

# Store DOE problem
problem.run(run)
fileObject = open('DOE_FullFactorial','wb')
pickle.dump(problem, fileObject)
fileObject.close()
