from generate_module import generate_module
from venation_module import generate_venation
from aerodynamic_module import create_aerodynamic_step
from displacement_module import create_displacement_step

from materials import Materials, aluminum
from airfoil_module import CST, create_x
from xfoil_module import create_input
from abaqus_tools import get_displacement, find_maxMises

import pickle

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DESIGN VARIABLES

fileObject = open('design_variables.p','rb')
design_variables = pickle.load(fileObject)
fileObject.close()

kill_distance = design_variables['k']
relative_growth_distance = design_variables['g']
growth_distance = 0.02 + relative_growth_distance*(kill_distance - 0.02)
grid_size = design_variables['N']
print 'deisgn variable: ', kill_distance, growth_distance, grid_size
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PARAMETERS
# Wing parameters
span = .002
chord = design_variables['c']
velocity = design_variables['V']
aoa = design_variables['alfa']
altitude = 10000.
spar_x_coordinate = [150.E-03, 292.5E-03]

# CST parameters
Au = [0.1805, 0.1622]
Al = [0.1184, -0.0959]
deltaz = [0.002, 0.002]
datafile = 'airfoil.txt'

# Actuator positioning
x_u1 = [.1,.3,.5,.7]
x_u2 = [.12,.35,.6,.8]
x_l1 = [.1,.3,.5,.7]
x_l2 = [.12,.35,.6,.8]

# Abaqus parameters
JobName = 'Analysis'
ModelName = 'wing_structure'
Step1 = 'Aerodynamic loading'
Step2 = 'Morphing displacement'

# Material parameters
structure_thickness = 0.001
structure_properties = Materials['ABS']['Average']
SMA_thickness = 0.001


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CST module
airfoil_x = create_x(chord, n=100, distribution = 'polar')
airfoil_y = CST(airfoil_x, chord, deltaz, Au, Al)
create_input(airfoil_x, airfoil_y['u'], airfoil_y['l'], datafile)

# Venation Module
venation_data = {'x1':[1], 'x2':[1,2]} # Random value to get into loop
while len(venation_data['x1']) != len(venation_data['x2']):
	venation_data = generate_venation(kill_distance, growth_distance,
									  grid_size, plot=True)
print 'Genarated Venation structure!'

Mdb()
# Generate module
generate_module(Au, Al, deltaz, spar_x_coordinate, chord, span,
				structure_thickness, structure_properties, SMA_thickness,
				x_u1, x_u2, x_l1, x_l2, datafile)
print 'Generated model!'

# Aerodynamic loading module
create_aerodynamic_step(airfoil_x, airfoil_y, velocity, altitude, aoa, chord,
						span, Step1)
print 'Created aerodynamic step!'
# # Displacement module
# create_displacement_step(Step2, Step1, span, chord, deltaz, Au, Al,
						 # spar_x_coordinate)
# print 'Created displacement step!'

# Mesh it
p = mdb.models['Model-1'].parts['wing_structure']
p.seedPart(size=0.002, deviationFactor=0.1, minSizeFactor=0.1)
p.generateMesh()

# Check for lock files
if os.access('%s.lck'% JobName,os.F_OK):
	os.remove('%s.lck'% JobName)

# Create job and submit
job = mdb.Job(name=JobName, model='Model-1', description='', type=ANALYSIS,
	atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
	memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
	explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
	modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
	scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=4,
	numDomains=4, numGPUs=0)

mdb.saveAs(
	pathName='C:/Users/leal26/Documents/GitHub/leafy_wingy/wing_model.cae')
try:
    job.submit()
    job.waitForCompletion()
except:
    print 'Abaqus odb file had an error'
# Getting data out of it
TE_displacement = get_displacement(JobName + '.odb', Step1)
print 'Trailing Edge displacement: ', TE_displacement
print 'Number of nodes: ', TE_displacement
max_stress = find_maxMises(JobName, Step1)
# max_stress_OML = find_maxMises(JobName, Step2, 'Set-OML'.upper())
# max_stress = max(max_stress_OML, max_stress_venation)
# print 'Max stress: ', max_stress

fileObject = open('output.p','wb')
pickle.dump( {'displacement' : TE_displacement,
              'nodes':len(venation_data['x1']),
              'stress' : max_stress}, fileObject)
fileObject.close()
