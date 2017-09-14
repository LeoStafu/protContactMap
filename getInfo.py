#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import AminoAcid.py


def read_pdb_file(filename):
	"""Read pdb file and returns all lines containing alpha carbons in a list
	"""
	try:
		file_in = open(filename, "r")
	except:
		exit("Error: wrong filename")
	res = []
	for line in file_in:
        if line[0:6] == "ATOM" and line[12:16] == "CA":
        	res.append(line)
    return res


def create_residues(res_raw_list):
	"""Create AminoAcid objects based on the unprocessed pdb file lines
	Returns a list of objects
	"""
	all_aa = []
	for i in range(len(res_raw_list)):
		x = int(res_raw_list[i][30:38])
		y = int(res_raw_list[i][38:46])
		z = int(res_raw_list[i][46:54])
		num = int(res_raw_list[i][22:26])
		nom = (res_raw_list[i][17:20]).strip()
		aa = AminoAcid(posX = x, posY = y, posZ = z, numAA = num, nomAA = nom)
		all_aa.append(aa)
	return all_aa


