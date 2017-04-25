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
	canvas = Canvas(fenetre, width=photo.width(), height = photo.height() + 10)
	canvas.create_image(0, 10, anchor=NW, image= photo)
	#canvas.pack()
	canvas.grid(row = 3, column = 5)
	fenetre.mainloop()

b1 = Button(text = "Choose", width = 5, height = 1)
b1.config(command = choose)
b1.pack(padx = 8, pady = 1)
b1.grid(row = 0, column = 1)


b2 = Button(text = "Run", width = 5, height = 1)
#b2.config()
#b2.pack(padx = 15, pady = 1)
b2.grid(row = 0, column = 6)

fenetre.mainloop()