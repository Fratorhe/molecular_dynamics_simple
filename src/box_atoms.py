
class Box():
    def __init__(self, L, atoms):
        self._L = L
        self.atoms = atoms
        self.N = len(atoms)
        self.cutoff = 2.5

    @property
    def box_size(self):
        return self._L

    # @box_size.setter
    # def box_size(self,box_size):

    def __str__(self):
        return "The box has %s atoms and has a length %s" % (self.N, self.box_size)

