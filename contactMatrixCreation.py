#!/home/leonard/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

from AminoAcid import *
from getInfo import *
from contactMapGUI import *


def matrix_process():

    pdb_ID, distThres, mode = main_menu()
    #print(pdb_ID, distThres, mode)
    rawCA = read_pdb_file(pdb_ID + ".pdb")
    #print(rawCA)
    allCA = create_residues(rawCA)
    #print(allCA)
    nbResidue = len(allCA)

    distMatrix = np.zeros((nbResidue, nbResidue), float)

    for i in range(0,nbResidue-1):
        for j in range(i+1, nbResidue):
            distMatrix[i][j] = round(allCA[i].distance_to(allCA[j]), 2)

    #print(distMatrix)
    #print("")
    distMatrix = distMatrix + distMatrix.T
    #print(distMatrix)
    contactMatrix = distMatrix < distThres
    if mode == "grey":
        for i in range(distMatrix.shape[0]):
            for j in range(distMatrix.shape[1]):
                if distMatrix[i, j] > distThres :
                    distMatrix[i, j] = distThres
    #print(contactMatrix)

    print_matrix(distMatrix, mode)



matrix_process()