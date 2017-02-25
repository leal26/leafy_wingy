# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-2 replay file
# Internal Version: 2014_08_22-09.00.46 134497
# Run by leal26 on Sat Feb 25 00:05:40 2017
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=234.129150390625, 
    height=264.936126708984)
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
#: 0.1 0.0510503734588 0.05
#: 0.3 0.0676998473523 0.05
#: 0.5 0.0615813734782 0.05
#: 0.7 0.0434898559548 0.05
#: 0.2 0.0636682017826 0.05
#: 0.4 0.0665171894226 0.05
#: 0.6 0.0537238509479 0.05
#: 0.8 0.0312699387798 0.05
#: 0.1 -0.0277981458236 0.05
#: 0.3 -0.0213460873106 0.05
#: 0.5 -0.00497747564417 0.05
#: 0.7 0.00653404703162 0.05
#: 0.2 -0.0274260120033 0.05
#: 0.4 -0.0132011880721 0.05
#: 0.6 0.00195415763715 0.05
#: 0.8 0.00788808364213 0.05
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
#: Warning: findAt could not find a geometric entity at (0.106973, 0.05155837, 0.05)
#: Warning: findAt could not find a geometric entity at (0.306827, 0.06687709, 0.05)
#: Warning: findAt could not find a geometric entity at (0.507933, 0.06040179, 0.05)
#: Warning: findAt could not find a geometric entity at (0.707708, 0.04225549, 0.05)
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: Warning: findAt could not find a geometric entity at (0.05551155, 0.04005073, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.04847109, 0.03772303, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.0418847, 0.03532538, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.03575938, 0.03286278, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.0301021, 0.03034021, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.0249169, 0.02776069, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.02021172, 0.02512923, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.01598859, 0.02245181, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.01225251, 0.01973245, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.00900845, 0.01697713, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.00625842, 0.01418987, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.00400541, 0.01137667, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.00225143, 0.00854351, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.00099945, 0.00569441, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.00024948, 0.00283536, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (2.52e-06, -1.878e-05, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.00025955, -0.0018967, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.00101957, -0.00376654, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.00228159, -0.00562031, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.00404558, -0.00745098, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.00630855, -0.00924858, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.00906849, -0.01100609, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.01232241, -0.01271455, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.01606828, -0.01436891, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.0203011, -0.01595922, 0.0)
#: []
#: Warning: findAt could not find a geometric entity at (0.0250159, -0.01748046, 0.0)
#: []
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: ['Face object']
#: The model database has been saved to "D:\Google Drive\PhD\MEEN689\project\generate_seed_module\wing_model.cae".
p = mdb.models['Model-1'].parts['wing_structure']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Material']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.8215, 
    farPlane=2.62356, width=0.997619, height=0.466248, cameraPosition=(1.77235, 
    0.448353, 1.82194), cameraUpVector=(-0.702021, 0.703576, -0.11022), 
    cameraTarget=(0.543846, -0.00708529, 0.0327832))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Material']
cmap.updateOverrides(overrides={'AL-6061':(False, )})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Material']
cmap.updateOverrides(overrides={'AL-6061':(False, '#0000FF', 'Default', 
    '#0000FF')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#000000')
cmap = session.viewports['Viewport: 1'].colorMappings['Material']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#000000')
cmap = session.viewports['Viewport: 1'].colorMappings['Material']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.8717, 
    farPlane=2.57757, width=1.02512, height=0.479099, cameraPosition=(1.57182, 
    -0.16699, 1.99121), cameraUpVector=(-0.459759, 0.885749, -0.0637979), 
    cameraTarget=(0.543846, -0.00708534, 0.0327832))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#000000')
cmap = session.viewports['Viewport: 1'].colorMappings['Material']
cmap.updateOverrides(overrides={'AL-6061':(True, )})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#000000')
cmap = session.viewports['Viewport: 1'].colorMappings['Material']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
