import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Botón Interactivo")
        self.resize(300, 200)
        
        # Layout vertical
        layout = QVBoxLayout()
        
        # Etiqueta
        self.etiqueta = QLabel("Haz clic en el botón")
        layout.addWidget(self.etiqueta)
        
        # Botón
        boton = QPushButton("Clic Aquí")
        boton.clicked.connect(self.cambiar_texto)  # Conectar señal a slot
        layout.addWidget(boton)
        
        self.setLayout(layout)

    def cambiar_texto(self):
        self.etiqueta.setText("¡Botón clicado!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())