from xfoil_module import *
from airfoil_module import CST, create_x
import aero_module as aero

from abaqus import *
from abaqusConstants import *
from caeModules import *

def create_aerodynamic_step(x, y, velocity, altitude, aoa, chord, span,
                            StepName, prev_Step = 'Initial'):
    ModelName = 'Model-1'
    JobName = 'Aerodynamic_loading'

    # Getting all data
    Reynolds = aero.Reynolds(altitude, velocity, chord)

    airfoil='airfoil'
    # Create Text file with the new coordinates of the outer mold
    create_input(x, y['u'], y['l'], airfoil)

    xfoil_data= find_pressure_coefficients(airfoil, aoa, Reynolds=Reynolds,
                                           NACA=False)

    Forces = aero.pressure_shell_2D(Data=xfoil_data, chord=chord,
                                    half_span= span, height=altitude,
                                    Velocity=velocity, N=2, thickness=0)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Abaqus

    # Generate Step
    mdb.models['Model-1'].StaticStep(name=StepName, previous=prev_Step, nlgeom=ON)

    # Generate BC
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['wing_structure-1'].sets['Set-Spars']
    mdb.models['Model-1'].EncastreBC(name='BC-Encastre', createStepName=StepName,
        region=region, localCsys=None)
        
    # Generate the Force Field
    mdb.models['Model-1'].MappedField(name='Distribution', description='',
        regionType=POINT, partLevelData=False, localCsys=None, pointDataFormat=XYZ,
        fieldDataType=SCALAR, xyzPointData=Forces)

    # Generate the load inside Abaqus
    region = a.instances['wing_structure-1'].surfaces['Surf-OML']
    mdb.models['Model-1'].Pressure(name='Pressure', createStepName=StepName,
        region=region, distributionType=FIELD, field='Distribution',
        magnitude=1.0)

if __name__ == '__main__':
    # Parameters
    Au_avian = [0.23993240191629417, 0.34468227138908186, 0.18125405377549103,
            0.35371349126072665, 0.2440815012119143, 0.25724974995738387]
    Al_avian = [0.18889012559339036, -0.24686758992053115, 0.077569769493868401,
            -0.547827192265256, -0.0047342206759065641, -0.23994805474814629]
    deltaz = [0.002, 0.002]
    chord = 1.
    aoa = 2.
    velocity = 30.
