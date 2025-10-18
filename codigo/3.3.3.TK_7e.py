import tkinter as tk

root = tk.Tk()
root.title("Login")

frame = tk.Frame(root, padx=20, pady=20)
frame.grid()

tk.Label(frame, text="Usuario:").grid(row=0, column=0)
tk.Entry(frame).grid(row=0, column=1)

tk.Label(frame, text="Contraseña:").grid(row=1, column=0)
tk.Entry(frame, show="*").grid(row=1, column=1)

tk.Button(frame, text="Ingresar").grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()