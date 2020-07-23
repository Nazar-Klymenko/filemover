# from tkinter import *    
import tkinter as tk

# , extension, source, destination, option


class Picmover:
    # def __init__(self):
    #     self.extension = extension
    #     self.source = source
    #     self.destination = destination
    #     self.option = option
    def choose_format(self, extension):
        pass
    def please(self, option):
        print(option)  

class FrameGui:
    root = tk.Tk()
    root.iconphoto(False, tk.PhotoImage(file='./assets/folder.png'))
    Picmover().please("lollol")
    root.mainloop()



