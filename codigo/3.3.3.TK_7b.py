import tkinter as tk

root = tk.Tk()
root.title("pack()")

tk.Label(root, text="Etiqueta 1").pack()
tk.Label(root, text="Etiqueta 2").pack()
tk.Label(root, text="Etiqueta 3").pack()

root.mainloop()