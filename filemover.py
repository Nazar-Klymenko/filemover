import tkinter as tk
#        self.files_found = 0
# ---------------------------------------------------


class Filemover:
    def __init__(self):
        self.extension = []
        self.source = False
        self.destination = False
        self.file_option = "Copy to"

    def choose_extension(self, chosen_extension):
        self.extension = chosen_extension

    def choose_option(self, chosen_option):
        self.file_option = chosen_option
        print(self.file_option)

    def choose_source(self, chosen_source):
        self.source = chosen_source

    def choose_destination(self, chosen_destination):
        self.destination = chosen_destination

    def value_hub(self):
        pass

    def move_files(self):
        # print(self.extension)
        print(self.file_option)

        # print(f"{option} {extension} files from:\n{source}\n to:\n {destination}")s


class FrameGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Filemover")
        self.root.iconphoto(False, tk.PhotoImage(file='./assets/folder.png'))
        # self.root.geometry('900x450')
        self.root.minsize(300, 300)
        Options(root=self.root)
        Extensions()
        Buttons()
        # Source()
        # Destination
        self.root.mainloop()


class Extensions:
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
        self.avaliable_extensions = [self.check_PNG,
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
        self.extension_names = ["PNG", "JPG", "GIF", "PSD",
                                "MP3", "WAV", "ZIP", "RAR", "DOC", "XLS", "PDF"]
        self.create_checkboxes()

    def create_checkboxes(self):
        cn = 0
        for C in self.avaliable_extensions:
            C = tk.Checkbutton(text=self.extension_names[cn], variable=self.avaliable_extensions[cn], anchor="nw",
                               onvalue=1, offvalue=0, height=1, width=5, padx=14)
            C.grid(row=cn, column=1)
            cn += 1

    def checkbox_value(self):
        checkboxes_selected = []
        for _ext in self.avaliable_extensions:
            checkboxes_selected.append(_ext.get())
        result = [x for x, y in zip(
            self.extension_names, checkboxes_selected) if y == True]
        if result == []:
            # create a pop up
            print("please select at least one file format")
        elif result != []:
            # fm = Filemover()
            Filemover().choose_extension(result)
            Filemover().move_files()


class Finalizer:
    pass


class Options():
    def __init__(self, root=None):
        self.root = root
        self.roption = tk.StringVar()
        self.avaliable_options = ["Copy to", "Move to", "Delete"]
        self.dropdown()

    def callback(self, selection):
        # fm = Filemover()
        Filemover().choose_option(selection)
        print(selection)
        # print(selection)

    def dropdown(self):
        W = tk.OptionMenu(self.root, self.roption,
                          *self.avaliable_options, command=self.callback)
        self.roption.set(self.avaliable_options[0])  # def val
        W.grid(row=1, column=2)


class Buttons:
    def __init__(self):
        self.create_buttons()

    def create_buttons(self):
        B1 = tk.Button(text="Start", command=Extensions().checkbox_value)
        B1.grid(row=12, column=1, padx=14, sticky=tk.W+tk.S)


if __name__ == '__main__':
    FrameGui()
