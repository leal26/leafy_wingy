import numpy as np
import subprocess as sp
import pickle
from scipy.optimize import minimize, minimize_scalar
import matplotlib.pyplot as plt

def run_abaqus(design_variables, V=30, alfa=8., chord=1.):
    input_file = 'design_variables.p'
    output_file = 'output.p'

    if V==30. and alfa==8. and chord==1.:
        command_file = 'launch_cmd.bat'
        design_variables = {'g': design_variables[0],
                            'k': 0.02 + (0.075-0.02)*design_variables[1],
                            'N': 100 + 900*design_variables[2]}
    else:
        command_file = 'launch_cmd_sensitivity.bat'
        design_variables = {'g': design_variables[0],
                            'k': 0.02 + (0.075-0.02)*design_variables[1],
                            'N': 100 + 900*design_variables[2],
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

    return abs(outputs['displacement'])

Data = []
optimum_x = [ 0.033663, (0.053503-0.02)/(0.075), 550.000000/(880.)]
for i in range(len(optimum_x)):
    perturbed_x_pos = optimum_x
    perturbed_x_neg = optimum_x
    perturbed_x_pos[i] = 1.05*perturbed_x_pos[i]
    perturbed_x_neg[i] =  .95*perturbed_x_neg[i]
    result_pos = run_abaqus(perturbed_x_pos)
    result_neg = run_abaqus(perturbed_x_neg)
    Data.append([result_neg, result_pos])

V = 30
V_neg = .95*V
V_pos = 1.05*V
result_pos = run_abaqus(optimum_x, V=V_pos)
result_neg = run_abaqus(optimum_x, V=V_neg)
Data.append([result_neg, result_pos])

alfa = 8.
alfa_neg = .95*alfa
alfa_pos = 1.05*alfa
result_pos = run_abaqus(optimum_x, alfa=alfa_pos)
result_neg = run_abaqus(optimum_x, alfa=alfa_pos)
Data.append([result_neg, result_pos])

c = 1.
c_neg = .95*c
c_pos = 1.05*c
result_pos = run_abaqus(optimum_x, chord=c_pos)
result_neg = run_abaqus(optimum_x, chord=c_neg)
Data.append([result_neg, result_pos])

# Write input file
fileObject = open('sensitivity_data.p','wb')
pickle.dump(Data, fileObject)
fileObject.close()

print Data
