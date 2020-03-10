from src.box_atoms import Box
from src.create_atoms_random import create_atoms_random
from src.create_atoms_random import Atom
from src.compute_forces import compute_forces
from src.integrate_position_velocity import integrate_position_velocity
import numpy as np
L = [1,1,1]
N = 10

atoms = create_atoms_random(L, N, v=(0.1,0.1,0.1), m=1, seed=42)
box = Box(L,atoms)

deltat = 0.000001
tend =   0.001
t = 0

positions_time = []
velocities_time = []
i = 0
while t<tend:
    forces = compute_forces(box, Rcutoff=2.5)
    positions, velocities = integrate_position_velocity(box,forces,deltat)
    positions_time.append(positions)
    velocities_time.append(velocities)
    print('step done')
    t += deltat

# 3D plot
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import matplotlib.animation as animation


positions_time0 = np.array(positions_time[0]).T.tolist()

def update_graph(num):
    positions_timeN = np.array(positions_time[num]).T.tolist()
    print(positions_timeN)
    graph.set_data (positions_timeN[0], positions_timeN[1])
    graph.set_3d_properties(positions_timeN[2])
    return graph,

# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
title = ax.set_title('3D Test')

graph, = ax.plot(positions_time0[0],positions_time0[1], positions_time0[2], 'o')

ani = animation.FuncAnimation(fig, update_graph, 100,
                                         interval=150, blit=False)

plt.show()
