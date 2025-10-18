import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Notas con archivos")

texto = tk.Text(root, height=5, width=30)
texto.pack()

def guardar_nota():
    with open("nota.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto.get("1.0", tk.END))
    messagebox.showinfo("Éxito", "Nota guardada")

def cargar_nota():
    try:
        with open("nota.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            texto.delete("1.0", tk.END)
            texto.insert("1.0", contenido)
    except FileNotFoundError:
        messagebox.showerror("Error", "No hay notas guardadas")

tk.Button(root, text="Guardar nota", command=guardar_nota).pack()
tk.Button(root, text="Cargar nota", command=cargar_nota).pack()

root.mainloop()