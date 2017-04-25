from Tkinter import * 
import tkFileDialog as filedialog
import tkFont
import Image

fenetre = Tk()
fenetre.title("SYSTEME DE RECONNAISSANCE D'EMPREINTES DIGITALES")
fenetre.geometry('600x400')

def choose():
	filepath = filedialog.askopenfilename(title = "Selectionez une image", filetypes = [('png files','.png'),('all files','.*')])
	img = PhotoImage(file=filepath)
	photo = img.subsample(4,4)
	canvas = Canvas(fenetre, width=photo.width(), height = photo.height() + 15)
	canvas.create_image(0, 15, anchor=NW, image= photo)
	canvas.pack()
	#canvas.grid(row = 3, column = 1, columnspan = 2)
	fenetre.mainloop()

b1 = Button(text = "Choose a fingerprint", width = 14, height = 1)
b1.config(command = choose)
b1.pack(side='left', anchor='s')
#b1.grid(row = 0, column = 8, columnspan = 1)


b2 = Button(text = "Run", width = 5, height = 1)
#b2.config()
b2.pack(side='bottom', anchor='w')
#b2.grid(row = 0, column = 9, columnspan = 1)

fenetre.mainloop()