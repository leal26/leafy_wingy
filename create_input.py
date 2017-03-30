import pickle

input_file = 'design_variables.p'

design_variables = {'g': 0.0 ,
                    'k': 0.02,
                    'N': 100.}
print 0.02 + design_variables['g']*(design_variables['k']-0.02)
# Write input file
fileObject = open(input_file,'wb')
pickle.dump( design_variables, fileObject)
fileObject.close()
