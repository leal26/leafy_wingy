import numpy as np
import subprocess as sp
import pickle
from scipy.optimize import minimize, minimize_scalar
import matplotlib.pyplot as plt
import numdifftools as nd
import math
def run_abaqus(design_variables, V=30, alfa=8., chord=1.):
    input_file = 'design_variables.p'
    output_file = 'output.p'

    if V==30. and alfa==8. and chord==1.:
        command_file = 'launch_cmd.bat'
        design_variables = {'g': 10*design_variables[0],
                            'k': 0.02 + (0.075-0.02)*10*design_variables[1],
                            'N': math.floor(100 + 900*100*design_variables[2])}
    else:
        command_file = 'launch_cmd_sensitivity.bat'
        design_variables = {'g': design_variables[0],
                            'k': 0.02 + (0.075-0.02)*design_variables[1],
                            'N': math.floor(100 + 900*design_variables[2]),
                            'V': V,
                            'alfa': alfa,
                            'c':chord}
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

    # Storing it to txt file just to check
    # Read output file
    growth_distance = 0.02 + design_variables['g']*(design_variables['k'] - 0.02)
    fileObject = open('hessian_data.txt','ab')
    fileObject.write('%.5f\t %.5f\t %.5f\t %.5f\t %.5f\n' % (design_variables['g'], growth_distance, design_variables['k'], design_variables['N'], abs(outputs['displacement'])))
    fileObject.close()
    return abs(outputs['displacement'])


fileObject = open('hessian_data.txt','wb')
fileObject.close()
# 0.79229	 0.04223	 0.04806	 813.0000
optimum_x = [ .1*0.79229, .1*(0.04806 -0.02)/(0.075-0.02), .01*(813-100.)/900.]
hessian_function = nd.Hessian(run_abaqus, step=1e-3)
data = hessian_function(optimum_x)

# Write input file
fileObject = open('hessian_data.p','wb')
pickle.dump(data, fileObject)
fileObject.close()

print data
