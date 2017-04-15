import pyKriging
from pyKriging.krige import kriging
from pyKriging.samplingplan import samplingplan

def run_abaqus(design_variables_ND):
    input_file = 'design_variables.p'
    command_file = 'launch_cmd.bat'
    output_file = 'output.p'
    global outputs
    design_variables = {'g': 0.02 + (0.075-0.02)*design_variables_ND[0]}
    design_variables['k'] =  0.02 + (design_variables['g']-0.02)*design_variables_ND[1]
    design_variables['N'] = 100 + 900*design_variables_ND[2]
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

# The Kriging model starts by defining a sampling plan, we use an optimal Latin Hypercube here
# The input for sampling plan is the number of design variables
sp = samplingplan(3)
# The latin hypercube will use from 0 to 1, the number is the number of points to evaluate
X = sp.optimallhc(4)

# Next, we define the problem we would like to solve. The function has only one input which the vextor of designs
y = run_abaqus(X)

# Now that we have our initial data, we can create an instance of a Kriging model
k = kriging(X, y, testfunction=run_abaqus, name='simple')
k.train()

# Now, five infill points are added. Note that the model is re-trained after each point is added
numiter = 5
for i in range(numiter):
    print 'Infill iteration {0} of {1}....'.format(i + 1, numiter)
    newpoints = k.infill(1)
    for point in newpoints:
        k.addPoint(point, testfun(point)[0])
    k.train()

# And plot the results
k.plot()
