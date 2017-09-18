#!/home/leonard/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pylab as plt

from AminoAcid import *
from getInfo import *

#Reading file
if len(sys.argv) >= 3:
    filename = sys.argv[1]
    distThres = float(sys.argv[2])

rawCA = read_pdb_file(filename)
print(rawCA)
allCA = create_residues(rawCA)

print(allCA)
nbResidue = len(allCA)

distMatrix = np.zeros((nbResidue, nbResidue), float)

for i in range(0,nbResidue-1):
    for j in range(i+1, nbResidue):
        distMatrix[i][j] = round(allCA[i].distance_to(allCA[j]), 2)

print(distMatrix)
print("")
distMatrix = distMatrix + distMatrix.T

print(distMatrix)

contactMatrix = distMatrix < distThres
print(contactMatrix)

plt.imshow(distMatrix, interpolation='nearest', cmap=plt.cm.ocean)
plt.colorbar()
plt.show()
