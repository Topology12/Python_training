import tkinter as tk
from tkinter import END


def print():
    text = tk.Label(frame_two, text=text_entry.get(), bg="#f00")
    text.pack()
    text_entry.delete(0, END)


def count(number):
    global value
    text = tk.Label(frame_two, text=number, bg="red")
    text.pack()
    value = number + 1


root = tk.Tk()
root.title("Entry Basic")
root.geometry("500x500")
root.resizable(0, 0)
root.iconbitmap("think.ico")

frame_one = tk.Frame(root, bg='blue', height=100)
frame_one.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)
frame_one.grid_propagate(False)

text_entry = tk.Entry(frame_one, width=40)
text_entry.grid(row=0, column=0, padx=5, pady=5)

button_print = tk.Button(frame_one, text="Print", command=print)
button_print.grid(row=0, column=1, padx=5, pady=5, ipadx=30)

button_count = tk.Button(frame_one, text="Count", command=lambda: count(value))
button_count.grid(row=1, column=0, columnspan=2, sticky="we", padx=5, pady=5)

value = 1 
frame_two = tk.Frame(root, bg="red", height=400)
frame_two.pack(fill=tk.BOTH, expand=1, padx=10, pady=(0,10))
frame_two.pack_propagate(False)

root.mainloop()
