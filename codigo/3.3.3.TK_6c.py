import tkinter as tk

root = tk.Tk()
root.title("Lista de tareas")

tareas = [
    "Comprar leche",
    "Hacer ejercicio",
    "Estudiar Python"
]

variables = []
checkbuttons = []

for tarea in tareas:
    var = tk.BooleanVar()
    check = tk.Checkbutton(root, text=tarea, variable=var)
    check.pack(anchor='w')
    variables.append(var)
    checkbuttons.append(check)

def mostrar_tareas():
    for i, var in enumerate(variables):
        if var.get():
            print(f"Tarea completada: {tareas[i]}")

boton = tk.Button(root, text="Mostrar tareas completadas", command=mostrar_tareas)
boton.pack()

root.mainloop()