from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi;

class VentanaPrincipal(QMainWindow):
    def __init__(self, ppal = None):
        super(VentanaPrincipal,self).__init__(ppal);
        loadUi("ventana_principal.ui",self);
        self.__ventana_principal = ppal
        self.setup();
        
    def asignarControlador(self,c):
        self.__mi_controlador = c
    
    def setup(self):
        self.boton_ingresar.clicked.connect(self.abrir_ventana)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_mostrar.clicked.connect(self.abrir_mostrar)
        self.boton_eliminar.clicked.connect(self.eliminar_paciente)
        
    def eliminar_paciente(self):
        ventana_eliminar = VentanaEliminar(self)
        ventana_eliminar.asignarControlador(self.__mi_controlador)
        
        ventana_eliminar.show()
        
    def abrir_mostrar(self):
        #la ventana principal se pasa como argumento a la ventana
        #secundaria
        ventana_mostrar = VentanaBuscar(self)
        
        #se le asigna el controlador a la ventana ingreso
        #la unica variable que existe de controlador se pasa entre
        #ventanas
        ventana_mostrar.asignarControlador(self.__mi_controlador)
        
        ventana_mostrar.show()

    def abrir_ventana(self):
        #la ventana principal se pasa como argumento a la ventana
        #secundaria
        ventana_ingreso = VentanaIngreso(self)
        
        #se le asigna el controlador a la ventana ingreso
        #la unica variable que existe de controlador se pasa entre
        #ventanas
        ventana_ingreso.asignarControlador(self.__mi_controlador)
        
        ventana_ingreso.show()
    
    def salir(self):
        self.close()

class VentanaIngreso(QMainWindow):
    def __init__(self, ppal = None):
        super(VentanaIngreso,self).__init__(ppal);
        loadUi("VentanaIngreso.ui",self);
        self.__ventana_principal = ppal
        self.setup();
        
    def setup(self):
        self.boton_agregar.clicked.connect(self.agregar_paciente)
        self.boton_limpiar.clicked.connect(self.limpiar_campos)
        
    def agregar_paciente(self):
        nombre = self.campo_nombre.text()
        apellido  = self.campo_apellido.text()
        cedula = self.campo_cedula.text()
        servicio = self.campo_servicio.text()
        edad = self.campo_edad.text()
        #devuelve True si se pudo ingresar
        #False si ya existia la cedula
        resultado = self.__mi_controlador.ingresarPaciente(nombre, apellido, cedula, servicio, edad)
        if resultado == True:
            self.mostrarMensaje("Ingreso exitoso")
        else:
            self.mostrarMensaje("Ya existia la cedula")
    
    def mostrarMensaje(self, mensaje):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Resultado de la operacion")
        msg.setDetailedText("The details are as follows:")
        
        msg.show()
    
    def asignarControlador(self,c):
        self.__mi_controlador = c

    def limpiar_campos(self):
        self.campo_nombre.setText("")
        self.campo_apellido.setText("")
        self.campo_cedula.setText("")
        self.campo_servicio.setText("")
        self.campo_edad.setText("")
        
class VentanaBuscar(QDialog):
    def __init__(self, ppal = None):
        super(VentanaBuscar,self).__init__(ppal);
        loadUi("ventana_buscar.ui",self);
        self.__ventana_principal = ppal
        self.setup();
        
    def setup(self):
        self.boton_buscar.clicked.connect(self.buscar_usuario)
        
        
    def buscar_usuario(self):
        cedula = self.campo_cedula.text()
        
        paciente = self.__mi_controlador.buscarPaciente(cedula)
        
        if paciente != None:
            nombre = paciente.verNombre()
            apellido = paciente.verApellido()
            
            self.campo_nombre.setText(nombre)
            self.campo_apellido.setText(apellido)
        else:
            self.mostrarMensaje("Paciente no existe")
            
    def mostrarMensaje(self, mensaje):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Resultado de la operacion")
        msg.setDetailedText("The details are as follows:")
        msg.show()
            
    def asignarControlador(self,c):
        self.__mi_controlador = c
        
class VentanaEliminar(QDialog):
    def __init__(self, ppal = None):
        super(VentanaEliminar,self).__init__(ppal);
        loadUi("ventana_eliminar.ui",self);
        self.__ventana_principal = ppal
        self.setup();
    
    def setup(self):
        self.buttonBox.accepted.connect(self.eliminarPaciente)
    
    def eliminarPaciente (self):
        c = self.campo_cedula.text()
        
        res = self.__mi_controlador.eliminarPaciente(c)
        
        if res == True:
            self.mostrarMensaje("paciente eliminado")
        else:
            self.mostrarMensaje("Paciente no existe")
            
    def mostrarMensaje(self, mensaje):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Resultado de la operacion")
        msg.setDetailedText("The details are as follows:")
        msg.show()
        
    def asignarControlador(self, c):
        self.__mi_controlador = c
        
        