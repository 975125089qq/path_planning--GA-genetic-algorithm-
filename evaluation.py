import numpy as np


def evaluation(x, map_size):
    distance = 0
    for i in range(len(x)-1):
        distance += discal(x[i],x[i+1],map_size)
    return distance


def discal(x1, x2, map_size):
    row1, row2 = x1 % map_size, x2 % map_size
    line1, line2 = x1 // map_size, x2 // map_size
    distance = np.sqrt((row1 - row2)**2 + (line1 - line2) ** 2)
    return distance
