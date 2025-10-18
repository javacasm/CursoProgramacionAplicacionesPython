import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Formulario con validación")

tk.Label(root, text="Nombre:").pack()
nombre = tk.Entry(root)
nombre.pack()

tk.Label(root, text="Edad:").pack()
edad = tk.Entry(root)
edad.pack()

def validar_formulario():
    if not nombre.get():
        messagebox.showerror("Error", "El nombre es obligatorio")
        return
    try:
        int(edad.get())
    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número")
        return
    messagebox.showinfo("Éxito", "Formulario válido")

tk.Button(root, text="Enviar", command=validar_formulario).pack()

root.mainloop()