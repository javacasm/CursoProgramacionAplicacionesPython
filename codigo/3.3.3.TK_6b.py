import tkinter as tk

root = tk.Tk()
root.title("Radiobutton")

valor = tk.StringVar()
opciones = [
    ("Opción 1", "1"),
    ("Opción 2", "2"),
    ("Opción 3", "3")
]

for texto, valor_opcion in opciones:
    tk.Radiobutton(root, text=texto, variable=valor, value=valor_opcion).pack()

def mostrar_seleccion():
    print("Has elegido:", valor.get())

boton = tk.Button(root, text="Mostrar selección", command=mostrar_seleccion)
boton.pack()

root.mainloop()