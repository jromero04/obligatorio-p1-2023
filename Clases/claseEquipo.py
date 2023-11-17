class Equipo:
    def __init__(self, nombre_eq, modelo_aut_eq, lista_ci_empleado_eq=[]):
        self._nombre_eq = nombre_eq
        self._modelo_aut_eq = modelo_aut_eq
        self._ci_empleado_eq = lista_ci_empleado_eq
        
    def __eq__(self, nuevo_equipo):
        return self._nombre_eq == nuevo_equipo._nombre
    
    def __repr__(self):
        return f"El equipo {self._nombre_eq} es representado por los empleados de Cédula {self._ci_empleado_eq}"
        
    