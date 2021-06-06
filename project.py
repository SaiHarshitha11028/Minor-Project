from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from tkinter import *

def plotscatter():
	#frame for plot
	panel= LabelFrame(r1,text="PLOT")
	panel.pack()

	#getting input
	x= list(map(int, entry1.get().split(",")))
	y=list(map(int, entry2.get().split(",")))

	fig = Figure(figsize=(12, 7), dpi=100)
    	plot1 = fig.add_subplot(111)
    	plot1.set_xlabel(entry3.get())
    	plot1.set_ylabel(entry4.get())
    	plot1.scatter(x, y)
    	canvas = FigureCanvasTkAgg(fig, master=panel)
    	canvas.draw()
    	canvas.get_tk_widget().pack()

def scatterplt():
	#destroying old window
	global root
	root.destroy()

	#creating new window
	global r1
	r1=Tk()
	r1.state("zoomed")

	#adding frame to window
	frame_2=LabelFrame(r1)
	frame.place(width=1920, height=480)
	frame_2.pack()

	#creating labels for input fields
	label1=Label(frame,text="Enter X Values:",padx=20, font=(" Maiandra GD",20))
	label2=Label(frame,text="Enter Y Values:",padx=20, font=(" Maiandra GD",20))
	label3=Label(frame,text="Label = :",padx=20, font=(" Maiandra GD",20))
	label4=Label(frame,text="Label = :",padx=20, font=(" Maiandra GD",20))
	
	#creating input fields
	global entry1,entry2,entry3,entry4
	entry1=Entry(frame_2 ,width=30, font=(" Maiandra GD",25))
	entry2=Entry(frame_2,width=30, font=(" Maiandra GD",25))
	entry3=Entry(frame_2,width=15 font=(" Maiandra GD",25))
	entry4=Entry(frame_2,width=15 font=(" Maiandra GD",25))

	# creating submit button to frame
	submit = Button(frame_2, text="PLOT IT", bg="green" , fg="white",  width=20, height=3, command=plotscatter)

	#adding text fields,labels and buttons in order
	label1.grid(row=0,column=0)
	entry1.grid(row=0,column=1,padx=20,pady=10)

	label3.grid(row=0,column=2)
	entry3.grid(row=0,column=3,padx=10)

	label2.grid(row=1,column=0)
	entry2.grid(row=1,column=1,padx=20,pady=10)

	label3.grid(row=1,column=2)
	entry3.grid(row=1,column=3,padx=10)

	submit.grid(row=2,column=1,pady=20)

	r1.mainloop()

def plothist():
	#frame for plot
	panel= LabelFrame(r1,text="PLOT")
	panel.pack()

	#getting input
	x= list(map(int, entry1.get().split(",")))
	y=list(map(int, entry2.get().split(",")))

	fig = Figure(figsize=(12, 7), dpi=100)
    	plot1 = fig.add_subplot(111)
    	plot1.set_xlabel(entry3.get())
    	plot1.set_ylabel(entry4.get())
    	plot1.hist(x, y)
    	canvas = FigureCanvasTkAgg(fig, master=panel)
    	canvas.draw()
    	canvas.get_tk_widget().pack()

def histplt():
	#destroying old window
	global root
	root.destroy()

	#creating new window
	global r1
	r1=Tk()
	r1.state("zoomed")

	#adding frame to window
	frame_2=LabelFrame(r1)
	frame.place(width=1920, height=480)
	frame_2.pack()

	#creating labels for input fields
	label1=Label(frame,text="Enter X Values:",padx=20, font=(" Maiandra GD",20))
	label2=Label(frame,text="Enter Y Values:",padx=20, font=(" Maiandra GD",20))
	label3=Label(frame,text="Label = :",padx=20, font=(" Maiandra GD",20))
	label4=Label(frame,text="Label = :",padx=20, font=(" Maiandra GD",20))
	
	#creating input fields
	global entry1,entry2,entry3,entry4
	entry1=Entry(frame_2 ,width=30, font=(" Maiandra GD",25))
	entry2=Entry(frame_2,width=30, font=(" Maiandra GD",25))
	entry3=Entry(frame_2,width=15 font=(" Maiandra GD",25))
	entry4=Entry(frame_2,width=15 font=(" Maiandra GD",25))

	# creating submit button to frame
	submit = Button(frame_2, text="PLOT IT", bg="green" , fg="white",  width=20, height=3, command=plothist)

	#adding text fields,labels and buttons in order
	label1.grid(row=0,column=0)
	entry1.grid(row=0,column=1,padx=20,pady=10)

	label3.grid(row=0,column=2)
	entry3.grid(row=0,column=3,padx=10)

	label2.grid(row=1,column=0)
	entry2.grid(row=1,column=1,padx=20,pady=10)

	label3.grid(row=1,column=2)
	entry3.grid(row=1,column=3,padx=10)

	submit.grid(row=2,column=1,pady=20)

	r1.mainloop()

def plotline():
	#frame for plot
	panel= LabelFrame(r1,text="PLOT")
	panel.pack()

	#getting input
	x= list(map(int, entry1.get().split(",")))

	fig = Figure(figsize=(12, 7), dpi=100)
    	plot1 = fig.add_subplot(111)
    	plot1.set_xlabel(entry3.get())
    	plot1.plot(x)
    	canvas = FigureCanvasTkAgg(fig, master=panel)
    	canvas.draw()
    	canvas.get_tk_widget().pack()

def lineplt():
	#destroying old window
	global root
	root.destroy()

	#creating new window
	global r1
	r1=Tk()
	r1.state("zoomed")

	#adding frame to window
	frame_2=LabelFrame(r1)
	frame.place(width=1920, height=480)
	frame_2.pack()

	#creating labels for input fields
	label1=Label(frame,text="Enter X Values:",padx=20, font=(" Maiandra GD",20))
	label3=Label(frame,text="Label = :",padx=20, font=(" Maiandra GD",20))
		
	#creating input fields
	global entry1,entry3,
	entry1=Entry(frame_2 ,width=30, font=(" Maiandra GD",25))
	entry3=Entry(frame_2,width=15 font=(" Maiandra GD",25))

	# creating submit button to frame
	submit = Button(frame_2, text="PLOT IT", bg="green" , fg="white",  width=20, height=3, command=plotline)

	#adding text fields,labels and buttons in order
	label1.grid(row=0,column=0)
	entry1.grid(row=0,column=1,padx=20,pady=10)

	label3.grid(row=0,column=2)
	entry3.grid(row=0,column=3,padx=10)

	submit.grid(row=2,column=1,pady=20)

	r1.mainloop()
def plotbar():
	#frame for plot
	panel= LabelFrame(r1,text="PLOT")
	panel.pack()

	#getting input
	x= list(map(int, entry1.get().split(",")))
	y=list(map(int, entry2.get().split(",")))

	fig = Figure(figsize=(12, 7), dpi=100)
    	plot1 = fig.add_subplot(111)
    	plot1.set_xlabel(entry3.get())
    	plot1.set_ylabel(entry4.get())
    	plot1.bar(x, y)
    	canvas = FigureCanvasTkAgg(fig, master=panel)
    	canvas.draw()
    	canvas.get_tk_widget().pack()

def barplt():
	#destroying old window
	global root
	root.destroy()

	#creating new window
	global r1
	r1=Tk()
	r1.state("zoomed")

	#adding frame to window
	frame_2=LabelFrame(r1)
	frame.place(width=1920, height=480)
	frame_2.pack()

	#creating labels for input fields
	label1=Label(frame,text="Enter X Values:",padx=20, font=(" Maiandra GD",20))
	label2=Label(frame,text="Enter Y Values:",padx=20, font=(" Maiandra GD",20))
	label3=Label(frame,text="Label = :",padx=20, font=(" Maiandra GD",20))
	label4=Label(frame,text="Label = :",padx=20, font=(" Maiandra GD",20))
	
	#creating input fields
	global entry1,entry2,entry3,entry4
	entry1=Entry(frame_2 ,width=30, font=(" Maiandra GD",25))
	entry2=Entry(frame_2,width=30, font=(" Maiandra GD",25))
	entry3=Entry(frame_2,width=15 font=(" Maiandra GD",25))
	entry4=Entry(frame_2,width=15 font=(" Maiandra GD",25))

	# creating submit button to frame
	submit = Button(frame_2, text="PLOT IT", bg="green" , fg="white",  width=20, height=3, command=plotscatter)

	#adding text fields,labels and buttons in order
	label1.grid(row=0,column=0)
	entry1.grid(row=0,column=1,padx=20,pady=10)

	label3.grid(row=0,column=2)
	entry3.grid(row=0,column=3,padx=10)

	label2.grid(row=1,column=0)
	entry2.grid(row=1,column=1,padx=20,pady=10)

	label3.grid(row=1,column=2)
	entry3.grid(row=1,column=3,padx=10)

	submit.grid(row=2,column=1,pady=20)

	r1.mainloop()

root= Tk()
root.state("zoomed")#for full screen

#creating a label for adding title
title=Label(root, text="Data Visualizer")
title.config(font=("Maiandra GD",44)
title.pack()

#creating a frame to add buttons
frame=LabelFrame(root,text="Plot Options",padx=100,pady=100)
frame.pack(padx=10,pady=10)

#creating Image buttons
scatter_button=Button(frame,command=scatterplt)
histogram_button=Button(frame)
pie_button=Button(frame)
line_button=Button(frame)
bar_button=Buttton(frame,command=barplt)

#creating  photos for buttons
scatter_photo=PhotoImage(file="D:/chinnu/project photos/scatter plt.png")
histogram_photo = PhotoImage(file="D:/chinnu/project photos/hist.png")
pie_photo = PhotoImage(file="D:/chinnu/project photos/pie.png")
line_photo= PhotoImage(file="D:/chinnu/project photos/lineplt.png")
bar_photo = PhotoImage(file="D:/chinnu/project photos/bar.png")

# adding photos to buttons
scatter_button.config(image=scatter_photo,width=255,height=180)
histogram_button.config(image=histogram_photo,width=255,height=180)
pie_button.config(image=pie_photo,width=255,height=180)
line_button.config(image=line_photo,width=255,height=180)
bar_button.config(image=bar_photo,width=255,height=180)

#adding buttons to grid
scatter_button.grid(row=1,column=0)
histogram_button.grid(row=1,column=2)
pie_button.grid(row=1,column=4)
line_button.grid(row=2,column=1)
bar_button.grid(row=2,column=3)

root.mainloop()




