import sys
import json
from PySide6.QtWidgets import QApplication, QListWidget, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Tareas")
        self.resize(400, 400)
        
        layout = QVBoxLayout()
        
        # Campo para nueva tarea
        self.campo_tarea = QLineEdit()
        layout.addWidget(self.campo_tarea)
        
        # Botón agregar
        boton_agregar = QPushButton("Agregar Tarea")
        boton_agregar.clicked.connect(self.agregar_tarea)
        layout.addWidget(boton_agregar)
        
        # Lista de tareas
        self.lista_tareas = QListWidget()
        layout.addWidget(self.lista_tareas)
        
        # Botón eliminar
        boton_eliminar = QPushButton("Eliminar Seleccionada")
        boton_eliminar.clicked.connect(self.eliminar_tarea)
        layout.addWidget(boton_eliminar)
        
        self.setLayout(layout)
        
        # Cargar tareas desde archivo
        self.archivo = "tareas.json"
        self.cargar_tareas()

    def agregar_tarea(self):
        tarea = self.campo_tarea.text().strip()
        if tarea:
            self.lista_tareas.addItem(tarea)
            self.campo_tarea.clear()
            self.guardar_tareas()
        else:
            QMessageBox.warning(self, "Error", "Ingresa una tarea.")

    def eliminar_tarea(self):
        item_seleccionado = self.lista_tareas.currentItem()
        if item_seleccionado:
            self.lista_tareas.takeItem(self.lista_tareas.row(item_seleccionado))
            self.guardar_tareas()
        else:
            QMessageBox.warning(self, "Error", "Selecciona una tarea.")

    def guardar_tareas(self):
        tareas = [self.lista_tareas.item(i).text() for i in range(self.lista_tareas.count())]
        with open(self.archivo, 'w') as f:
            json.dump(tareas, f)

    def cargar_tareas(self):
        try:
            with open(self.archivo, 'r') as f:
                tareas = json.load(f)
                for tarea in tareas:
                    self.lista_tareas.addItem(tarea)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TodoApp()
    ventana.show()
    sys.exit(app.exec())