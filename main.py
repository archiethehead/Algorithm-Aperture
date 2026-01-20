import tkinter as tk
from tkinter import ttk
from algorithms import sorting, search, dynamic_programming, encryption

#Singleton pattern, creational design pattern
class state_manager():

    instance = None

    def __new__(self):
        if self.instance is None:
            self.instance = super(state_manager, self).__new__(self)
            self.instance.facacde = None
            self.ascending = True

        return self.instance
    
    def get_ascending(self):
        return self.ascending
    
    def set_ascending(self):
        self.ascending = not self.ascending
    
class sort_strategy():
    def __init__()


class algorithm_aperture():
    def __init__(self):
        self.screen = screen
        self.manager = state_manager()

        self.ascending_toggle = None
        self.execute_button = None
        self.ascending_text = ["Descending", "Ascending"]

        self.data_entry = None
        self.combobox = None
        self.text_box = None
    
    def set_ascending_button(self):
        self.manager.set_ascending()
        self.ascending_toggle.config(text=self.ascending_text[self.manager.get_ascending()])

    def create_window(self):
        screen.geometry("640x480")
        screen.resizable(0,0)
        screen.title("Algorithm Aperture")
        main_frame = tk.Frame(width = 1150, height = 690, bg = "#7b2182")
        main_frame.pack()
        
        self.ascending_toggle = tk.Button(text = "Ascending", command = self.set_ascending_button)
        self.ascending_toggle.place(x=0,y=125)

        self.data_entry = tk.Entry(width = 30)
        self.data_entry.place(x=0,y=80)
        data_entry_lbl = tk.Label(text="Data Entry (insert arrays in the [n, x, y] pattern, and single values as n)")
        data_entry_lbl.place(x=0,y=59)

        self.combobox = ttk.Combobox(screen)
        self.combobox.place(x=0,y=170)
        self.combobox['values'] = ('Selection Sort',
                                   'Bubble Sort',
                                   'Merge Sort',
                                   'Card Shuffle',
                                   'Factorial',
                                   'Fibonacci',
                                   'Search',
                                   'RSA',
                                   'Palindrome')
        self.combobox.current(0)

        self.execute_button = tk.Button(text = "Execute")
        self.execute_button.place(x=0,y=195)

        self.text_box = tk.Listbox(width = "164", height = "30", background = "#ffffff",
                                   font = ("Courier new",10), selectmode = "single")
        self.text_box.insert(0,"Output: ")
        self.text_box.place(x = 0, y = 250)

    def clear_window(self):
        for widgets in screen.winfo_children():
            widgets.destroy()
        self.create_window()

screen = tk.Tk()
window = algorithm_aperture()
window.create_window()
screen.mainloop()