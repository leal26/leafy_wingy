from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup

import numpy as np
from airfoil_module import CST

def create_displacement_step(current_Step, prev_Step, span, chord,
                             deltaz, Au, Al, spar_x_coordinate):

    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['wing_structure']

    mdb.models['Model-1'].StaticStep(name=current_Step, previous=prev_Step)

    # Deactivating loads and BC's
    mdb.models['Model-1'].loads['Pressure'].deactivate(current_Step)
    mdb.models['Model-1'].boundaryConditions['BC-Encastre'].deactivate(
        'Morphing displacement')
    # fake morphing (quadratic, both with same coefficient)
    x_box = np.linspace(spar_x_coordinate[0], spar_x_coordinate[1], 20)
    x_after = np.linspace(spar_x_coordinate[1], chord, 80)
    x = np.array(list(x_box) + list(x_after))

    # Calculating displacement
    A = 0.04*chord/(chord**2 + chord - spar_x_coordinate[1]**2 -
                    spar_x_coordinate[1])
    B = -A*(spar_x_coordinate[1]**2 + spar_x_coordinate[1])
    displacement_box = np.linspace(0,0,20)
    displacement_after = A*(x_after**2+x_after)
    displacement = np.array(list(displacement_box) + list(displacement_after))

    y = CST(x, chord, deltaz, Au, Al)
    x = list(x) + list(x[-2::-1])
    y = list(y['u'][::-1]) + list(y['l'])
    displacement = list(displacement) + list(displacement[-1::-1])
    z = np.linspace(0,span,10)

    displacement_field = []
    for i in range(len(x)):
        for y_i in y:
            for z_i in z:
                displacement_field.append((x[i], y_i, z_i, displacement[i]),)

    # Generate the Displacement Field
    mdb.models['Model-1'].MappedField(name='Displacement', description='',
        regionType=POINT, partLevelData=False, localCsys=None, pointDataFormat=XYZ,
        fieldDataType=SCALAR, xyzPointData=displacement_field)
    region = a.instances['wing_structure-1'].sets['Set-OML']
    mdb.models['Model-1'].DisplacementBC(name='Displacement', createStepName=current_Step,
        region=region, u1=UNSET, u2=1.0, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
        localCsys=None)
