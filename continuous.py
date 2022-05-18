import math
import numpy as np

def continuous(one_pop, map):
    map_size = map.shape[0]
    path = one_pop
    i = 0
    while (i != len(path)-1):
        max_iteration = 0
        x_now = int(path[i] % map_size)
        x_next = int(path[i + 1] % map_size)
        y_now = int(path[i] // map_size)
        y_next = int(path[i+1] // map_size)
        # continuous or not
        while max(abs(x_now - x_next), abs(y_now - y_next)) > 1:
            x_insert = math.floor((x_next + x_now) / 2)
            y_insert = math.floor((y_next + y_now) / 2)

            if map[x_insert, y_insert] == 0:
                num_insert = y_insert * map_size + x_insert
                path = np.insert(path, i + 1, num_insert)
            else:
                # move left
                if x_insert >= 1 and judgement(x_insert - 1, y_insert, map, path, i) :
                    x_insert = x_insert - 1
                    num_insert = x_insert + y_insert * map_size
                    path = np.insert(path,i + 1, num_insert)

                # move right
                elif x_insert < map_size -1 and judgement(x_insert + 1, y_insert, map, path, i):
                    x_insert = x_insert + 1
                    num_insert = x_insert + y_insert * map_size
                    path = np.insert(path,i + 1, num_insert)

                # move up
                elif y_insert < map_size -1 and judgement(x_insert, y_insert + 1, map, path, i):
                    y_insert = y_insert + 1
                    num_insert = x_insert + y_insert * map_size
                    path = np.insert(path,i + 1, num_insert)

                # move down
                elif y_insert >= 1 and judgement(x_insert, y_insert - 1, map, path, i):
                    y_insert = y_insert - 1
                    num_insert = x_insert + y_insert * map_size
                    path = np.insert(path,i + 1, num_insert)

                else:
                    path = []
                    break

            x_next = x_insert
            y_next = y_insert
            max_iteration = max_iteration + 1
            if max_iteration > 20000:
                path = []
                break

        if not len(path):
            break

        i += 1
    return path


# to decide whether this point is possible
def judgement(x, y, map, path, i):
    map_size = map.shape[0]
    position =  x + y * map_size
    if map[x, y] == 0 and position != path[i] and position != path[i + 1] and position != path[i-1]:
        return True
    else:
        return False
