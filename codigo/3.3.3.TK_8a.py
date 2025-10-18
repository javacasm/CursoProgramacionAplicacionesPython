import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Validación básica")

entry = tk.Entry(root)
entry.pack()

def validar():
    texto = entry.get()
    if not texto:
        messagebox.showerror("Error", "El campo no puede estar vacío")
    else:
        messagebox.showinfo("Éxito", f"Texto ingresado: {texto}")

tk.Button(root, text="Validar", command=validar).pack()

root.mainloop()