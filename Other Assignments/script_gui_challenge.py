
import tkinter
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Check files')
        self.master.config(bg='lightgray')

        self.varFile1 = StringVar()
        self.varFile2 = StringVar()

        self.btnBrowse1 = Button(self.master, text='Browse...', width=10, height=2, command=self.browseOne)
        self.btnBrowse1.grid(row=0, column=0, padx=(0,0), pady=(35,0), sticky=W)

        self.btnBrowse2 = Button(self.master, text='Browse...', width=10, height=2, command=self.browseTwo)
        self.btnBrowse2.grid(row=1, column=0, padx=(0,0), pady=(35,0), sticky=W)

        self.txtFile1 = Text(self.master, height=1, width=35, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFile1.grid(row=0, column=1, sticky=W)
        
        self.txtFile2 = Text(self.master, height=1, width=35, font=("Helvetic", 16), fg='black', bg='lightblue')
        self.txtFile2.grid(row=1, column=1, sticky=W)

        self.btnCheck = Button(self.master, text='Check for files...', width=10, height=2, command=self.check)
        self.btnCheck.grid(row=3, column=0, padx=(35,0), pady=(35,0), sticky=W)

        self.btnClose = Button(self.master, text='Close Program', width=10, height=2, command=self.close)
        self.btnClose.grid(row=3, column=4, padx=(35,0), pady=(35,0), sticky=W)


    

        
    def browseOne(self):
        path = filedialog.askdirectory()
        self.txtFile1.insert('1.0', path)
        print(path)

    def browseTwo(self):
        path = filedialog.askdirectory()
        self.txtFile2.insert('1.0', path)
        print(path)
        
    def check(self):
        checkPath = filedialog.askdirectory()
        print(checkPath)
        pathCopy1 = self.txtFile1.get('1.0', 'end').strip()
        print(pathCopy1)
        pathCopy2 = self.txtFile2.get('1.0', 'end').strip()
        print(pathCopy2)
        

        if len(pathCopy1) == 0 or len(pathCopy2) == 0:
            showinfo(title='Error', message='Please provide two paths to check.')
        elif pathCopy1 == checkPath:
            showinfo(title='Match!', message='Path #1 matches the path selected.')
        elif pathCopy2 == checkPath:
            showinfo(title='Match!', message='Path #2 matched the path selected.')
        else:
            showinfo(title='Error', message='No provided path matches the selected path.')
       
            
        

    def close(self):
        self.master.destroy()



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()    
