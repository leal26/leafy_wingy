from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup

import numpy as np
from airfoil_module import CST

def create_displacement_step(current_Step, prev_Step, span, chord,
                             deltaz, Au, Al):

    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['wing_structure']

    mdb.models['Model-1'].StaticStep(name=current_Step, previous=prev_Step)
    mdb.models['Model-1'].loads['Pressure'].deactivate(current_Step)

    # fake morphing (quadratic, both with same coefficient)
    x = np.linspace(0,0.36,100)
    A = 0.04/(chord+1)
    displacement = A*(x**2+x)
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
