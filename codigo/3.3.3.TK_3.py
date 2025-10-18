import tkinter as tk

root = tk.Tk()
root.title("Hola mundo")

etiqueta = tk.Label(root, text="¡Bienvenido a Tkinter!")
etiqueta.pack()

def saludar():
    print("¡Hola, Tkinter!")

boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack()

root.mainloop()