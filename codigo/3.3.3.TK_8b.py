import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Conversión numérica")

entry = tk.Entry(root)
entry.pack()

def convertir():
    try:
        numero = float(entry.get())
        messagebox.showinfo("Éxito", f"Número convertido: {numero}")
    except ValueError:
        messagebox.showerror("Error", "Debes introducir un número válido")

tk.Button(root, text="Convertir", command=convertir).pack()

root.mainloop()