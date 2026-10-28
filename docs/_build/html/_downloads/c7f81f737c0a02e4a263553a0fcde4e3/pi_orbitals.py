'''
This example shows how to find pi-orbitals of a heterocyclic compound using PyOrbb.

This example uses an ADF calculation on indole in a random orientation 
calculated at the OLYP/TZ2P level of theory with a small frozen core.
'''

import pyorbb
import scipy
import numpy as np


# load the orbital data
orbs = pyorbb.Orbitals('indole.adf.rkf')

# this molecule has a random orientation, so we must first find the
# normal vector to the plane of the molecule to find the right pi-orbitals
molecule = orbs.molecule

# find orthogonal components of the molecule using singular value decomposition
# we only need the rotation matrix Vh in this case
_, _, Vh = scipy.linalg.svd(molecule.as_array())

# the last row of Vh is the vector with the smallest component
# this should be the normal vector of the planar indole molecule
n = Vh[-1]

# we can then find the p-orbitals of the carbons and nitrogens
px_fmos = orbs.fmos.filter(fragment=('N', 'C'), orbname='2P:x')
py_fmos = orbs.fmos.filter(fragment=('N', 'C'), orbname='2P:y')
pz_fmos = orbs.fmos.filter(fragment=('N', 'C'), orbname='2P:z')

pi_mos = []
sigma_mos = []
# we then check every MO
for mo in orbs.mos:
    # and obtain the coefficients of the px, py and pz orbitals
    px_coeffs = [fmo.coefficient(mo) for fmo in px_fmos]
    py_coeffs = [fmo.coefficient(mo) for fmo in py_fmos]
    pz_coeffs = [fmo.coefficient(mo) for fmo in pz_fmos]
    # we can now construct the direction of the p-orbitals
    p_vectors = np.array([px_coeffs, py_coeffs, pz_coeffs]).T

    # and normalize the directions
    p_vectors = p_vectors / np.linalg.norm(p_vectors, axis=1, keepdims=True)

    # check if the directions are aligned with the normal vector
    alignments = np.dot(p_vectors, n)

    # the total alignment can just be the product of all individual alignments
    alignment = np.prod(alignments)

    # if the total alignment is close to 1 it is most likely a pi-orbital
    if alignment > 0.999:
        pi_mos.append(mo)
    # otherwise it is probably a sigma-orbital
    else:
        sigma_mos.append(mo)


print('π-MOs:')
print('\t'.join([mo.name.rjust(4) for mo in pi_mos]))
print()

print('σ-MOs:')
print('\t'.join([mo.name.rjust(4) for mo in sigma_mos]))
