#!/home/leonard/anaconda3/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
import matplotlib.pylab as plt



def main_menu():
    root = Tk()
    root.title("Protein Contact Map")

    pdb_ID = ""
    txt1 = Label(root, text="PDB ID")
    txt1.grid(row = 1, column = 0, sticky = W, padx = 20, pady = 10)
    entry_ID = Entry(root, textvariable = pdb_ID)
    entry_ID.grid(row = 1, column = 2, padx = 20, pady = 10)

    txt2 = Label(root, text="Distance Threshold (Å)")
    txt2.grid(row = 2, column = 0, sticky = W, padx = 20, pady = 10)
    distThres = Scale(root, from_ = 0, to = 15, orient = HORIZONTAL)
    distThres.grid(row = 2, column = 2, padx = 20, pady = 10)

    mode = StringVar()
    greyscale = Radiobutton(root, text="Grey scale", variable=mode, value="grey")
    colorscale = Radiobutton(root, text="Color scale", variable=mode, value="color")
    ligand = Radiobutton(root, text="With ligand", variable=mode, value="ligand")
    greyscale.grid(row = 3, column = 0, padx = 5, pady = 5)
    colorscale.grid(row = 3, column = 1, padx = 5, pady = 5)
    ligand.grid(row = 3, column = 2, padx = 5, pady = 5)

    button_go = Button(root, text = "GO !", command = root.quit)
    button_go.grid(row = 5, column = 1, padx = 5, pady = 5)

    root.mainloop()
    return (entry_ID.get(), distThres.get(), mode.get())


def print_matrix(matrix):
    plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.rainbow)
    plt.colorbar()
    plt.show()
