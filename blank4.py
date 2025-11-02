import tkinter as tk

root = tk.Tk()
root.title("Blank App 4")
root.geometry("200x100")

label = tk.Label(root, text="Hello World!", font=("Arial", 12))
label.pack(expand=True)

root.mainloop()
