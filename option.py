from tkinter import *

Option= Tk()
Option.title("Option")
Option.geometry("300x500")

def clickedLogout():	
	Option.destroy()
	import login
	#####
Logout = Button (Option,text="Logout",command=clickedLogout)
Logout.place(x=1,y=1)