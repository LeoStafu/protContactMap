#!/home/leonard/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import math

class AminoAcid:

    def __init__(self, posX = 0.0, posY = 0.0, posZ = 0.0,
                 numAA = 0, nomAA = ""):
        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        self.numAA = numAA
        self.nomAA = nomAA

    def distance_to(self, aa):
        """Compute distance from self to another amino acid object
        """
        dist = math.sqrt( (aa.posX - self.posX)**2 
                        + (aa.posY - self.posY)**2 
                        + (aa.posZ - self.posZ)**2)
        return dist

    def __repr__(self):
        return("\n{} : Amino Acid n°: {}\nx = {}; y = {}; z = {}".format( \
            self.nomAA, self.numAA, self.posX, self.posY, self.posZ) )


if __name__ == "__main__":
    aa1 = AminoAcid(numAA = 1, nomAA = "LEU")
    aa2 = AminoAcid(posX = 1, posY = 1, posZ = 1, numAA = 2, nomAA = "VAL")
    print(aa1.distance_to(aa2))