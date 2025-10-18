import tkinter as tk

root = tk.Tk()
root.title("grid()")

tk.Label(root, text="Usuario:").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)
tk.Label(root, text="Contraseña:").grid(row=1, column=0)
tk.Entry(root, show="*").grid(row=1, column=1)
tk.Button(root, text="Ingresar").grid(row=2, column=0, columnspan=2)

root.mainloop()