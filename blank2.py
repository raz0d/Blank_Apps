import tkinter as tk

root = tk.Tk()
root.title("Blank App 2")
root.geometry("200x100")

label = tk.Label(root, text="I eat RAM!", font=("Arial", 12))
label.pack(expand=True)

root.mainloop()
