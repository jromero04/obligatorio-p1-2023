from Clases.claseEmpleado import Empleado
from Clases.claseEquipo import Equipo
from Clases.claseAuto import Auto
from Clases.clasePiloto import Piloto
from Clases.claseMecanico import Mecanico
from Metodos.f_alta_auto import alta_auto
from Metodos.f_alta_empleado import alta_empleado
from Metodos.f_alta_equipo import alta_equipo
from Consultas.consulta_nro_3 import consulta_3
from Consultas.consulta_nro_4 import consulta_4
#from Consultas.consulta_nro_5 import consulta_5
from Menu.menu_principal import menu_principal
from Metodos.metodos_aux import empleados_registrados
#from Metodos.metodos_aux import pilotos_lesionados

def menuEjecucion(menu_activado, listaTotalEmpleados, listaTotalAutos, listaTotalEquipos, lista_empleados_registrados):
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_empleado(listaTotalEmpleados)
    alta_auto(listaTotalAutos)
    alta_auto(listaTotalAutos)
    alta_auto(listaTotalAutos)
    alta_equipo(listaTotalEquipos, listaTotalAutos, listaTotalEmpleados)
    empleados_registrados(listaTotalEmpleados, lista_empleados_registrados, listaTotalEquipos)
    #consulta_4(listaTotalEmpleados)  ####)
    #consulta_5(listaTotalEmpleados)
    #consulta_3(listaTotalEmpleados)
    #pilotos_lesionados(listaTotalEquipos, listaTotalAutos, listaTotalEmpleados)
    #alta_equipo(listaTotalEquipos)
    #while(menu_activado):
        #menu_principal()
        #print("")
        #opcion = input("Seleccione una opción: ")
        #print("")

        #if opcion == "1":
        #    alta_empleado(listaTotalEmpleados)
        #elif opcion == "2":
        #    alta_auto(listaTotalAutos)
        