from tkinter import Tk, messagebox, Button

root = Tk()
root.title("Confirmación")

def confirmar():
    respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres continuar?")
    if respuesta:
        print("Usuario confirmó")
    else:
        print("Usuario canceló")

Button(root, text="Confirmar", command=confirmar).pack()
root.mainloop()