

class Controlador(object):
    #recibe una variable del tipo vista y otro del tipo modelo
    #guarda las variables en sus respectivos atributos
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo
        
    def buscarPaciente(self,c):
        resultado = self.__mi_modelo.buscarPaciente(c)
        return resultado
        
        
    def ingresarPaciente(self, n, a, c, s, e):
        resultado = self.__mi_modelo.ingresarPaciente(n, a, c, s, e)
        return resultado
    
    def eliminarPaciente(self, c):
        res = self.__mi_modelo.eliminarPaciente(c)
        return res
