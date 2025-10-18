import sys
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class Formulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario Simple")
        self.resize(400, 250)
        
        layout = QVBoxLayout()
        
        # Etiqueta y campo de texto
        etiqueta_nombre = QLabel("Ingresa tu nombre:")
        layout.addWidget(etiqueta_nombre)
        self.campo_nombre = QLineEdit()
        layout.addWidget(self.campo_nombre)
        
        # Botón
        boton_enviar = QPushButton("Enviar")
        boton_enviar.clicked.connect(self.procesar_formulario)
        layout.addWidget(boton_enviar)
        
        # Etiqueta de resultado
        self.resultado = QLabel("")
        layout.addWidget(self.resultado)
        
        self.setLayout(layout)

    def procesar_formulario(self):
        nombre = self.campo_nombre.text().strip()
        if nombre:
            self.resultado.setText(f"¡Hola, {nombre}!")
        else:
            QMessageBox.warning(self, "Error", "Por favor, ingresa un nombre.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Formulario()
    ventana.show()
    sys.exit(app.exec())