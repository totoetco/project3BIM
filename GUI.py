#!/usr/bin/env python
# -*- coding: utf-8
 
import os
import tkinter as tk 
import tkinter.filedialog as fdg
from affichagecomparaison import Comparaison

class Entreejeu(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.setmenu()
        self.setwidgets()
        
        
        
    def add(self):          
        
        filepath = fdg.askopenfilename(title = "Selectionez une image", filetypes = [('png files','.png'),('all files','.*')])        
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
            selection=self.liste.get(self.liste.curselection())
            affichagedonnes=Comparaison(listedonnes,selection,master=fenetre3)
            affichagedonnes.mainloop()
            
            

    def delete(self):
        print("element supprime est le suivant")
        print(self.liste.curselection())
        for i in self.liste.curselection():
            self.liste.delete(i)
               
    def reset(self):
        self.liste.delete(0, tk.END)
        print(tk.END)

    def read_db(self):
    #Variable du repertoire A REMPLACER !
        self.path = '/home/cdelgadodi/Documents/Projet/Empreintes/Noir-blanc/600ppp/'
    #Liste vide pour inclure tous les fichiers
        self.lstFiles = []
    #Liste avec tous les fichiers du repertoire:
        self.lstDir = os.walk(path)   #os.walk()Liste repertoires et fichiers
    #CRee une liste des fichiers bmp qui existent dans le repertoire et les inclut dans la liste.
        for root, dirs, files in lstDir:
            for fichier in files:
                (nomFichier, extension) = os.path.splitext(fichier)
                if(extension == ".bmp"):
                    lstFiles.append(nomFichier+extension)
                #print (nomFichier + extension)
        print(lstFiles)            
        print "taille de la liste = ", len(lstFiles)
        return lstFiles

    def algo(self, s1):
    for img in read_db():
        if self.s1 == img:
            print self.s1 + " avec " + img
            print True
        else:
            print self.s1 + " avec " + img
            print False
        
    def compare(self):
        print("la taille est de")
        print(self.liste.size())
        
        if (len(self.liste.curselection())!=2):
              fenetre2=tk.Toplevel()      
              fenetre2.grab_set()
              fenetre2.master.title("erreur saisie")
              message=tk.Message(fenetre2,text="veuillez ne sélectionner que 2 éléments à la fois",aspect=200,fg="red",bg="white")
              message.pack()
              fenetre2.mainloop()
        else:
            
            self.image1=tk.PhotoImage(file =self.liste.get(self.liste.curselection()[0]))
            self.image2=tk.PhotoImage(file =self.liste.get(self.liste.curselection()[1]))
            self.item1 = self.can1.create_image((int)(self.can1.cget('width'))/2, (int)(self.can1.cget('height'))/2, image =self.image1)
            self.item2 = self.can2.create_image((int)(self.can1.cget('width'))/2, (int)(self.can1.cget('height'))/2, image =self.image2)        
       
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
        fichierempreintedigitale = open("fingerprint.txt", "a")
        
        fichierempreintedigitale.close()
    
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
        
        
        self.master.config(menu=self.menubar)
        
    def selectionfin(self,filename):                
        b=filename.split("/")
        return (b[len(b)-1])

      
        
fenetre = tk.Tk()
fenetre.title("SYSTEME DE RECONNAISSANCE D'EMPREINTES DIGITALES")
fenetre.geometry('1000x400')
fenetre.resizable(width=False, height=False)
debutjeu=Entreejeu(master=fenetre)

debutjeu.mainloop()
