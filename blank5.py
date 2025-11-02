import tkinter as tk

root = tk.Tk()
root.title("Blank App 5")
root.geometry("200x100")

label = tk.Label(root, text="Bye Bye!", font=("Arial", 12))
label.pack(expand=True)

root.mainloop()
