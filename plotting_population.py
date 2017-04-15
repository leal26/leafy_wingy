import math
import matplotlib.pyplot as plt
import pickle

fileobject = open('pop.p','rb')
pop = pickle.load(fileobject)

fileobject = open('front.p','rb')
front = pickle.load(fileobject)

fileobject = open('stats.p','rb')
stats = pickle.load(fileobject)

print pop.keys()
print front.keys()
plt.scatter(), front[:,1], c="b")
plt.axis("tight")
plt.grid()
plt.xlabel("Deflection angle (${}^{\circ}$)")
plt.ylabel("Heating load (J)")
plt.show()