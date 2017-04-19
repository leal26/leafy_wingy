import numpy as np
import subprocess as sp
import pickle
from scipy.optimize import minimize, minimize_scalar
import matplotlib.pyplot as plt

def run_abaqus(design_variables):
    input_file = 'design_variables.p'
    command_file = 'launch_cmd.bat'
    output_file = 'output.p'
    global outputs
    design_variables = {'g': 10*design_variables[0],
                        'k': 0.02 + (0.075-0.02)*design_variables[1],
                        'N': 100 + 900*design_variables[2]}
    print design_variables
    # Write input file
    fileObject = open(input_file,'wb')
    pickle.dump( design_variables, fileObject)
    fileObject.close()

    # Run bat file
    ps = sp.Popen(command_file)
    ps.wait()

    # Read output file
    fileObject = open(output_file,'rb')
    outputs = pickle.load(fileObject)
    fileObject.close()


    file_txt = open('gradient_data.txt', 'a')

    file_txt.write('%10f \t %10f \t %10f \t %10f \t %10f \t %10f \n' % (0.02 + (design_variables['k']-.02)*design_variables['g'],
                                              design_variables['k'],
                                              design_variables['N'],
                                              abs(outputs['displacement']),
                                              outputs['nodes'],
                                              outputs['stress']))
    file_txt.close()
    return abs(outputs['displacement'])

def run_reporter(p):
    """Reporter function to capture intermediate states of optimization."""
    global data
    data.append(abs(outputs['displacement']))

def run_cons(x):
    global outputs
    return 30e6 - outputs['stress']
file_txt = open('gradient_data.txt', 'w')
file_txt.close()

data = []
x0 = [.1*0.033663, (0.053503-0.02)/(0.075), 550.000000/(880.)]

low_bound = [0, 0, 0]
high_bound = [.1, 1, 1]

global outputs
outputs = {'stress':0}
bounds = zip(low_bound, high_bound)
cons = ({'type': 'ineq',
         'fun': run_cons})
result = minimize(run_abaqus, x0, bounds = bounds,
                  constraints = cons, callback=run_reporter,
                  options = {'eps': 1.e-2})

print result.x
print result.fun

x = range(1, len(data)+1)
plt.plot(x, data)
plt.scatter(x, data)
plt.ylabel('displacement')
plt.xlabel('Iteration')
plt.grid()
plt.show()
