#!/usr/bin/python

from tkinter import *
root = Tk()

def printData(firstName, lastName):
    print(firstName)
    print(lastName)
    root.destroy()

def get_input():
    firstName = entry1.get()
    lastName = entry2.get()
    printData(firstName, lastName)

mainFrame = Frame(root)
mainFrame.grid(column=0,row=0, sticky=(N,W,E,S) )
mainFrame.columnconfigure(0, weight = 1)
mainFrame.rowconfigure(0, weight = 1)
mainFrame.pack(pady = 100, padx = 100)

tkvar = StringVar(root)

f = open('graphList.txt', 'r')
choices = []
for line in f:
	choices.append(line)

tkvar.set('2D-Histogram.md')


popupMenu = OptionMenu(mainFrame, tkvar, *choices)
Label(mainFrame, text="Select a graph").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

def change_dropdown(*args):
	print(tkvar.get())

tkvar.trace('w', change_dropdown)

root.mainloop()
f.close()