from Clases.claseEmpleado import Empleado

class Mecanico(Empleado):
    def __init__(self, cedula, nombre, apellido, fecha_nacimiento, nacionalidad, salario, cargo, equipo, score):
        super().__init__(cedula, nombre, apellido, fecha_nacimiento, nacionalidad, salario, cargo, equipo)
        self._score = score
        
    def __eq__(self, otro_mec):
        if isinstance(otro_mec, Mecanico):
            return int(self._cedula) == int(otro_mec._cedula)
        else:
            return False
