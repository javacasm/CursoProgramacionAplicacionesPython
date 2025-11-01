import sqlite3

def crear_conexion():
    return sqlite3.connect('tareas.db')

def crear_tabla(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion TEXT NOT NULL,
        completada INTEGER NOT NULL DEFAULT 0 CHECK(completada IN (0,1))
    )
    ''')
    conn.commit()

def agregar_tarea(conn, descripcion):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tareas (descripcion) VALUES (?)', (descripcion,))
    conn.commit()

def listar_tareas(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT id, descripcion, completada FROM tareas')
    return cursor.fetchall()

def marcar_como_completada(conn, id_tarea):
    cursor = conn.cursor()
    cursor.execute('UPDATE tareas SET completada = 1 WHERE id = ?', (id_tarea,))
    conn.commit()

def eliminar_tarea(conn, id_tarea):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tareas WHERE id = ?', (id_tarea,))
    conn.commit()

# Uso
conn = crear_conexion()
crear_tabla(conn)

agregar_tarea(conn, "Aprender SQLite")
agregar_tarea(conn, "Practicar Python")

print("Tareas:")
for tarea in listar_tareas(conn):
    print(tarea)

marcar_como_completada(conn, 1)
eliminar_tarea(conn, 2)

print("\nTareas después de actualizar:")
for tarea in listar_tareas(conn):
    print(tarea)

conn.close()