from Core import *
from tkinter import *

#window Instance

root = Tk()

#Window Title
root.title ('Covid Tracker')

#Window Generation

root.geometry("630x480")
root.configure(background='#00B2EE')
root.resizable(width=False, height=False)

# This is the section of code which creates the a label

Label(root, text='Covid Tracker', bg='#789ac7', font=('verdana', 48, 'bold')).place(x=65, y=52)

#GUI SECTION

tCPlotButton = Button(root, text="Click here for total cases in the Philippines as a Graph", command = Function.totalCasesPlot,bg = '#7e78c7', fg ='white')
totalCasesBtn = Button(root, text = "Total number of Cases in the Philippines", command = Function.totalCases,bg = '#7e78c7', fg ='white')
totalTestedBtn = Button(root, text = "Total number of people Tested in the Philippines", command = Function.totalTested,bg = '#7e78c7', fg ='white')
newestCasesBtn = Button(root, text = "Newest Cases in the Philippines", command = Function.newestCases,bg = '#7e78c7', fg ='white')

#Button Placements

newestCasesBtn.place(x=225, y=190)

totalCasesBtn.place(x=202, y=240)

totalTestedBtn.place(x=181, y=290)

tCPlotButton.place(x=168, y=340)


#Quit Button

button_quit = Button(root, text="Quit Program", command=root.quit,bg = '#7e78c7',fg='white')
button_quit.place(x=265, y=400)

#change color of Background

root['background']='#789ac7'

#Tkinter stuff
root.mainloop()





