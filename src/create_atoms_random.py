import numpy as np

from numpy.random import rand

class Atom():

    def __init__(self, x, y, z, vx, vy, vz):
        self._x = x
        self._y = y
        self._z = z

        self._vx = vx
        self._vy = vy
        self._vz = vz

    # positions

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,new_y):
        self._y = new_y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self,new_z):
        self._z = new_z

    @property
    def position(self):
        return self._x, self._y, self._z

    @position.setter
    def position(self,new_position):
        self.x = new_position[0]
        self.y = new_position[1]
        self.z = new_position[2]

    # velocities

    @property
    def vx(self):
        return self._vx

    @vx.setter
    def vx(self,new_vx):
        self._vx = new_vx

    @property
    def vy(self):
        return self._vy

    @vy.setter
    def vy(self,new_vy):
        self._vy = new_vy

    @property
    def vz(self):
        return self._vz

    @vz.setter
    def vz(self,new_vz):
        self._vz = new_vz

    @property
    def velocity(self):
        return self._vx, self._vy, self._vz

    @velocity.setter
    def velocity(self,new_velocity):
        self.vx = new_velocity[0]
        self.vy = new_velocity[1]
        self.vz = new_velocity[2]


def create_atoms_random(L, N, v=(1,1,1), m=1, seed=None):
# this function generates atoms in a random way in a box of size L
# N number of atoms
# L is the box size [lx, ly, lz]
# m is the mass, let's keep it =1 for the moment
    if seed is not None:
        np.random.seed(seed)

    atoms = []
    for atom in range(N):
        L = np.array(L)
        random_pos = rand(3)
        random_pos = random_pos*L
        new_atom = Atom(*random_pos,*v)
        atoms.append(new_atom)

    return atoms

if __name__ == '__main__':

    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

    import matplotlib.pyplot as plt

    atoms = create_atoms_random([1, 1, 1], 20, m=1)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    atoms[0].position = [0,0,0] # we can force a position with this

    for atom in atoms:
        ax.scatter(atom.x, atom.y, atom.z)

    plt.show()