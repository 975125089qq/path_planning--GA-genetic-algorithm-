# genetic algorithm search of the one max optimization problem
import pandas as pd
from numpy.random import randint
from evaluation import evaluation
from map import generate_map, plt_map
from genetic_algorithm import genetic_algorithm
import numpy as np
from continuous import continuous

# find possible points in the map
def search(map, ys, ye):
    map_size = map.shape[0]
    can = []
    for yk in range(ys, ye + 1):
        can_line = []  # possible points in a line
        for xk in range(map_size):
            if map[xk, yk] != 1:
                num = xk + yk * map_size
                can_line.append(num)
        can.append(can_line)
    return can

# the size of map
map_size =20
# define the total iterations
n_iter = 100
# define the population size
n_pop = 100
# crossover rate
p_cross = 0.8
# mutation possibility
p_mut = 0.2

# starting position
p_start = 0
# ending position
p_end = map_size * map_size -1

per = 0.2# how many obstacles

# generate the map
map = generate_map(map_size, per)

# the coordinates of starting and ending position
xs = p_start % map_size
ys = p_start // map_size
xe = p_end % map_size
ye = p_end // map_size

pass_num = ye - ys + 1
pop = np.zeros((n_pop, pass_num)).astype("int")
can = search(map,ys,ye)
new_pop = []

# initilize
for i in range(n_pop):
    pop[i, 0] = p_start
    # find a possible point in a line
    for line in range(1,pass_num-1):
        index = np.random.randint(len(can[line]))
        pop[i, line] = can[line][index]
    pop[i, -1] = p_end
    path = continuous(pop[i], map)
    if (len(path)):  # if there exists a path
        new_pop.append(path)
if not len(new_pop):
    print(" the map is too complex for my current program")
    plt_map(map, [])

# iterations
best, score = genetic_algorithm(evaluation, n_iter, p_cross, p_mut, map, new_pop)
print("what has happened")
plt_map(map, best)
print('Done!')
print('f(%s) = %f' % (best, score))
