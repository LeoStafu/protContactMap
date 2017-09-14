#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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


