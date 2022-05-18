import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

def generate_map(map_size,per):
    map=np.random.random((map_size,map_size))
    for i in range(map.shape[0]):
        for j in range(map.shape[0]):
            if map[i,j]<per:
                map[i,j]=1
            else:
                map[i,j]=0
    return map

def plt_map(x,best):
    LENGTH=x.shape[0]
    fig, ax = plt.subplots()
    for i in range(LENGTH):
        for j in range(LENGTH):
            if x[i, j] == 1:
                ax.add_patch(patches.Rectangle(xy=(i, j), width=1, height=1, edgecolor="black",fill=True))
            else:
                ax.add_patch(patches.Rectangle(xy=(i, j), width=1, height=1, edgecolor="black",fill=False))

    row, line = [0.5], [0.5]
    for i in best:
        row.append( i % LENGTH+0.5)
        line.append( i // LENGTH+0.5)
    row.append(LENGTH-0.5)
    line.append(LENGTH-0.5)
    plt.plot(row,line,color = 'red')
    ax.autoscale()
    plt.show()

