#!/usr/bin/python
import plotly.graph_objects as go
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

# Enter space separated INTEGER values into 'entry 1' and 'entry 2' fields on PlotlyGUI
# ex, 1 2 3 4 5 6 etc.
# Only 3D scatter plots supported at the moment
def scatterPlot():
	# Helix equation
	t = np.linspace(0, 20, 100)
	x, y, z = list(map(int, entry1.get().split())), list(map(int, entry2.get().split())), t

	fig = go.Figure(data=[go.Scatter3d(
		x=x,
		y=y,
		z=z,
		mode='markers',
		marker=dict(
			size=12,
			color=z,                # set color to an array/list of desired values
			colorscale='Viridis',   # choose a colorscale
			opacity=0.8
		)
	)])

	# tight layout
	fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
	fig.show()


def change_dropdown(*args):
	tkvar.trace('w', change_dropdown)

# handler for button and text fields
def clickRun():
	print(tkvar.get())
	print(entry1.get())
	print(entry2.get())
	scatterPlot()

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






