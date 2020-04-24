# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
from pygra import operators

op0 = h.get_operator("valley")
h.get_bands(operator=op0)
