import tkinter as tk

class Filemover:
    def __init__(self):
        self.extension = []
        self.source = False
        self.destination = False
        self.option = False
    def move_files(self):
        print(self.extension)
        # print(f"{option} {extension} files from:\n{source}\n to:\n {destination}")s
  
class FrameGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Filemover")
        self.root.iconphoto(False, tk.PhotoImage(file='./assets/folder.png'))
        self.root.geometry('900x450')
        Extensions()
        self.root.mainloop()

        
class Extensions(Filemover):
    def __init__(self):
        self.check_PNG = tk.BooleanVar()
        self.check_JPG = tk.BooleanVar()
        self.check_GIF = tk.BooleanVar()
        self.check_PSD = tk.BooleanVar()
        self.check_MP3 = tk.BooleanVar()
        self.check_WAV = tk.BooleanVar()
        self.check_ZIP = tk.BooleanVar()
        self.check_RAR = tk.BooleanVar()
        self.check_DOC = tk.BooleanVar()
        self.check_XLS = tk.BooleanVar()
        self.check_PDF = tk.BooleanVar()
        self.avaliable_extensions=[self.check_PNG,
            self.check_JPG,
            self.check_GIF,
            self.check_PSD,
            self.check_MP3,
            self.check_WAV,
            self.check_ZIP,
            self.check_RAR,
            self.check_DOC,
            self.check_XLS,
            self.check_PDF]
        self.extension_names=["PNG","JPG","GIF","PSD","MP3","WAV","ZIP","RAR","DOC","XLS","PDF"]
        self.files_found = 0
        self.create_checkboxes()
        self.create_buttons()


    def choose_extension(self, chosen_extension):
        Filemover.extension = chosen_extension
    def choose_option(self, chosen_option):
        Filemover.option = chosen_option
    def choose_source(self, chosen_option):
        Filemover.source = chosen_option
    def choose_destination(self, chosen_destination):
        Filemover.destination = chosen_destination

    def create_checkboxes(self):
        cn = 0
        for ext in self.avaliable_extensions:
            C = tk.Checkbutton(text = self.extension_names[cn], variable = self.avaliable_extensions[cn], anchor = "nw",  onvalue = 1,
                offvalue = 0, height=1, width=5)
            C.pack()
            cn +=1

    def checkbox_value(self):
        checkboxes_selected = []
        for _ext in self.avaliable_extensions:
            checkboxes_selected.append(_ext.get())
        result = [x for x, y in zip(self.extension_names, checkboxes_selected) if y == True]
        if result==[]:
            #create a pop up
            print("please select file formats")
        elif result!=[]:
            fm=Filemover()
            fm.extension = result
            fm.move_files()
            print(result)

    def create_buttons(self):
        B1 = tk.Button(text="Start", anchor = "nw",command=self.checkbox_value)
        B1.pack()


if __name__== '__main__':
    FrameGui()
