# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:40:57 2017

@author: bchassagno
"""
import tkinter as tk
class Comparaison(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.setwidgets()     
    
    def setwidgets(self):
        # Création de nos widgets
        self.bouton_cliquer = tk.Button(self, text="Cancel", fg="red", command=self.destroy, bg="blue")        
        self.b1 = tk.Button(self,text = "how do we calculate it?")              
       
        
        #disposition des widgets
        self.bouton_cliquer.grid(row = 0, column = 1,padx=5)
        self.b1.grid(row = 0, column = 2,padx =5)
        self.can1 = tk.Canvas(self, width =480, height =700, bg ='white')
        self.can1.grid(row =1, column =1, columnspan = 2, padx =5, pady =5)
        

       
        
