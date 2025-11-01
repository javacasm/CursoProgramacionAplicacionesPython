# ejemplo de uso de sqlite
# base de datos de películas
import sqlite3

conn = sqlite3.connect('peliculas.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM peliculas")
resultados = cursor.fetchall()
for peli in resultados:
    print(peli[1],peli[2])
    
conn.commit()

