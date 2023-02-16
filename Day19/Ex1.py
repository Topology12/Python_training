import tkinter as tk

root = tk.Tk()
root.title("Button Basics")
root.geometry("500x500")
root.resizable(0, 0)
root.iconbitmap("think.ico")

name_button = tk.Button(root, text="Name")
name_button.grid(row=0, column=0)

time_button = tk.Button(root, text="Time", bg="#00FFFF")
time_button.grid(row=0, column=1, padx=(10, 0))

place_button = tk.Button(root, text="Place", bg="#00FFFF")
place_button.grid(row=0, column=2, padx=(10,0), ipadx=15 )
 
day_button = tk.Button(root, text="Day", bg="black", foreground="white")
day_button.grid(row=1, column=0, columnspan=3, sticky="we", pady=(10,0))

test_one = tk.Button(root, text="Test1")
test_one.grid(padx=5, pady=5, row=2, column=0)

test_two = tk.Button(root, text="Test2")
test_two.grid(row=2, column=1, padx=5, pady=5)

test_three = tk.Button(root, text="Test3")
test_three.grid(row=2, column=2, padx=5, pady=5, sticky="w")

test_four = tk.Button(root, text="Test4")
test_four.grid(row=3, column=0, padx=5, pady=5)

test_five = tk.Button(root, text="Test5")
test_five.grid(row=3, column=1, padx=5, pady=5)

test_six = tk.Button(root, text="Test6")
test_six.grid(row=3, column=2, padx=5, pady=5, sticky="w")

root.mainloop()
