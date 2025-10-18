from tkinter import Tk, messagebox,Button

root = Tk()
root.title("Cuadros de diálogo")
root.geometry("400x200")

def mostrar_mensaje():
    messagebox.showinfo("Información", "¡Operación realizada con éxito!")

Button(root, text="Mostrar mensaje", command=mostrar_mensaje).pack()

root.mainloop()