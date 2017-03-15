# My libraries
from xfoil_module import output_reader
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

def generate_module(Au, Al, deltaz, spar_x_coordinate, chord, span,
                 aluminum_type, venation_type, aluminum_thickness,
                 aluminum_properties, SMA_thickness, SMA_properties,
                 venation_properties, x_u1, x_u2, x_l1, x_l2, datafile):

    # Spar coordinates
    spar_y_coordinate = CST(spar_x_coordinate, chord, deltaz, Au, Al)
    spar_locations = {'x1':spar_x_coordinate, 'y1':spar_y_coordinate['u'],
                      'x2':spar_x_coordinate, 'y2':spar_y_coordinate['l']}

    y_u1 = list(CST(x_u1, chord, deltaz[0], Au=Au))
    y_u2 = list(CST(x_u2, chord, deltaz[0], Au=Au))
    y_l1 = list(CST(x_l1, chord, deltaz[1], Al=Al))
    y_l2 = list(CST(x_l2, chord, deltaz[1], Al=Al))

    material_sets = ['Set-OML-Aluminum','Set-SMA','Set-Venation-Structure', 'Set-Spars']
    material_properties = [aluminum_properties, SMA_properties, venation_properties,
                           venation_properties]
    material_names = ['AL-2024', 'SMA', 'AL-6061', 'AL-6061']
    material_thicknesses = [aluminum_thickness, SMA_thickness, aluminum_thickness,
                            aluminum_thickness]

    # Abaqus
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # CREATING PARTS AND ASSEMBLY
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

    # Generating structure
    wing_venation_generator(wing_data, venation_data, span, spar_locations)

    # Partitioning
    p = mdb.models['Model-1'].parts['wing_structure']
    x_partitions = x_u1 + x_u2 + x_l1 + x_l2
    y_partitions = y_u1 + y_u2 + y_l1 + y_l2
    z_partitions = [span/2. for i in range(len(x_partitions))]
    enhanced_partition(p, x_partitions, y_partitions, z_partitions)

    # Create assembly
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['wing_structure']
    a.Instance(name='wing_structure-1', part=p, dependent=ON)

    # Create mesh
    p.generateMesh()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # SURFACES AND SETS
    # Surface for Outer Mold Line
    f = p.faces
    pickedRegions = enhanced_findAt(f, wing_data['x'], wing_data['y'],
                                    wing_data['z'], coordinate_type = 'face_nodes')
    p.Surface(side2Faces = pickedRegions, name='Surf-OML')
    p.Set(faces = pickedRegions, name='Set-OML')

    # Set for internal Venation structure
    pickedRegions = enhanced_findAt(f, venation_data['x'], venation_data['y'],
                                    venation_data['z'], coordinate_type = 'face_nodes',
                                    ratio = 1.)
    p.Set(faces = pickedRegions, name='Set-Venation-Structure')

    # Set for Main box
    camber_y_coordinate = [(spar_y_coordinate['u'][0]-spar_y_coordinate['l'][0])/2.,
                           (spar_y_coordinate['u'][1]-spar_y_coordinate['l'][1])/2.]

    spar_data = {'x':[spar_x_coordinate[0], spar_x_coordinate[0],
                      spar_x_coordinate[1], spar_x_coordinate[1]],
                 'y':[(spar_y_coordinate['u'][0] + camber_y_coordinate[0])/2.,
                      (spar_y_coordinate['l'][0] + camber_y_coordinate[0])/2.,
                      (spar_y_coordinate['u'][1] + camber_y_coordinate[1])/2.,
                      (spar_y_coordinate['l'][1] + camber_y_coordinate[1])/2.],
                 'z':[span/2., span/2., span/2., span/2.]}

    pickedRegions = enhanced_findAt(f, spar_data['x'], spar_data['y'],
                                    spar_data['z'], coordinate_type = 'face_nodes',
                                    ratio = 1.)
    p.Set(faces = pickedRegions, name='Set-Spars')

    # Set for trailing edge displacement
    a = mdb.models['Model-1'].rootAssembly
    v = a.instances['wing_structure-1'].vertices

    # TE_v = (0,0,0)
    # TE_index = 0
    # for i in range(len(v)):
    #     if v[i].pointOn[0][0] > TE_v[0]:
    #         TE_v = v[i].pointOn[0]
    #         TE_index = i
    # verts = v[TE_index]
    verts = v.findAt(((1.0, -0.002, 0.0),))
    a.Set(vertices=verts, name='TIPNODE')
    ## Find Set-SMA and Set OML-Aluminum
    # List of actuator coordinates
    x_1 = x_u1 + x_l1
    x_2 = x_u2 + x_l2
    y_1 = y_u1 + y_l1
    y_2 = y_u2 + y_l2

    # Use points from OML to precisely find faces. Since Abaqus used a Spline
    # other sampled points might not have same y
    for i in range(len(x_u1)):
        x_u = [x1 for x1 in wing_data['x'] if x1 > x_u1[i] and x1 <x_u2[i]]
        y_u = [y1 for x1,y1 in zip(wing_data['x'], wing_data['y']) if x1 > x_u1[i] and x1 <x_u2[i]]
        z_u = len(x_u)*[span/2.]

        if i == 0:
            PickedFace = enhanced_findAt(f, x_u, y_u,
                                            z_u, coordinate_type = 'face_nodes')
        else:
            PickedFace += enhanced_findAt(f, x_u, y_u,
                                            z_u, coordinate_type = 'face_nodes')
    p.Set(faces = PickedFace, name='Set-SMA')
    # Neglecting the points selected for Set-SMA, choose Set-Aluminum
    # Include trailing edge section
    f = p.faces
    pickedRegions = enhanced_findAt(f, wing_data['x'] + [chord],
                                    wing_data['y'] + [0],
                                    wing_data['z'] + [span/2.],
                                    coordinate_type = 'face_nodes',
                                    not_select = PickedFace)
    p.Set(faces = pickedRegions, name='Set-OML-Aluminum')

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # MATERIAL SECTION
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
        region = p.sets[material_sets[i]]
        p.SectionAssignment(region=region, sectionName='Section-'+material_names[i], offset=0.0,
            offsetType=MIDDLE_SURFACE, offsetField='',
            thicknessAssignment=FROM_SECTION)
