from controlador import Controlador
from vista import VentanaPrincipal
from modelo import BaseDatos 
import sys
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    
    
    mi_vista = VentanaPrincipal()
    base_datos = BaseDatos()
    controlador = Controlador(mi_vista,base_datos)
    mi_vista.asignarControlador(controlador)
    mi_vista.show()
    

    sys.exit(app.exec_())

if __name__=='__main__': 
    main()