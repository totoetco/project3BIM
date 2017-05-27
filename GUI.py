# -*- coding: utf-8 -*-
import tkinter as tk 
import tkinter.filedialog as fdg
from affichagecomparaison import Comparaison
from PIL import Image, ImageTk
import time
import random


class Entreejeu(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.setmenu()
        self.setwidgets()
        self.database=[]
        self.photoavant=True
        self.arret=True
        
        
        
    def add(self):          
        
        filepath = fdg.askopenfilename(title = "Selectionnez une image", filetypes = [('all files','.*')])       
         
        if (filepath not in self.database and len(filepath)!=0):
            self.database.append(filepath)
            self.liste.insert(tk.END,self.selectionfin(filepath))
        
        
    def run(self):
        
        if (len(self.liste.curselection())!=1):
              fenetre2=tk.Toplevel()      
              fenetre2.grab_set()
              fenetre2.master.title("erreur saisie")
              message=tk.Message(fenetre2,text="veuillez ne sélectionner qu'une seule image, à comparer avec toutes les autres images",aspect=200,fg="red",bg="white")
              message.pack()
              fenetre2.mainloop()
        else:
            fenetre3=tk.Toplevel()
            fenetre3.grab_set()
            fenetre3.title("COMPARISON AMONG FINGERPRINTS")
            fenetre3.geometry('400x600')
            fenetre3.resizable(width=False, height=False)
            listedonnes = list(self.liste.get(0, tk.END))        
            selection=self.database[self.liste.curselection()[0]]
            affichagedonnes=Comparaison(listedonnes,selection,master=fenetre3)
            affichagedonnes.mainloop()
            
     
        
    def delete(self):
        
        
        selection=self.liste.curselection()
        iteration=0
        #fonction pour s'assurer den pas sortir de la selection
        for i in range(len(selection)):      
            self.liste.delete(selection[i]-iteration)
            del self.database[selection[i]-iteration]
            iteration+=1
               
    def reset(self):
        self.liste.delete(0, tk.END)
        del(self.database[:])        
        self.Arreter()               
                
        self.can1.delete(tk.ALL)
        self.can2.delete(tk.ALL)
        
    def load(self):
        with open("fingerprint.txt", "r") as fichierempreintedigitale:
            data=fichierempreintedigitale.readlines()
            
            for ligne in data:               
                if (ligne not in self.database):                                        
                    self.database.append(ligne[0:len(ligne)-1])
                    self.liste.insert(tk.END,self.selectionfin(ligne))
                    
            
        
    def compare(self):
       
        
        if (len(self.liste.curselection())!=2):
              fenetre2=tk.Toplevel()      
              fenetre2.grab_set()
              fenetre2.master.title("erreur saisie")
              message=tk.Message(fenetre2,text="veuillez ne sélectionner que 2 éléments à la fois",aspect=200,fg="red",bg="white")
              message.pack()
              fenetre2.mainloop()
        else:
            
            #☻self.image1=tk.PhotoImage(file =self.database[self.liste.curselection()[0]])
           # self.image2=tk.PhotoImage(file =self.database[self.liste.curselection()[1]])
            self.image1 = Image.open(self.database[self.liste.curselection()[0]])
            largeur=(int)(self.can1.cget('width'))
            hauteur=(int)(self.can1.cget('height'))
            self.image1.resize((largeur,hauteur))            
            self.photo1 = ImageTk.PhotoImage(self.image1)            
            
            self.image2 = Image.open(self.database[self.liste.curselection()[1]])
            self.image2.resize((largeur,hauteur)) 
            self.photo2 = ImageTk.PhotoImage(self.image2)           
            
            self.item1 = self.can1.create_image((int)(self.can1.cget('width'))/2, (int)(self.can1.cget('height'))/2, image =self.photo1)
            self.item2 = self.can2.create_image((int)(self.can1.cget('width'))/2, (int)(self.can1.cget('height'))/2, image =self.photo2)        
       
    def setwidgets(self):
        # Création de nos widgets
        self.bouton_cliquer = tk.Button(self, text="Leave", fg="red", command=fenetre.destroy, bg="blue")        
        self.b1 = tk.Button(self,text = "add fingerprint",command =self.add)  
        self.b2 = tk.Button(self,text = "Compare 2 pictures",command=self.compare) 
        self.b3 = tk.Button(self,text = "RUN",command=self.run)
        self.b4 = tk.Button(self,text = "remove fingerprint",command =self.delete)  
        self.b5 = tk.Button(self,text = "reset",command =self.reset)  
        self.can1 = tk.Canvas(self, width =300, height =300, bg ='white')
        self.can2 = tk.Canvas(self, width =300, height =300, bg ='white')
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.liste=tk.Listbox(self,selectmode=tk.MULTIPLE ,width =50,yscrollcommand=self.scrollbar.set,height=5)
        self.scrollbar.config(command=self.liste.yview)
        
        
      
        
        #disposition des widgets
        self.bouton_cliquer.grid(row = 0, column = 1,padx=5)
        
        self.b2.grid(row = 0, column = 3, columnspan = 1,padx=5) 
        self.b3.grid(row = 0, column = 4, columnspan = 1,padx=5)
        self.can1.grid(row =1, column =1, columnspan = 2, padx =5, pady =5)
        self.can2.grid(row =1, column =3, columnspan = 2, padx =5, pady =5)
        self.scrollbar.grid(row=1,column=5,padx=3)
        self.liste.grid(row = 1, column = 6, columnspan = 1,padx=5)
        self.b1.grid(row = 2, column = 1,padx =5)
        self.b4.grid(row = 2, column = 2,padx =5)
        self.b5.grid(row = 2, column = 3,padx =5)
    
    def save(self):
        #verification pour ne pas ajouter denouveaux fichiers
        
        with open("fingerprint.txt", "r") as fichierempreintedigitale:
            data=fichierempreintedigitale.readlines()
        base=[]
        for ligne in data:
                print(ligne)            
                base.append(ligne)
        
                         
        with open("fingerprint.txt", "a") as fichierempreintedigitale:
            for index, item in enumerate(self.database):
                if item not in base:
                    fichierempreintedigitale.write(item+"\n")  
                    
        with open("fingerprint.txt", "r") as fichierempreintedigitale:
            data=fichierempreintedigitale.readlines()
        base=[]
        for ligne in data:
                print(ligne)            
                base.append(ligne)
        
        
    def erase(self):
        with open("fingerprint.txt", "w") as fichierempreintedigitale:            
                fichierempreintedigitale.write("") 
    
    def setmenu(self):
        self.menubar = tk.Menu(self)
        
        self.menu1 = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Update database", menu=self.menu1)        
        self.menu1.add_command(label="add", command=self.add)
        self.menu1.add_command(label="remove", command=self.delete)
        self.menu1.add_separator()
        self.menu1.add_command(label="reset", command=self.reset)
        
        self.menu2 = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="fichier", menu=self.menu2)        
        self.menu2.add_command(label="quit", command=self.master.destroy)
        self.menu2.add_command(label="save", command=self.save)
        self.menu2.add_command(label="load", command=self.load)
        self.menu2.add_command(label="erase", command=self.erase)
        
        self.menu3 = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="animate", menu=self.menu3)        
        self.menu3.add_command(label="start", command=self.Demarrer)
        self.menu3.add_command(label="stop", command=self.Arreter)        
        
        self.master.config(menu=self.menubar)
        
    def selectionfin(self,filename):                
        b=filename.split("/")
        #return os.path.basename(filename) 
        return (b[len(b)-1])
    
    def Arreter(self):
        
        self.arret = True

    def Demarrer(self):    
        
        self.can1.delete(tk.ALL)                       
        
        if self.arret == True:
            self.arret = False
            self.animepictures()
    
    def animepictures(self):
        if self.arret == False:          
            self.after(4000,self.animepictures)    
        
        self.photoavant=not(self.photoavant)
        self.can1.delete(tk.ALL) 
        if (self.photoavant):            
            self.item1 = self.can1.create_image((int)(self.can1.cget('width'))/2, (int)(self.can1.cget('height'))/2, image =self.photo1)
        else:
            self.item2 = self.can1.create_image((int)(self.can1.cget('width'))/2, (int)(self.can1.cget('height'))/2, image =self.photo2)
        
        
       
        
            
            

      
        
fenetre = tk.Tk()
fenetre.title("SYSTEME DE RECONNAISSANCE D'EMPREINTES DIGITALES")
fenetre.geometry('1000x400')
fenetre.resizable(width=False, height=False)
Arret=True
debutjeu=Entreejeu(master=fenetre)


debutjeu.mainloop()
