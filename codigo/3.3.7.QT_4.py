import sys
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QLineEdit, QWidget

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Básica")
        self.resize(300, 400)
        
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)  # Alineación derecha
        
        layout = QGridLayout()
        layout.addWidget(self.display, 0, 0, 1, 4)  # Display en la fila 0, columnas 0-3
        
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        fila = 1
        columna = 0
        for boton_texto in botones:
            boton = QPushButton(boton_texto)
            boton.clicked.connect(self.presionar_boton)
            layout.addWidget(boton, fila, columna)
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1
        
        self.setLayout(layout)
        self.expresion = ""

    def presionar_boton(self):
        boton = self.sender()  # Obtener el botón que emitió la señal
        texto = boton.text()
        
        if texto == '=':
            try:
                resultado = str(eval(self.expresion))
                self.display.setText(resultado)
                self.expresion = resultado
            except Exception:
                self.display.setText("Error")
                self.expresion = ""
        else:
            self.expresion += texto
            self.display.setText(self.expresion)

if __name__ == "__main__":
    from PySide6.QtCore import Qt  # Importar Qt para AlignmentFlag
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())