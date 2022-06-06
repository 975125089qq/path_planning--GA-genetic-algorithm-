# genetic algorithm search of the one max optimization problem
from numpy.random import randint
from numpy.random import rand
from continuous import continuous
import numpy as np

# Roulette Wheel Selection
def selection(pop, scores):
    # create a roulette wheel
    scores = 1 / scores
    sum_score = sum(scores)
    p_score = scores / sum_score
    p_score = np.cumsum(p_score)
    # create new pop
    pop_num = len(pop)
    new_pop = []
    # select
    index = np.sort(rand(pop_num))
    pointer = 0
    pos_wheel = 0
    while (pointer < pop_num):
        if (index[pointer]) < p_score[pos_wheel]:
            new_pop.append(pop[pos_wheel])
            pointer += 1
        else:
            pos_wheel += 1
    np.random.shuffle(new_pop)
    return new_pop


# crossover two parents to create two children
def crossover(p1, p2, p_cross):
    # create childrens
    c1, c2 = p1.copy(), p2.copy()
    # find shared positions
    common = list(set(p1[1:-1]) & set(p2[1:-1]))
    if rand() < p_cross and len(common) > 0:
        np.random.shuffle(common)
        # select crossover point
        num_common = common[0]
        # print(f"num_common:{num_common}")
        for index1 in range(1, len(p1) - 1):
            if p1[index1] == num_common:
                crossover_index1 = index1
                break
        for index2 in range(1, len(p2) - 1):
            if p2[index2] == num_common:
                crossover_index2 = index2
                break
        # perform crossover

        c1 = np.concatenate([p1[:crossover_index1], p2[crossover_index2:]])
        c2 = np.concatenate([p2[:crossover_index2], p1[crossover_index1:]])

    return [c1, c2]


# mutation operator
def mutation(chromosome, p_mut, map):
    result = chromosome.copy()
    if rand() < p_mut:
        num_mut1 = randint(0, len(result) - 1)  # choose two points to mutate
        num_mut2 = randint(0, len(result) - 1)
        while num_mut2 == num_mut1:  # make sure num_mut2 is different from num_mut1
            num_mut2 = randint(0, len(result) - 1)
        if num_mut1 > num_mut2:  # sort
            a = num_mut2
            num_mut2 = num_mut1
            num_mut1 = a
        pos_mut1 = result[num_mut1]  # position in the map
        pos_mut2 = result[num_mut2]
        part1, part2 = result[:num_mut1], result[num_mut2:]
        slice = continuous([pos_mut1, pos_mut2], map)
        if len(slice):
            result = np.concatenate([part1, slice, part2])
        # print(len(chromosome))
        # print(len(result))
    return result


# genetic algorithm
def genetic_algorithm(evaluation, n_iter, p_cross, p_mut, map, new_pop):
    # keep track of best solution
    map_size = map.shape[0]
    best, best_score = 0, evaluation(new_pop[0], map_size)
    # enumerate generations
    for gen in range(n_iter):
        # evaluate all candidates in the population
        scores = np.array([evaluation(c, map_size) for c in new_pop])
        # check for new best solution
        for i in range(len(new_pop)):
            if scores[i] < best_score:
                best, best_score = new_pop[i], scores[i]
                print(f"gen: {gen}\n path: {best}\n score: {best_score} ")
        # selection
        selected = selection(new_pop, scores)
        # create the next generation
        children = []
        # to see if new_pop is plural or singular
        parity = len(new_pop) % 2
        for i in range(0, len(new_pop) - parity, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i + 1]
            # crossover and mutation
            for c in crossover(p1, p2, p_cross):
                # mutation
                c = mutation(c, p_mut, map)
                # pass the mutation to the children
                children.append(c)

        # replace population
        new_pop = children

    return [best, best_score]
