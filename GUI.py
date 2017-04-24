import sys
import Tkinter as tk
import tkFileDialog as filedialog
from PIL import Image, ImageTk
from PyQt4 import QtGui


class window(QtGui.QWidget):
    
    def __init__(self):
        super(window, self).__init__()
        
        self.initUI()
        
    def choose(event):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title = "Selectionez une image", filetypes = [('png files','.png'),('all files','.*')])
        image1 = tk.PhotoImage(file = file_path)
        return image1
        

    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('Presiona <b>Run</b> para lanzar el programa')
        
        btn = QtGui.QPushButton('Open', self)
        btn.setToolTip('Appuyez <b>Open</b> pour charger une empreinte digitale')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)  
        img = btn.clicked.connect(self.choose)        

        while(img != None):
            canvas = tk.Canvas(root,width=img.width(),height=img.height())
            canvas.create_image(0,0,anchor='nw',image = img)
            canvas.pack()

        btn = QtGui.QPushButton('Run', self)
        btn.setToolTip("Appuyez <b>Run</b> pour lancer l'algorithme")
        btn.resize(btn.sizeHint())
        btn.move(150, 50)
        
        self.setGeometry(1500, 400, 800, 500)
        self.setWindowTitle("SYSTEME DE RECONNAISSANCE D'EMPREINTES DIGITALES")    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()