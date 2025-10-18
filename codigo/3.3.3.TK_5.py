import tkinter as tk

root = tk.Tk()
root.title("Actualización de etiqueta")

contador = 0
etiqueta = tk.Label(root, text=f"Contador: {contador}")
etiqueta.pack()

def incrementar():
    global contador
    contador += 1
    etiqueta.config(text=f"Contador: {contador}")

def clic_derecho(event):
    print("¡Clic derecho detectado!")

boton = tk.Button(root, text="Incrementar", command=incrementar)
boton.pack()

root.bind("<Button-3>", clic_derecho)
root.mainloop()