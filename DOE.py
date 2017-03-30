import pickle
import subprocess as sp

from DOE_FullFactorial import DOE

def run_abaqus(design_variables):
    input_file = 'design_variables.p'
    command_file = 'launch_cmd.bat'
    output_file = 'output.p'

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


    file_txt = open('DOE_data.txt', 'a')

    file_txt.write('%10f \t %10f \t %10f \t %10f \t %10f \t %10f \n' % (design_variables['g'],
                                              design_variables['k'],
                                              design_variables['N'],
                                              outputs['displacement'],
                                              outputs['nodes'],
                                              outputs['stress']))
    file_txt.close()
    return outputs

file_txt = open('DOE_data.txt', 'w')
file_txt.close()
# Create DOE problem
problem = DOE(levels=4, driver='Full Factorial')
problem.add_variable('k', lower=0.02, upper=0.075, type=float)
problem.add_variable('g', lower=0.0, upper=1, type=float)
problem.add_variable('N', lower=100, upper=1000, type=int)
problem.define_points()

# Store DOE problem
problem.run(run_abaqus)
fileObject = open('DOE_FullFactorial.p','wb')
pickle.dump(problem, fileObject)
fileObject.close()
