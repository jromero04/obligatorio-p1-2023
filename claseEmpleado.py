class Empleado:
    def __init__(self, cedula, nombre, apellido, fecha_nacimiento, nacionalidad, salario, cargo, equipo):
        self._cedula = cedula 
        self._apellido = apellido
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento
        self._nacionalidad = nacionalidad
        self._salario = salario
        self._cargo = cargo
        self._equipo = equipo
    
    def __repr__(self):
        return str(self._cargo) +" "+ self._nombre + " " + self._apellido + " -- " + str(self._cedula)
    
    def __eq__(self, nuevo_empleado):
        return str(self._cedula) == str(nuevo_empleado._cedula)
    
    @property
    def equipo(self):
        return self._equipo
    
    @equipo.setter
    def equipo(self, nuevo_equipo):
        self._equipo = nuevo_equipo
        return nuevo_equipo

    @property
    def cedula(self):
        return self._cedula
    
    @cedula.setter
    def cedula(self, actualizacion_cedula):
        self._cedula = actualizacion_cedula
        return actualizacion_cedula
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre == nuevo_nombre
        return nuevo_nombre
    
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @property
    def nacionalidad(self):
        return self.__nacionalidad
    
    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        self.__nacionalidad = nueva_nacionalidad
        return nueva_nacionalidad
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, nuevo_salario):
        self.__salario = nuevo_salario
        return nuevo_salario
    
    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, nuevo_cargo):
        self.__cargo = nuevo_cargo
        return nuevo_cargo