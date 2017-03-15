from generate_module import generate_module
from venation_module import generate_venation
from aerodynamic_module import create_aerodynamic_step
from displacement_module import create_displacement_step

from materials import Materials, aluminum
from airfoil_module import CST, create_x
from xfoil_module import create_input

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PARAMETERS
# Wing parameters
span = .02
chord = 1.
velocity = 20.
aoa = 2.
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
aluminum_type = 'AL-2024-T3'
venation_type = 'AL-6061-T4'
aluminum_thickness = 0.002
aluminum_properties = aluminum(aluminum_type, aluminum_thickness)
SMA_thickness = 0.002
SMA_properties = Materials['TiNiCu-M+']
venation_properties = aluminum(aluminum_type, aluminum_thickness)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DESIGN VARIABLES
kill_distance = 0.075
growth_distance = 0.075
grid_size = 100

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CST module
airfoil_x = create_x(chord, n=100, distribution = 'polar')
airfoil_y = CST(airfoil_x, chord, deltaz, Au, Al)
create_input(airfoil_x, airfoil_y['u'], airfoil_y['l'], datafile)

# Venation Module
venation_data = generate_venation(kill_distance, growth_distance,
                                  grid_size, plot=True)
print 'Genarated Venation structure!'

# Generate module
generate_module(Au, Al, deltaz, spar_x_coordinate, chord, span,
                 aluminum_type, venation_type, aluminum_thickness,
                 aluminum_properties, SMA_thickness, SMA_properties,
                 venation_properties, x_u1, x_u2, x_l1, x_l2, datafile)
print 'Generated model!'

# Aerodynamic loading module
create_aerodynamic_step(airfoil_x, airfoil_y, velocity, altitude, aoa, chord,
                        span, Step1)
print 'Created aerodynamic step!'
# Displacement module
create_displacement_step(Step2, Step1, span, chord, deltaz, Au, Al,
                         spar_x_coordinate)
print 'Created displacement step!'

# Mesh it
p = mdb.models['Model-1'].parts['wing_structure']
p.seedPart(size=span, deviationFactor=0.1, minSizeFactor=0.1)
p.generateMesh()

# Check for lock files
if os.access('%s.lck'% JobName,os.F_OK):
    os.remove('%s.lck'% JobName)

# Create job and submit
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=4,
    numDomains=4, numGPUs=0)
BREAK
job.submit()
job.waitForCompletion()

TE_displacement = get_displacement(JobName + '.odb', StepName)
