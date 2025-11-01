import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('peliculas.db')
cursor = conn.cursor()

# Crear tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS peliculas (
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        anio INTEGER,
        director TEXT
    )
''')

# Insertar datos
cursor.execute("INSERT INTO peliculas (titulo, anio, director) VALUES (?, ?, ?)",
               ('El Padrino', 1972, 'Francis Ford Coppola'))
cursor.execute("INSERT INTO peliculas (titulo, anio, director) VALUES (?, ?, ?)",
               ('Pulp Fiction', 1994, 'Quentin Tarantino'))

# Guardar cambios
conn.commit()

# Cerrar conexión
conn.close()