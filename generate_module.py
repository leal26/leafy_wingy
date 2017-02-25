# My libraries
from xfoil_module import output_reader
from materials import Materials, aluminum
from venation_module import generate_venation
from structure_generation import *
from airfoil_module import CST, create_x
from xfoil_module import create_input

# Python libraries
import numpy as np

# Abaqus libraries
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

# Pre-processing
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Model parameters
span = .1
chord = 1.
datafile = 'airfoil.txt'
aluminum_type = 'AL-2024-T3'
aluminum_thickness = 0.002
aluminum_properties = aluminum(aluminum_type, aluminum_thickness)

# CST parameters:
Au = [0.1805, 0.1622]
Al = [0.1184, -0.0959]
deltaz = [0.002, 0.002]
x = create_x(chord, n = 100, distribution = 'polar')
y = CST(x, chord, deltaz, Au, Al)
create_input(x, y['u'], y['l'], datafile)

SMA_thickness = 0.002
positive_SMA_properties = Materials['TiNiCu-M+']
negative_SMA_properties = Materials['TiNiCu-M-']

material_properties = [aluminum_properties, negative_SMA_properties, positive_SMA_properties]
material_names = ['AL-2024', 'SMA-', 'SMA+']
material_thicknesses = [aluminum_thickness, SMA_thickness, SMA_thickness]

# Abaqus
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extracting data
wing_data = output_reader(datafile, header=['x','y'])
wing_data['z'] = [0 for i in range(len(wing_data['x']))]

header = ['element', 'x1', 'y1', 'x2', 'y2']
structure = [['element'], ['x1', 'y1'], ['x2', 'y2']]
venation_data = output_reader('edges.txt', header = header, structure = structure)

venation_data['x'] = list((np.array(venation_data['x1']) +
                           np.array(venation_data['x2']))/2)
venation_data['y'] = list((np.array(venation_data['y1']) +
                           np.array(venation_data['y2']))/2)
venation_data['z'] = [0 for i in range(len(venation_data['x']))]

wing_venation_generator(wing_data, venation_data, span)

# Create material properties
for i in range(len(material_properties)):
    YoungModulus = material_properties[i]['YoungModulus']
    Poisson = material_properties[i]['PoissonRatio']
    Density = material_properties[i]['Density']
    thickness = material_thicknesses[i]

    mdb.models['Model-1'].Material(name=material_names[i])
    mdb.models['Model-1'].materials[material_names[i]].Elastic(table=((YoungModulus, Poisson), ))
    mdb.models['Model-1'].materials[material_names[i]].Density(table=((Density, ), ))
    mdb.models['Model-1'].HomogeneousShellSection(name='Section-'+material_names[i],
        preIntegrate=OFF, material=material_names[i], thicknessType=UNIFORM,
        thickness=thickness, thicknessField='', idealization=NO_IDEALIZATION,
        poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT,
        useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)

# Create assembly
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['wing_structure']
a.Instance(name='wing_structure-1', part=p, dependent=ON)

# Create relevant surfaces and sets
f = p.faces
pickedRegions = enhanced_findAt(f, wing_data['x'], wing_data['y'],
                                wing_data['z'], coordinate_type = 'face_nodes')
p.Surface(side2Faces = pickedRegions, name='Surf-OML')
p.Set(faces = pickedRegions, name='Set-OML')

pickedRegions = enhanced_findAt(f, venation_data['x'], venation_data['y'],
                                venation_data['z'], coordinate_type = 'face_nodes',
                                ratio = 1.)
p.Set(faces = pickedRegions, name='Set-Venation-Structure')
mdb.saveAs(
    pathName='D:/Google Drive/PhD/MEEN689/project/generate_seed_module/wing_model')
