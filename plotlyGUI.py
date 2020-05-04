#!/usr/bin/python
import plotlyGenerics as pg
import numpy as np
from os import listdir
from os.path import isfile, join
from tkinter import *
root = Tk()
root.title("Plotly")

mainFrame = LabelFrame(root, text="Plotly Graphical User Interface", padx=100, pady=100)
mainFrame.grid(column=0,row=0, sticky=(N,W,E,S) )
mainFrame.columnconfigure(0, weight = 1)
mainFrame.rowconfigure(0, weight = 1)
#mainFrame.pack(padx = 50, pady = 50)

subFrame = LabelFrame(root, text="", padx=100, pady=20)
subFrame.grid(column=0, row=1, sticky=(N,W,E,S))
subFrame.columnconfigure(0, weight = 1)
subFrame.rowconfigure(0, weight = 1)
#subFrame.pack(padx = 50, pady = 20)

tkvar = StringVar(root)

choices = [f for f in listdir('doc/python') if isfile(join('doc/python', f))]
#tkvar.set(choices[0])

<<<<<<< HEAD
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

l1 = Label(subFrame, text="")
l2 = Label(subFrame, text="")
l3 = Label(subFrame, text="")
=======
>>>>>>> 5de90dd6cb704e6ed764fa56003505277ddb211d

def change_dropdown(*args):
	#subFrame.destroy()
	if (tkvar.get().count("3d") == 1):
		l1 = Label(subFrame, text="Input 1").grid(row = 3, column = 1)
		l2 = Label(subFrame, text="Input 2").grid(row = 3, column = 3)
		l3 = Label(subFrame, text="Input 3").grid(row = 3, column = 5)
		entry1 = Entry(subFrame)
		entry2 = Entry(subFrame)
		entry3 = Entry(subFrame)
		entry1.grid(row = 4, column = 1)
		entry2.grid(row = 4, column = 3)
		entry3.grid(row = 4, column = 5)
	else:
		l1 = Label(subFrame, text="Input 1").grid(row = 3, column = 1)
		l2 = Label(subFrame, text="Input 2").grid(row = 3, column = 5)
		entry1 = Entry(subFrame)
		entry2 = Entry(subFrame)
		entry1.grid(row = 4, column = 1)
		entry2.grid(row = 4, column = 5)

# handler for button and text fields
def clickRun():
	print(tkvar.get())
	print(entry1.get())
	print(entry2.get())
	# list(map(int, entry1.get().split())), list(map(int, entry2.get().split()))
	pg.isosurface_3d(list(map(int, entry1.get().split())), list(map(int, entry2.get().split())), z=[0])

buttonRun = Button(mainFrame, text="Run", command=clickRun)
buttonRun.grid(row = 5, column = 3)

popupMenu = OptionMenu(mainFrame, tkvar, *choices)#, command=traceTkvar)
Label(mainFrame, text="Select a graph").grid(row = 1, column = 3)
popupMenu.grid(row = 2, column =3)

tkvar.trace('w', change_dropdown)
'''
Label(mainFrame, text="Input 1").grid(row = 3, column = 1)
Label(mainFrame, text="Input 2").grid(row = 3, column = 5)

entry1 = Entry(mainFrame)
entry2 = Entry(mainFrame)

entry1.grid(row = 4, column = 1)
entry2.grid(row = 4, column = 5)
'''
'''
canvas1 = Canvas(root, width = 100, height = 100)
canvas1.pack()
entry1 = Entry(root)
canvas1.create_window(200, 140, window=entry1)
'''

root.mainloop()
#f.close()