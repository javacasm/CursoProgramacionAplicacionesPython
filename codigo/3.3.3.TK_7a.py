import tkinter as tk

root = tk.Tk()
root.title("Frame básico")

# Crear un Frame
frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
frame.pack()

# Agregar widgets al Frame
etiqueta = tk.Label(frame, text="¡Este es un Frame!")
etiqueta.pack()

root.mainloop()