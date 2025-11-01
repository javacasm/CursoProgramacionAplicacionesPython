from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

# Definir modelos
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    publicaciones = relationship('Publicacion', back_populates='usuario')

    def __repr__(self):
        return f"<Usuario(nombre='{self.nombre}')>"

class Publicacion(Base):
    __tablename__ = 'publicaciones'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    contenido = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship('Usuario', back_populates='publicaciones')

    def __repr__(self):
        return f"<Publicacion(titulo='{self.titulo}')>"

# Crear motor y tablas
motor = create_engine('sqlite:///ejemplo.db', echo=True)
Base.metadata.create_all(motor)

# Crear una sesión
Session = sessionmaker(bind=motor)
sesion = Session()

# Insertar datos
alicia = Usuario(nombre='Alicia')
pub1 = Publicacion(titulo='Primera Publicación', contenido='¡Hola, mundo!', usuario=alicia)
pub2 = Publicacion(titulo='Segunda Publicación', contenido='¡SQLAlchemy es genial!', usuario=alicia)
sesion.add_all([alicia, pub1, pub2])
sesion.commit()

# Consultar datos con relaciones
usuarios = sesion.query(Usuario).all()
for usuario in usuarios:
    print(usuario)
    for publicacion in usuario.publicaciones:
        print(f"  {publicacion}")