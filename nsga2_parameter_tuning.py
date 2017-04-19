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

from operator import attrgetter

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

    return [abs(outputs['displacement'])]

#==============================================================================
# DEAP algorithm
#==============================================================================

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
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
	global eta_mutate, eta_crossover, CXPB, N_t
	# Number of generations
	NGEN = 10
	# Population size (has to be a multiple of 4)
	MU = 20
	# Mating probability

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
		offspring = tools.selTournamentDCD(pop, N_t)
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

	eta_mutate_list = [10,50]
	eta_crossover_list = [10, 50]
	CXPB_list = [.8, .95]
	N_t_list = [10, 15]

	eta_crossover = 20.
	eta_mutate= 20.
	CXPB=.9
	N_t = 20
	
	pop, stats = main()
	pop.sort(key=lambda x: x.fitness.values)
	best = max(pop, key=attrgetter("fitness"))
	print(stats)
	fileObject = open('parameter_tuning_data.txt','wb')
	fileObject.write('%5f\t %5f\t %5f\t %5f\t %.5f\n' % (eta_crossover, eta_mutate, CXPB, N_t, best.fitness.values[0]))
	fileObject.close()
	print best.fitness.values

	for eta_mutate in eta_mutate_list:
		pop, stats = main()
		pop.sort(key=lambda x: x.fitness.values)
		best = max(pop, key=attrgetter("fitness"))
		print(stats)
		print best
		fileObject = open('parameter_tuning_data.txt','ab')
		fileObject.write('%5f\t %5f\t %5f\t %5f\t %.5f\n' % (eta_crossover, eta_mutate, CXPB, N_t, best.fitness.values[0]))
		fileObject.close()
		print best.fitness.values

	for eta_crossover in eta_crossover_list:
		pop, stats = main()
		pop.sort(key=lambda x: x.fitness.values)
		best = max(pop, key=attrgetter("fitness"))
		print(stats)
		fileObject = open('parameter_tuning_data.txt','ab')
		fileObject.write('%5f\t %5f\t %5f\t %5f\t %.5f\n' % (eta_crossover, eta_mutate, CXPB, N_t, best.fitness.values[0]))
		fileObject.close()	

	for CXPB in CXPB_list:
		pop, stats = main()
		pop.sort(key=lambda x: x.fitness.values)
		best = max(pop, key=attrgetter("fitness"))
		print(stats)
		fileObject = open('parameter_tuning_data.txt','ab')
		fileObject.write('%5f\t %5f\t %5f\t %5f\t %.5f\n' % (eta_crossover, eta_mutate, CXPB, N_t, best.fitness.values[0]))
		fileObject.close()	

	for N_t in N_t_list:
		pop, stats = main()
		pop.sort(key=lambda x: x.fitness.values)
		best = max(pop, key=attrgetter("fitness"))
		print(stats)
		fileObject = open('parameter_tuning_data.txt','ab')
		fileObject.write('%5f\t %5f\t %5f\t %5f\t %.5f\n' % (eta_crossover, eta_mutate, CXPB, N_t, best.fitness.values[0]))
		fileObject.close()	

