# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-2 replay file
# Internal Version: 2014_08_22-09.00.46 134497
# Run by leal26 on Fri Feb 24 19:01:23 2017
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=234.129150390625, 
    height=254.352783203125)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('generate_module.py', __main__.__dict__)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: Warning: findAt could not find a geometric entity at (0.05551155, 0.04005073, 0.0)
#: Warning: findAt could not find a geometric entity at (0.04847109, 0.03772303, 0.0)
#: Warning: findAt could not find a geometric entity at (0.0418847, 0.03532538, 0.0)
#: Warning: findAt could not find a geometric entity at (0.03575938, 0.03286278, 0.0)
#: Warning: findAt could not find a geometric entity at (0.0301021, 0.03034021, 0.0)
#: Warning: findAt could not find a geometric entity at (0.0249169, 0.02776069, 0.0)
#: Warning: findAt could not find a geometric entity at (0.02021172, 0.02512923, 0.0)
#: Warning: findAt could not find a geometric entity at (0.01598859, 0.02245181, 0.0)
#: Warning: findAt could not find a geometric entity at (0.01225251, 0.01973245, 0.0)
#: Warning: findAt could not find a geometric entity at (0.00900845, 0.01697713, 0.0)
#: Warning: findAt could not find a geometric entity at (0.00625842, 0.01418987, 0.0)
#: Warning: findAt could not find a geometric entity at (0.00400541, 0.01137667, 0.0)
#: Warning: findAt could not find a geometric entity at (0.00225143, 0.00854351, 0.0)
#: Warning: findAt could not find a geometric entity at (0.00099945, 0.00569441, 0.0)
#: Warning: findAt could not find a geometric entity at (0.00024948, 0.00283536, 0.0)
#: Warning: findAt could not find a geometric entity at (2.52e-06, -1.878e-05, 0.0)
#: Warning: findAt could not find a geometric entity at (0.00025955, -0.0018967, 0.0)
#: Warning: findAt could not find a geometric entity at (0.00101957, -0.00376654, 0.0)
#: Warning: findAt could not find a geometric entity at (0.00228159, -0.00562031, 0.0)
#: Warning: findAt could not find a geometric entity at (0.00404558, -0.00745098, 0.0)
#: Warning: findAt could not find a geometric entity at (0.00630855, -0.00924858, 0.0)
#: Warning: findAt could not find a geometric entity at (0.00906849, -0.01100609, 0.0)
#: Warning: findAt could not find a geometric entity at (0.01232241, -0.01271455, 0.0)
#: Warning: findAt could not find a geometric entity at (0.01606828, -0.01436891, 0.0)
#: Warning: findAt could not find a geometric entity at (0.0203011, -0.01595922, 0.0)
#: Warning: findAt could not find a geometric entity at (0.0250159, -0.01748046, 0.0)
#: The model database has been saved to "D:\Google Drive\PhD\MEEN689\project\generate_seed_module\wing_model.cae".
p1 = mdb.models['Model-1'].parts['wing_structure']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.90719, 
    farPlane=2.14796, width=1.01266, height=0.491207, cameraUpVector=(
    0.0781012, 0.996945, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.49359, 
    farPlane=2.56157, width=0.79305, height=0.384683, cameraPosition=(-1.25924, 
    0.233834, 1.03793), cameraUpVector=(0.17831, 0.976717, 0.119289))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.59246, 
    farPlane=2.4627, width=0.845546, height=0.410147, cameraPosition=(
    -0.783545, -1.08784, 1.14847), cameraUpVector=(-0.377679, 0.831506, 
    0.407378), cameraTarget=(0.499987, 0.0333277, 0.0499999))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.5534, 
    farPlane=2.50177, width=0.824806, height=0.400087, cameraPosition=(
    -1.00113, 0.477867, 1.33847), cameraUpVector=(0.204319, 0.973986, 
    -0.098001), cameraTarget=(0.499987, 0.0333275, 0.0499999))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.82565, 
    farPlane=2.22953, width=0.96936, height=0.470206, cameraPosition=(0.216792, 
    1.03182, 1.79182), cameraUpVector=(0.306991, 0.846351, -0.435256), 
    cameraTarget=(0.499987, 0.0333274, 0.0499998))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.80723, 
    farPlane=2.24795, width=0.95958, height=0.465462, cameraPosition=(
    0.0816945, -0.0418115, 2.03255), cameraUpVector=(0.0321239, 0.998487, 
    0.0446202), cameraTarget=(0.499987, 0.0333277, 0.0499997))
p = mdb.models['Model-1'].parts['wing_structure']
p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=0.0)
p = mdb.models['Model-1'].parts['wing_structure']
p.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=0.3)
p = mdb.models['Model-1'].parts['wing_structure']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#200 ]', ), )
d = p.datums
p.PartitionFaceByDatumPlane(datumPlane=d[6], faces=pickedFaces)
