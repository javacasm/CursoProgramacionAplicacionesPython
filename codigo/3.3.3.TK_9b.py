import tkinter as tk
from tkinter import messagebox
import sqlite3

root = tk.Tk()
root.title("Base de datos de contactos")

tk.Label(root, text="Nombre:").pack()
nombre = tk.Entry(root)
nombre.pack()

tk.Label(root, text="Teléfono:").pack()
telefono = tk.Entry(root)
telefono.pack()

# Crear la base de datos y la tabla si no existen
conexion = sqlite3.connect("contactos.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS contactos (nombre TEXT, telefono TEXT)")
conexion.commit()

def guardar_contacto():
    cursor.execute("INSERT INTO contactos VALUES (?, ?)", (nombre.get(), telefono.get()))
    conexion.commit()
    nombre.delete(0, tk.END)
    telefono.delete(0, tk.END)
    messagebox.showinfo("Éxito", "Contacto guardado")

def mostrar_contactos():
    cursor.execute("SELECT * FROM contactos")
    for fila in cursor.fetchall():
        print(f"Nombre: {fila[0]}, Teléfono: {fila[1]}")

tk.Button(root, text="Guardar contacto", command=guardar_contacto).pack()
tk.Button(root, text="Mostrar contactos", command=mostrar_contactos).pack()

root.mainloop()