from Clases.claseEmpleado import Empleado


class Piloto(Empleado):
    def __init__(self, cedula, nombre, apellido, fecha_nacimiento, nacionalidad, salario, cargo, equipo, score, nro_auto:int, puntaje_campeonato, lesion, abandona, error, penalidad):
        super().__init__(cedula, nombre, apellido, fecha_nacimiento, nacionalidad, salario, cargo, equipo)
        self._score = score
        self._nro_auto = nro_auto
        self._puntaje_campeonato = puntaje_campeonato
        self._lesion = lesion
        self._abandona = abandona
        self._error = error
        self._penalidad = penalidad
    
    def __repr__(self):
        return f"El piloto {self._nombre} {self._apellido} de cedula {self._cedula} con un score de {self._score} que pertenece al equipo {self._equipo}."
    
    def __eq__(self, otro_piloto):
        if isinstance(otro_piloto, Piloto):
            return int(self._cedula) == int(otro_piloto._cedula)
        else:
            return False

    
    #def __eq__(self, otro_piloto):
     #   return int(self._nro_auto) == (otro_piloto._nro_auto)
