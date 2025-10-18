import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget

# Crear la aplicación
app = QApplication(sys.argv)

# Crear una ventana principal
ventana = QWidget()
ventana.setWindowTitle("Hola Qt")  # Título de la ventana
ventana.resize(300, 200)  # Tamaño inicial

# Agregar una etiqueta
etiqueta = QLabel("¡Hola, Mundo con Qt!", parent=ventana)
etiqueta.move(50, 80)  # Posición absoluta

# Mostrar la ventana
ventana.show()

# Ejecutar el bucle de eventos
sys.exit(app.exec())