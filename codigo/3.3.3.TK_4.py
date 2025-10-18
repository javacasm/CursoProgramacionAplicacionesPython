import tkinter as tk

root = tk.Tk()
root.title("Saludo personalizado")

etiqueta = tk.Label(root, text="Escribe tu nombre:")
etiqueta.pack()

entrada = tk.Entry(root)
entrada.pack()

def saludar():
    nombre = entrada.get()
    mensaje = tk.Label(root, text=f"¡Hola, {nombre}!")
    mensaje.pack()

boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack()

root.mainloop()