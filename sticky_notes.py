from tkinter import *
import tkinter.messagebox
from random import *
import datetime


now = datetime.datetime.now()
	

def dayandnight():
	if now.strftime("%X") > '16:45:39':
		return 'black'
	elif now.strftime("%X") < '15:40:00':
		return 'white'


def dayand():
	if now.strftime("%X") > '16:45:39':
		return 'white'
	elif now.strftime("%X") < '15:40:00':
		return 'black'
	
	
def newgui():
	src = Tk()
	src.title('')
	src.geometry('400x360+100+200')
	isi = open("times.txt","a")
	isi.write("%s %s\n" % (now.strftime("%X"), str(hello.get())))
	stms = open("dailytask","a")
	time = "%b-%d/%m/%Y"
	stms.write("%s %s\n" %  (now.strftime(time), str(hello.get())))
	Label(src, text = str(hello.get())).pack()
	src.mainloop()
	

def shutdown():
	try:
		if tkinter.messagebox.askokcancel(title = "info",message = "are you sure to quit"):
			testy.destroy()
	except  Exception as ex:
		tkinter.messagebox.showinfo("Error", "cant find %s" % ex)
		
# create a app
testy = Tk()

# app title name
testy.title('Sticky Notes')

# label name

Label(testy, text = "hello").pack()
hello = Entry(testy)
hello.pack()

# button
Button(testy, text = "noteit", command = newgui).pack()
	
	
source = open("dailytask","r")

for each_item in source:
	som = Tk()
	(a,sdd) = each_item.split(' ',1)
	som.title(str(a))
	source = str(randint(700,1000))
	soe = str(randint(400,600))
	som.geometry(str('250x250+' + source + '+'+ soe))
	#dayandnight.pack(side = 'left', padx = 10, pady = 10)
	soap = Label(som, text = str(sdd),width = "10", height = "6", bg = dayandnight(), fg = dayand())
	soap.pack(side = 'left', padx = 10, pady = 10)
	x = datetime.datetime.now()
	if x.strftime("%X") > '16:30:39':
		som['bg']='black'
	elif x.strftime("%X") < '15:40:00':
		som['bg']='snow'

def kk():
	source = str(randint(700,1000))
	soe = str(randint(400,600))
	som.geometry(str('250x250+' + source + '+'+ soe))
	

def ioto(file):
	popss = open(file)
	for kk in popss:
		(s,sm) = kk.split(' ',1)
		#print(kk)
		#print(s)
		x = str("%b-%d/%m/%Y")
		smtsss = str(now.strftime(x))
		#print(s.find(str(smtsss)))
		y = s.find(smtsss)
		if y == 0:
			return ("you are already written some task")
		else:
			return ("write some task & be active")
		
#load for particular date
Label(testy, text = ioto("dailytask")).pack()
sou = StringVar()
sou.set(None)


testy.protocol("WM_DELETE_WINDOW",shutdown)

# full app
som.mainloop()
testy.mainloop()
