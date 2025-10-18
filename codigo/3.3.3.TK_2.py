import tkinter as tk

root = tk.Tk()
root.title("Widgets básicos")

entrada = tk.Entry(root)
entrada.pack()

boton = tk.Button(root, text="Saludar")
boton.pack()

root.mainloop()