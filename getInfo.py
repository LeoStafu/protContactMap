#!/home/leonard/anaconda3/bin/python3
# -*- coding: utf-8 -*-

from AminoAcid import *
import urllib.request
import os


def pdb_file_dl(filename):
    address = "https://files.rcsb.org/download/" + filename
    try:
        data = urllib.request.urlretrieve(address, filename)
    except IOError as e:
        if hasattr(e, 'reason'):
            exit("Cannot reach web server: " + str(e.reason))
        if hasattr(e, 'code'):
            exit("Server failed {:d}".format(e.code))
    

def read_pdb_file(filename):
    """Read pdb file and returns all lines containing alpha carbons in a list
    """
    if filename in os.listdir():
        try:
            file_in = open(filename, "r")
        except:
            exit("File not found.")
    else:
        print("Downloading file from pdb server...")
        pdb_file_dl(filename)
        try:
            file_in = open(filename, "r")
        except:
            exit("Impossible to download file from pdb server or to open it")
    res = []
    for line in file_in:
        if line[0:6].strip() == "ATOM" and line[12:16].strip() == "CA":
            res.append(line)
    return res


def create_residues(res_raw_list):
    """Create AminoAcid objects based on the unprocessed pdb file lines
    Returns a list of objects
    """
    all_aa = []
    for i in range(len(res_raw_list)):
        x = float(res_raw_list[i][30:38])
        y = float(res_raw_list[i][38:46])
        z = float(res_raw_list[i][46:54])
        num = int(res_raw_list[i][22:26])
        nom = (res_raw_list[i][17:20]).strip()
        aa = AminoAcid(posX = x, posY = y, posZ = z, numAA = num, nomAA = nom)
        all_aa.append(aa)
    return all_aa
