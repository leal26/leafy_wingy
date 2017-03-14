from xfoil_module import *
from airfoil_module import CST, create_x
import aero_module as aero

def stress_under_aerodynamic_load(x, y, velocity, altitude, chord):
    StepName = 'Aerodynamic loading'
    ModelName = 'Model-1'
    JobName = 'Aerodynamic_loading'

    # Getting all data
    Reynolds = aero.Reynolds(altitude, velocity, chord)

    airfoil='avian_airfoil'
    # Create Text file with the new coordinates of the outer mold
    create_input(x, y['u'], y['l'], airfoil)

    xfoil_data= find_pressure_coefficients(airfoil, aoa, Reynolds=Reynolds,
                                           NACA=False)

    Forces = aero.pressure_shell_2D(Data=Data, chord=chord, half_span= span, height=height, Velocity=velocity, N=2, thickness=0)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Abaqus

    # Generate Step
    mdb.models['Model-1'].StaticStep(name=StepName, previous='Initial', nlgeom=ON)

    # Generate BC
    mdb.models['Model-1'].EncastreBC(name='BC-Encastre', createStepName=StepName,
        region=region, localCsys=None)

    # Generate the Force Field
    model.MappedField(name='Distribution', description='',
        regionType=POINT, partLevelData=False, localCsys=None, pointDataFormat=XYZ,
        fieldDataType=SCALAR, xyzPointData=Forces)

    # Generate the load inside Abaqus
    a = model.rootAssembly
    region = a.instances[InstanceName].surfaces['Surf-OML']
    model.Pressure(name='Pressure', createStepName=StepName,
        region=region, distributionType=FIELD, field='Distribution',
        magnitude=1.0)

    # Check for lock files
    if os.access('%s.lck'% JobName,os.F_OK):
        os.remove('%s.lck'% JobName)

    # Create job and submit
    job = mdb.Job(name=JobName, model=ModelName, description='', type=RESTART,
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
        scratch='',  parallelizationMethodExplicit=DOMAIN, numDomains=4, activateLoadBalancing=False,
        multiprocessingMode=DEFAULT, numCpus=4)

    job.submit()
    job.waitForCompletion()

    maxMises = find_maxMises('Aerodynamic_loading', StepName)

    return maxMises
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
