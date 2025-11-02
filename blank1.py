import tkinter as tk

root = tk.Tk()
root.title("Blank App 1")
root.geometry("200x100")

label = tk.Label(root, text="This does nothing!", font=("Arial", 12))
label.pack(expand=True)

root.mainloop()
