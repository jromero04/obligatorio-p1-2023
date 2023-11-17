from Clases.claseEmpleado import Empleado

class Jefe(Empleado):
    def __init__(self, cedula, nombre, apellido, fecha_nacimiento, nacionalidad, salario, cargo, equipo):
        super().__init__(cedula, nombre, apellido, fecha_nacimiento, nacionalidad, salario, cargo, equipo)
        
    def __eq__(self, nuevo_jefe):
        if isinstance(nuevo_jefe, Jefe):
            return self._cedula == nuevo_jefe._cedula
        else:
            return False
    
    @property
    def cedula(self):
        self._cedula

    @cedula.setter
    def cedula(self, nueva_cedula):
        self._cedula = nueva_cedula
        return nueva_cedula