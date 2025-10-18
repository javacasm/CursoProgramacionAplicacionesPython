import tkinter as tk

root = tk.Tk()
root.title("Checkbutton")

valor = tk.BooleanVar()
casilla = tk.Checkbutton(root, text="Acepto los términos", variable=valor)
casilla.pack()

def mostrar_estado():
    print("Estado:", valor.get())

boton = tk.Button(root, text="Mostrar estado", command=mostrar_estado)
boton.pack()

root.mainloop()