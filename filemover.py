import tkinter as tk
#        self.files_found = 0


class Filemover:
    def __init__(self):
        pass

    def choose_extension(self, chosen_extension):
        self.extension = chosen_extension

    def choose_option(self, chosen_option):
        self.file_option = chosen_option

    def choose_source(self, chosen_source):
        self.source = chosen_source

    def choose_destination(self, chosen_destination):
        self.destination = chosen_destination

    def value_hub(self):
        pass

    def move_files(self):
        print(self.extension)
        print(self.file_option)

        # print(f"{option} {extension} files from:\n{source}\n to:\n {destination}")s


class FrameGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Filemover")
        self.root.iconphoto(False, tk.PhotoImage(file='./assets/folder.png'))
        # self.root.geometry('900x450')
        self.root.minsize(300, 300)
        self.main_state = Buttons()
        Options(root=self.root, state=self.main_state)
        Extensions(state=self.main_state)
        # Source(state=self.main_state)
        # Destination(state=self.main_state)
        self.root.mainloop()


class Extensions:
    def __init__(self, state=None):
        self.state = state
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

    def checkbox_value(self):
        checkboxes_selected = []
        for _ext in self.avaliable_extensions:
            checkboxes_selected.append(_ext.get())
        result = [x for x, y in zip(
            self.extension_names, checkboxes_selected) if y == True]
        self.state.extension = result

    def create_checkboxes(self):
        cn = 0
        for C in self.avaliable_extensions:
            C = tk.Checkbutton(text=self.extension_names[cn], variable=self.avaliable_extensions[cn], anchor="nw",
                               onvalue=1, offvalue=0, height=1, width=5, padx=14, command=self.checkbox_value)
            C.grid(row=cn, column=1)
            cn += 1


class Options:
    def __init__(self, root=None, state=None):
        self.root = root
        self.state = state
        self.option = tk.StringVar()
        self.dropdown()

    def send_option(self, selectx):
        self.state.file_option = selectx

    def dropdown(self):
        W = tk.OptionMenu(self.root, self.option,
                          "Copy to", "Move to", "Delete", command=self.send_option)
        self.option.set("Choose option")
        W.grid(row=1, column=2)


class Source:
    def __init__(self, state=None):
        self.state = state
    pass


class Destination:
    def __init__(self, state=None):
        self.state = state
    pass


class Buttons:
    def __init__(self):
        self.extension = []
        self.source = False
        self.destination = False
        self.file_option = "Not chosen"
        self.create_buttons()

    def check_state(self):
        print(self.extension)
        print(self.file_option)

    def check_state_elaborate(self):
        if self.extension != [] and self.file_option == "Not chosen":
            print("choose file option")
        elif self.file_option == "Not chosen" and self.extension == []:
            print("choose file option and file extension")
        elif self.file_option != "Not chosen" and self.extension == []:
            print("choose file extension")
        elif self.file_option != "Not chosen" and self.extension != []:
            print(self.extension)
            print(self.file_option)

    def create_buttons(self):
        B1 = tk.Button(text="Start", command=self.check_state_elaborate)
        B1.grid(row=12, column=1, padx=14, sticky=tk.W+tk.S)


if __name__ == '__main__':
    FrameGui()
