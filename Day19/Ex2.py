import tkinter as tk 

root = tk.Tk()
root.title("Frame Basic")
root.geometry("500x500")
root.resizable(0,0)
root.iconbitmap("think.ico")

frame_one = tk.Frame(root, bg="red")
frame_one.pack(fill=tk.BOTH, expand=1)
tk.Label(frame_one, text="text").pack()
tk.Label(frame_one, text="text").pack()
tk.Label(frame_one, text="text").pack()

frame_two = tk.Frame(root, bg="blue")
frame_two.pack(fill="x", expand=1)
tk.Label(frame_two, text="text").grid(row=0, column=0)
tk.Label(frame_two, text="text").grid(row=1, column=1)
tk.Label(frame_two, text="text").grid(row=2, column=2)

frame_three = tk.LabelFrame(root, text="Grid System Rules", borderwidth=5 )
frame_three.pack(fill=tk.BOTH, expand=1, padx=10, pady=10 )
tk.Label(frame_three, text="a"*50).grid(row=0, column=0)
root.mainloop()