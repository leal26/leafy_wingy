# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-2 replay file
# Internal Version: 2014_08_22-09.00.46 134497
# Run by leal26 on Tue Mar 14 13:49:28 2017
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
#: 0.15 0.0588175831499 0.05
#: 0.35 0.0676473941395 0.05
#: 0.6 0.0537238509479 0.05
#: 0.8 0.0312699387798 0.05
#: 0.1 -0.0277981458236 0.05
#: 0.3 -0.0213460873106 0.05
#: 0.5 -0.00497747564417 0.05
#: 0.7 0.00653404703162 0.05
#: 0.15 -0.0286954551748 0.05
#: 0.35 -0.0173873383422 0.05
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
#* NameError: global name 'deltaz' is not defined
#* File "generate_module.py", line 179, in <module>
#*     print stress_under_aerodynamic_load(x, y, velocity, altitude, chord)
#* File "C:\Users\leal26\Documents\GitHub\leafy_wingy\aerodynamic_module.py", 
#* line 12, in stress_under_aerodynamic_load
#*     y = CST(x, chord, deltaz, Au_avian, Al_avian)
p = mdb.models['Model-1'].parts['wing_structure']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
