import tkinter as tk

root = tk.Tk()
root.title("place()")

tk.Label(root, text="¡Soy una etiqueta!").place(x=50, y=30)
tk.Button(root, text="OK").place(x=10, y=70)

root.mainloop()