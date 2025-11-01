import sqlite3

conn = sqlite3.connect('productos.db')
cursor = conn.cursor()

# Crear tabla productos
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT,
    precio REAL CHECK(precio >= 0),
    stock INTEGER CHECK(stock >= 0)
)
''')

# Insertar varios productos
productos = [
    ("Camiseta", "Ropa", 15.99, 50),
    ("Pantalones", "Ropa", 39.99, 20),
    ("Ratón", "Electrónica", 25.75, 15),
    ("Teclado", "Electrónica", 45.40, 10),
    ("Libro Python", "Libros", 29.95, 100)
]
cursor.executemany('INSERT INTO productos (nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)', productos)
conn.commit()

# Consultar productos en categoría "Electrónica" con stock > 5, ordenados por precio descendente
categoria = "Electrónica"
stock_min = 5
cursor.execute('''
SELECT nombre, precio, stock FROM productos
WHERE categoria = ? AND stock > ?
ORDER BY precio DESC
''', (categoria, stock_min))
resultados = cursor.fetchall()

print(f"Productos en categoría '{categoria}' con stock > {stock_min}:")
for producto in resultados:
    print(producto)

# Buscar productos cuyo nombre contenga 'Libro'
busqueda = "%Libro%"
cursor.execute('SELECT nombre, categoria, precio FROM productos WHERE nombre LIKE ?', (busqueda,))
productos_encontrados = cursor.fetchall()

print("\nProductos que contienen 'Libro' en el nombre:")
for producto in productos_encontrados:
    print(producto)

conn.close()