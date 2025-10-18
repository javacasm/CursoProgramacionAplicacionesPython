import tkinter as tk

ventana = tk.Tk()
ventana.title("Aplicación con menús")
ventana.geometry("800x600")

# Barra de menús
barra_menus = tk.Menu(ventana)
ventana.config(menu=barra_menus)

# Menú Archivo
menu_archivo = tk.Menu(barra_menus, tearoff=False)
barra_menus.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir", command=lambda: print("Abrir archivo"))
menu_archivo.add_command(label="Guardar", command=lambda: print("Guardar archivo"))
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.destroy)

# Submenú Preferencias
menu_preferencias = tk.Menu(menu_archivo, tearoff=False)
menu_archivo.add_cascade(label="Preferencias", menu=menu_preferencias)
menu_preferencias.add_command(label="Configuración", command=lambda: print("Configuración"))
menu_preferencias.add_command(label="Tema", command=lambda: print("Cambiar tema"))

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menus, tearoff=False)
barra_menus.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=lambda: print("Acerca de la aplicación"))

# Menú contextual
def menu_contextual(event):
    menu = tk.Menu(ventana, tearoff=False)
    menu.add_command(label="Copiar", command=lambda: print("Copiar"))
    menu.add_command(label="Pegar", command=lambda: print("Pegar"))
    menu.tk_popup(event.x_root, event.y_root)

ventana.bind("<Button-3>", menu_contextual)

ventana.mainloop()