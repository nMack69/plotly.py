#!/usr/bin/python
import plotlyGenerics as pg
import numpy as np
from os import listdir
from os.path import isfile, join
from tkinter import *
root = Tk()

mainFrame = LabelFrame(root, text="Plotly Graphical User Interface", padx=100, pady=100)
mainFrame.grid(column=0,row=0, sticky=(N,W,E,S) )
mainFrame.columnconfigure(0, weight = 1)
mainFrame.rowconfigure(0, weight = 1)
mainFrame.pack(padx = 50, pady = 50)

tkvar = StringVar(root)

choices = [f for f in listdir('doc/python') if isfile(join('doc/python', f))]
tkvar.set('2D-Histogram.md')


def change_dropdown(*args):
	tkvar.trace('w', change_dropdown)

# handler for button and text fields
def clickRun():
	print(tkvar.get())
	print(entry1.get())
	print(entry2.get())
	# list(map(int, entry1.get().split())), list(map(int, entry2.get().split()))
	pg.isosurface_3d(list(map(int, entry1.get().split())), list(map(int, entry2.get().split())), z=[0])

buttonRun = Button(mainFrame, text="Run", command=clickRun)
buttonRun.grid(row = 5, column = 3)

popupMenu = OptionMenu(mainFrame, tkvar, *choices)
Label(mainFrame, text="Select a graph").grid(row = 1, column = 3)
popupMenu.grid(row = 2, column =3)

Label(mainFrame, text="Input 1").grid(row = 3, column = 1)
Label(mainFrame, text="Input 2").grid(row = 3, column = 5)

entry1 = Entry(mainFrame)
entry2 = Entry(mainFrame)

entry1.grid(row = 4, column = 1)
entry2.grid(row = 4, column = 5)

'''
canvas1 = Canvas(root, width = 100, height = 100)
canvas1.pack()
entry1 = Entry(root)
canvas1.create_window(200, 140, window=entry1)
'''

root.mainloop()
#f.close()






