from tkinter import Tk, Label

root = Tk()
root.title("Estilos visuales")

label = Label(root, text="¡Hola, Tkinter!", bg="lightblue", fg="navy", font=("Arial", 16))
label.pack()

root.mainloop()