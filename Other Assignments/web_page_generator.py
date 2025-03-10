import tkinter as tk
from tkinter import *
import webbrowser

#Create child class from tkinter Frame parent
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        #Create a Label to prompt user to input text or click default button
        self.txtLbl = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.txtLbl.grid(row=0, column=0, padx=(10,0))

        #Provide text box where user can type custom text
        self.inputTxt = Entry(self.master, width=125)
        self.inputTxt.grid(row=1, column=0, columnspan=4, padx=(15,0), pady=(10,0), sticky=W)

        #Create a button that will generate a default webpage
        self.btnDef = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btnDef.grid(row=2, column=2, padx=(10,10), pady=(10,10))

        #Create a button that will generate a webpage using the user's inputted text
        self.btnCustom = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btnCustom.grid(row=2, column=3, padx=(10,10), pady=(10,10))

        

    #Create a function that will open a default webpage in a new tab
    def defaultHTML(self):
        #Set default text for webpage
        htmlText = "Stay tuned for our amazing summer sale!"
        #Create an html file
        htmlFile = open("index.html", "w")
        #Set content for the html file
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        #Write the content in the html file
        htmlFile.write(htmlContent)
        #Close the html file
        htmlFile.close()
        #Open the default html webpage in a new tab in the web browser
        webbrowser.open_new_tab("index.html")

    #Create a function that will open a custom text webpage in a new tab
    def customHTML(self):
        #Get user's input and set as text for webpage
        htmlText = self.inputTxt.get()
        #Create an html file
        htmlFile = open("index.html", "w")
        #Set content for the html file
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        #Write the content in the html file
        htmlFile.write(htmlContent)
        #Close the html file
        htmlFile.close()
        #Open the custom html webpage in a new tab in the web browser
        webbrowser.open_new_tab("index.html")
 



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
