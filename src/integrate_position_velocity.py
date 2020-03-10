import numpy as np

def integrate_position_velocity(box,forces,deltat):
    atoms = box.atoms
    DIM  = len(box.box_size)

    positions_M = []
    velocities_M = []

    for j,atom in enumerate(atoms):
        positions = np.array(atom.position)
        velocities = np.array(atom.velocity)

        # this is to unfold the Boundary condition
        for i in range(DIM):
            positions[i] = positions[i] - np.floor(positions[i] / box.box_size[i]) * box.box_size[i]
            # basically the floor operator does the following
            # if positions[i]
            # - is greater than the box, floor = 1, so we subtract box size, to put it inside
            # - is inside the box, floor = 0, so nothing happens
            # - is smaller than box, floor = -1, so we sum box size, to put it inside

        atom.position = positions + deltat*velocities  + 0.5*deltat**2*forces[j]
        atom.velocity = velocities + deltat*forces[j]

        # print(atom.position)
        positions_M.append(positions)
        velocities_M.append(velocities)
    return positions_M, velocities_M