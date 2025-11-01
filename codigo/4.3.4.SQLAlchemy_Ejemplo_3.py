from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Crear una clase base para modelos
Base = declarative_base()

# Definir el modelo Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    correo = Column(String)
    edad = Column(Integer)

    def __repr__(self):
        return f"<Usuario(nombre='{self.nombre}', correo='{self.correo}', edad={self.edad})>"

# Crear un motor de base de datos
motor = create_engine('sqlite:///ejemplo.db', echo=True)

# Crear tablas
Base.metadata.create_all(motor)

# Crear una sesión
Session = sessionmaker(bind=motor)
sesion = Session()

# Insertar datos
alicia = Usuario(nombre='Alicia', correo='alicia@ejemplo.com', edad=25)
roberto = Usuario(nombre='Roberto', correo='roberto@ejemplo.com', edad=30)
sesion.add_all([alicia, roberto])
sesion.commit()

# Consultar datos
usuarios = sesion.query(Usuario).all()
for usuario in usuarios:
    print(usuario)

# Actualizar datos
alicia = sesion.query(Usuario).filter_by(nombre='Alicia').first()
alicia.edad = 26
sesion.commit()

# Eliminar datos
roberto = sesion.query(Usuario).filter_by(nombre='Roberto').first()
sesion.delete(roberto)
sesion.commit()

# Consultar nuevamente
usuarios = sesion.query(Usuario).all()
for usuario in usuarios:
    print(usuario)