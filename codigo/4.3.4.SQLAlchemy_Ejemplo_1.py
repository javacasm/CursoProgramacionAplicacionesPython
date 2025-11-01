from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import select

# Crear un motor de base de datos (SQLite)
motor = create_engine('sqlite:///ejemplo.db', echo=True)

# Inicializar metadatos
metadatos = MetaData()

# Definir la tabla usuarios
usuarios = Table('usuarios', metadatos,
                 Column('id', Integer, primary_key=True),
                 Column('nombre', String),
                 Column('correo', String),
                 Column('edad', Integer))

# Crear la tabla en la base de datos
metadatos.create_all(motor)

# Insertar datos
with motor.connect() as conn:
    conn.execute(usuarios.insert().values([
        {'nombre': 'Alicia', 'correo': 'alicia@ejemplo.com', 'edad': 25},
        {'nombre': 'Roberto', 'correo': 'roberto@ejemplo.com', 'edad': 30}
    ]))
    conn.commit()

# Consultar los datos
with motor.connect() as conn:
    resultado = conn.execute(select(usuarios))
    for fila in resultado:
        print(fila)