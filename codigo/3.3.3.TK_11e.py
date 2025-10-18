from tkinter import Tk, Button, messagebox, Label

root = Tk()
root.title("Aplicación con diálogos")
root.geometry("400x200")

def mostrar_info():
    messagebox.showinfo("Información", "¡Bienvenido a la aplicación!")

def pedir_confirmacion():
    respuesta = messagebox.askyesno("Confirmar", "¿Desea salir de la aplicación?")
    if respuesta:
        root.destroy()

Label(root, text="Ejemplo de cuadros de diálogo", bg="lightgray", fg="black", font=("Arial", 12)).pack(pady=20)

Button(root, text="Mostrar información", command=mostrar_info).pack(pady=5)
Button(root, text="Salir", command=pedir_confirmacion).pack(pady=5)

root.mainloop()