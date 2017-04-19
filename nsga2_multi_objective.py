import math
import matplotlib.pyplot as plt

import array
import random
import numpy as np
import os
import sys
import pickle
import subprocess as sp

from deap import base
from deap import benchmarks
from deap import creator
from deap import tools

def run_abaqus(design_variables, V=30, alfa=8., chord=1.):
    input_file = 'design_variables.p'
    output_file = 'output.p'

    if V==30. and alfa==8. and chord==1.:
        command_file = 'launch_cmd.bat'
        design_variables = {'g': design_variables[0],
                            'k': 0.02 + (0.075-0.02)*design_variables[1],
                            'N': math.floor(100 + 900*design_variables[2])}
    else:
        command_file = 'launch_cmd_sensitivity.bat'
        design_variables = {'g': design_variables[0],
                            'k': 0.02 + (0.075-0.02)*design_variables[1],
                            'N': math.floor(100 + 900*design_variables[2]),
                            'V': V,
                            'alfa': alfa,
                            'c':chord}
    # Write input file
    fileObject = open(input_file,'wb')
    pickle.dump( design_variables, fileObject)
    fileObject.close()

    # Run bat file
    ps = sp.Popen(command_file)
    ps.wait()

    # Read output file
    fileObject = open(output_file,'rb')
    outputs = pickle.load(fileObject)
    fileObject.close()

    growth_distance = 0.02 + design_variables['g']*(design_variables['k'] - 0.02)
    fileObject = open('genetic_multi_data.txt','ab')
    fileObject.write('%.5f\t %.5f\t %.5f\t %.5f\t %.5f\t %.5f\t %.5f\n' % (design_variables['g'], growth_distance, design_variables['k'], design_variables['N'], abs(outputs['displacement']), outputs['nodes'], outputs['stress']))
    fileObject.close()
    
    lambda_displacement = 1e-10
    lambda_nodes = 1e-3
    if outputs['stress'] > 30e6:
    	penalization_displacement = lambda_displacement*(outputs['stress']-30e6)
    	penalization_nodes = lambda_nodes*(outputs['stress']-30e6)
    else:
    	penalization_displacement = 0
    	penalization_nodes = 0	
    return [abs(outputs['displacement']) + penalization_displacement, outputs['nodes'] + penalization_nodes]

#==============================================================================
# DEAP algorithm
#==============================================================================
fileObject = open('genetic_multi_data.txt','wb')
fileObject.close()

creator.create("FitnessMin", base.Fitness, weights=(-1.0,-1.0))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Problem definition
#               b,      t,      h,   beam_material,     n,  w,  d,      support_material
low_bound = [0, 0, 0]
high_bound = [1, 1, 1]

NDIM = 3

def uniform(low, up, size=None):
    try:
        return [random.uniform(a, b) for a, b in zip(low, up)]
    except TypeError:
        return [random.uniform(a, b) for a, b in zip([low] * size, [up] * size)]

toolbox.register("attr_float", uniform, low_bound, high_bound, NDIM)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.attr_float)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", run_abaqus)
toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=low_bound, up=high_bound, eta=20.0)
toolbox.register("mutate", tools.mutPolynomialBounded, low=low_bound, up=high_bound, eta=20.0, indpb=1.0/NDIM)
toolbox.register("select", tools.selNSGA2)
def main(seed=None):
    random.seed(seed)

    # Number of generations
    NGEN = 50
    # Population size (has to be a multiple of 4)
    MU = 40
    # Mating probability
    CXPB = 0.9

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    # stats.register("avg", np.mean, axis=0)
    # stats.register("std", np.std, axis=0)
    stats.register("min", np.min, axis=0)
    stats.register("max", np.max, axis=0)

    logbook = tools.Logbook()
    logbook.header = "gen", "evals", "std", "min", "avg", "max"

    pop = toolbox.population(n=MU)

    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in pop if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    # This is just to assign the crowding distance to the individuals
    # no actual selection is done
    pop = toolbox.select(pop, len(pop))

    record = stats.compile(pop)
    logbook.record(gen=0, evals=len(invalid_ind), **record)
    print(logbook.stream)

    # Begin the generational process
    for gen in range(1, NGEN):
        # Vary the population
        offspring = tools.selTournamentDCD(pop, len(pop))
        offspring = [toolbox.clone(ind) for ind in offspring]

        for ind1, ind2 in zip(offspring[::2], offspring[1::2]):
            if random.random() <= CXPB:
                toolbox.mate(ind1, ind2)

            toolbox.mutate(ind1)
            toolbox.mutate(ind2)
            del ind1.fitness.values, ind2.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # Select the next generation population
        pop = toolbox.select(pop + offspring, MU)
        record = stats.compile(pop)
        logbook.record(gen=gen, evals=len(invalid_ind), **record)
        print(logbook.stream)

#    print("Final population hypervolume is %f" % hypervolume(pop, [11.0, 11.0]))

    return pop, logbook

if __name__ == "__main__":


    pop, stats = main()
    pop.sort(key=lambda x: x.fitness.values)

    print(stats)


    front = np.array([ind.fitness.values for ind in pop])

    pickle.dump( front, open( "front.p", "wb" ) )
    pickle.dump( pop, open( "pop.p", "wb" ) )
    pickle.dump( stats, open( "stats.p", "wb" ) )
    plt.scatter(np.rad2deg(front[:,0]), front[:,1], c="b")
    plt.axis("tight")
    plt.grid()
    plt.xlabel("Deflection angle (${}^{\circ}$)")
    plt.ylabel("Heating load (J)")
    plt.show()
