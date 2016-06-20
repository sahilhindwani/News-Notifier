from Tkinter import *
import webbrowser

class Notification():
	w = 400
	h = 100
	bgColor = '#77216F'

	def __init__(self,*link):
		self.url=link[0]
		self.root = Tk()
		self.root.overrideredirect(1)
		self.root.configure(bg=self.bgColor)
		ws = self.root.winfo_screenwidth()  
		hs = self.root.winfo_screenheight() 
		self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, ws - self.w - 25, 40))
        
		self.label = Label(self.root, text=link[1], fg='#ffffff', bg=self.bgColor, wraplength=350)
		self.label.pack(pady=20)
		self.label.bind("<Double-Button-1>", self.bopen)

		self.bQuit = Button(self.root, text="X", command=self.closeSelf)
		self.bQuit.configure(background = '#77216F')    # configure background of the button
		self.bQuit.place(x=375, y=0, height=25, width=25)

		self.options = Button(self.root, text="NewsSelect", command=self.showoptions)
		self.options.configure(background = '#77216F')    # configure background of the button
		self.options.place(x=0, y=0, height=25, width=100)

		self.root.after(7500, lambda: self.root.destroy())  # close popup after 7500 second itself
		self.root.lift()
		self.root.call('wm', 'attributes', '.', '-topmost', True)   # so that window is always topmost
		self.root.mainloop()

	def closeSelf(self):        # closes the popup
		self.root.destroy()

	def bopen(self, event):     # open the url in default webbrowser
		webbrowser.open(self.url)
 		self.closeSelf()

 	def showoptions(self):
 		self.root.destroy()
 		cview=NewsSelector()
 		self.c1=cview.c1
 		self.c2=cview.c2

 	def get_c1_and_c2(self):
 		return [self.c1,self.c2]


class NewsSelector():

	w = 400
	h = 100
	bgColor = '#77216F'

	def __init__(self):
		self.root=Tk()
		self.root.title('Select news source')
		self.root.configure()
		ws = self.root.winfo_screenwidth()  
		hs = self.root.winfo_screenheight()
		self.c1=IntVar() 
		self.checkbox1=Checkbutton(self.root,text='techcrunch',variable = self.c1)
		self.checkbox1.place(x=0,y=20)

		self.c2=IntVar()
		self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, ws - self.w - 25, 40))
		self.checkbox2=Checkbutton(self.root,text='Cnet',variable=self.c2)
		self.checkbox2.place(x=0,y=40)

		self.bQuit = Button(self.root, text="Submit", command=self.closeSelf)
		self.bQuit.configure(background = '#77216F')    # configure background of the button
		self.bQuit.place(x=150, y=50, height=25)

		self.root.lift()
		self.root.call('wm', 'attributes', '.', '-topmost', True)   # so that window is always topmost
		self.root.mainloop()


	def closeSelf(self):        # closes the popup
		self.root.destroy()



