import sqlite3

# Conectar o crear base de datos
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Crear tabla usuarios si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    edad INTEGER
)
''')

# Insertar un usuario
cursor.execute('INSERT INTO usuarios (nombre, email, edad) VALUES (?, ?, ?)',
               ("Carlos", "carlos@example.com", 30))
conn.commit()

# Consultar todos los usuarios
cursor.execute('SELECT * FROM usuarios')
print("Usuarios en la base de datos:")
for fila in cursor.fetchall():
    print(fila)

# Actualizar edad de un usuario
cursor.execute('UPDATE usuarios SET edad = ? WHERE nombre = ?', (31, "Carlos"))
conn.commit()

# Eliminar usuario por nombre
cursor.execute('DELETE FROM usuarios WHERE nombre = ?', ("Carlos",))
conn.commit()

# Cerrar conexión
conn.close()