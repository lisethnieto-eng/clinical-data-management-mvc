
class Paciente:
    def __init__(self, n, a, c, s, e):
        self.__nombre = n
        self.__apellido = a
        self.__cedula = c
        self.__servicio = s
        self.__edad = e
        
    def verNombre(self):
        return self.__nombre
    
    def verApellido(self):
        return self.__apellido
        

class BaseDatos(object):
    
    def __init__(self):
        self.__pacientes = {}
        
    def verificarExiste(self,c):
        if c in self.__pacientes.keys():
            return True
        else:
            return False
        
    def buscarPaciente(self,c):
        try:
            return self.__pacientes[c]
        except:
            return None
        
    def eliminarPaciente(self, c):
        existe =self.verificarExiste(c)
        if existe == True:
            del self.__pacientes[c]
            return True
        else:
            False
    
    def ingresarPaciente(self, n, a, c, s, e):
        
        #verificamos si existe
        existe = self.verificarExiste(c)
        
        #si no existe lo guardo en el diccionario
        if existe == False:
            p = Paciente(n, a, c, s, e)
            self.__pacientes[c] = p
            return True #retorno True indicando que se pudo guardar
        else:
            #si ya estaba guardado retorno False
            return False
        
        
        
        
        
        
        