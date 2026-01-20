import tkinter as tk
from tkinter import ttk
from algorithms import sorting, search, dynamic_programming, encryption, brute_force, randomised
from algorithms import search, recursion

#Singleton pattern, creational design pattern
class state_manager():

    instance = None

    def __new__(self):
        if self.instance is None:
            self.instance = super(state_manager, self).__new__(self)
            self.instance.facade = algorithm_facade()
            self.instance.ascending = True
            self.instance.encrypting = True

        return self.instance
    
    def get_ascending(self):
        return self.instance.ascending
    
    def set_ascending(self):
        self.instance.ascending = not self.instance.ascending

    def get_encrypting(self):
        return self.instance.encrypting

    def set_encypting(self):
        self.instance.encrypting = not self.instance.encrypting
    
#Strategy pattern, behavioural design pattern
class sort_abstraction():

    def __init__(self, method):
        self.function = method
    
    def execute(self, data, ascending):
        return self.function(data, ascending)

#Facade pattern, structural design pattern
class algorithm_facade():
    def __init__(self):
        self.strategies = {
             'Selection Sort': sort_abstraction(sorting.selection_sort),
             'Bubble Sort': sort_abstraction(sorting.bubble_sort),
             'Merge Sort': sort_abstraction(brute_force.merge_sort)
        }
         
        self.palindrome_counter = dynamic_programming.palindrome_counter()

    def execute_algorithm(self, algorithm, data, ascending, rsa_key, encrypting):
         
        if algorithm != "Palindrome" and algorithm != "RSA" and data != '':
            data = data.split(',')
            for x in range(len(data)):
                data[x] = int(data[x])

        if algorithm in self.strategies:
            return self.strategies[algorithm].execute(data, ascending)
        
        if algorithm == "Palindrome":
            return self.palindrome_counter.check_substring(data)

        if algorithm == "Card Shuffle":
            return randomised.shuffle_deck()
        
        if algorithm == "Factorial":
            n = int(data[0])
            return recursion.factorial(n)
    
        if algorithm == "Fibonacci":
            n = int(data[0])
            return dynamic_programming.nth_fibonacci(n)

        if algorithm == "Search":
            return search.search(data)

        if algorithm == "RSA":
            if rsa_key != '':
                rsa_key = rsa_key.split(',')
                for x in range(len(rsa_key)):
                    rsa_key[x] = int(rsa_key[x])
                return encryption.rsa_entry(encrypting, data, rsa_key)
            else:
                return encryption.rsa_entry(encrypting, data)
        
        return ''
    


class algorithm_aperture():
    def __init__(self):
        self.screen = screen
        self.manager = state_manager()

        self.ascending_toggle = None
        self.execute_button = None
        self.ascending_text = ["Descending", "Ascending"]

        self.data_entry = None
        self.key_entry = None

        self.combobox = None
        self.text_box = None
        self.encrypt_button = None
        self.encrypt_text = ["Decrypt", "Encrypt"]

    def set_encrypt(self):
        self.manager.set_encypting()
        self.encrypt_button.config(text=self.encrypt_text[self.manager.get_encrypting()])
    
    def set_ascending_button(self):
        self.manager.set_ascending()
        self.ascending_toggle.config(text=self.ascending_text[self.manager.get_ascending()])
    
    def execute_command(self):
        algorithm = self.combobox.get()
        data = self.data_entry.get()
        ascending = self.manager.get_ascending()
        encrypting = self.manager.get_encrypting()
        rsa_key = self.key_entry.get()

        output = self.manager.facade.execute_algorithm(algorithm, data, ascending, rsa_key, encrypting)
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(1.0,output)

    def create_window(self):
        screen.geometry("640x480")
        screen.resizable(0,0)
        screen.title("Algorithm Aperture")
        main_frame = tk.Frame(width = 1150, height = 690, bg = "#7b2182")
        main_frame.pack()
        
        self.ascending_toggle = tk.Button(text = "Ascending", command = self.set_ascending_button)
        self.ascending_toggle.place(x=0,y=66)

        self.data_entry = tk.Entry(width = 30)
        self.data_entry.place(x=0,y=0)
        data_entry_lbl = tk.Label(text="Data Entry (insert arrays in the [n, x, y] pattern, and single values as n)")
        data_entry_lbl.place(x=0,y=21)

        self.combobox = ttk.Combobox(screen)
        self.combobox.place(x=0,y=100)
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

        self.execute_button = tk.Button(text = "Execute", command = self.execute_command)
        self.execute_button.place(x=0,y=210)

        self.text_box = tk.Text(width = "80", height = "30", background = "#ffffff",
                                   font = ("Courier new",10))
        self.text_box.insert(1.0, "Output")
        self.text_box.place(x = 0, y = 250)

        self.key_entry = tk.Entry(width = 30)
        self.key_entry.place(x=0,y=160)
        public_key_entry_lbl = tk.Label(text="Key Entry for RSA [public key, private key, modulus key]")
        public_key_entry_lbl.place(x=0,y=185)

        self.encrypt_button = tk.Button(text = "Encrypt", command = self.set_encrypt)
        self.encrypt_button.place(x=0,y=130)

    def clear_window(self):
        for widgets in screen.winfo_children():
            widgets.destroy()
        self.create_window()

screen = tk.Tk()
window = algorithm_aperture()
window.create_window()
screen.mainloop()