import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label

root = tk.Tk()
root.title('Label Basics!')
root.iconbitmap("think.ico")
root.geometry('400x400')
root.resizable(0,0)
root.config(bg='blue')


label =tk.Label(root, text='Hello, my name is Mike')
label.pack()

label_one =tk.Label(root, text="Hello, my name is John.", font=("Arial", 18, "bold"))
label_one.pack()

label_two =tk.Label(root, text="Hello, my name is Paul", background ="red")
label_two.config(font=("Arial", 10,))
label_two.pack(padx = 10, pady = 50)

label_three =tk.Label(root, text='Hello, my name is Sue.', background='black', fg='green')
label_three.pack(pady=(0, 10), ipadx=50, ipady=10, anchor='w')

label_four = tk.Label(root, text='Hello, my name is Pat', bg='white', fg="#123456")
label_four.pack(fill='both', expand=1, padx=10, pady=10)

root.mainloop()

