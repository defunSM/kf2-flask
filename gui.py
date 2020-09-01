import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

from getMutatorInfo import getWorkShopInfo
from getId import getWorkShopId

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        s = ttk.Style()
        # print(s.theme_names())
        s.theme_use('winnative')

        self.master = master
        self.pack()
        self.create_widgets()
        self.ROW_NUMBER = 3

    def create_widgets(self):

        self.label = tk.Label(self, text="Workshop ID/URL: ", font=tkFont.Font(family="Lucida Grande", size=12))
        self.label.grid(row=1, column=0, columnspan=1, sticky=tk.W)
        
        self.entry = tk.Entry(self)
        self.entry.grid(row=2, column=0)


        self.search = tk.Button(self)
        self.search["text"] = "Search"
        self.search["command"] = self.searchForId
        self.search.grid(row=2, column=1, sticky=tk.W)

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.grid(row=4, columnspan=4)

        self.pack()

    def searchForId(self):

        id = getWorkShopId(self.entry.get())
        name, size, date = getWorkShopInfo(id)
        print(id)
        print(name)
        print(size)
        print(date)

        mutatorLabel = name + ' (' + size + ') '
        

        self.new_progress_bar = tk.ttk.Progressbar(self)
        self.new_progress_bar.grid(row=self.ROW_NUMBER, column=6, padx=3)

        self.remove_mod = tk.Button(self, text="Remove")
        self.remove_mod.grid(row=self.ROW_NUMBER, column=5)

        self.new_button = tk.Button(self, text="Download")
        self.new_button.grid(row=self.ROW_NUMBER, column=4)

        self.mod_label = tk.Label(self, text=mutatorLabel)
        self.mod_label.grid(row=self.ROW_NUMBER, column=3, sticky=tk.W)

        self.new_checkbox = tk.Checkbutton(self)
        self.new_checkbox.grid(row=self.ROW_NUMBER, column=2, sticky=tk.E)

        self.pack()
        self.ROW_NUMBER += 1
        
root = tk.Tk()
app = Application(master=root)
app.master.title("KF2 Mod Manager")
app.mainloop()