from FIA import Fia
from Menu.menu_principal import menu_principal
from Menu.menu_consultas import menu_consultas

def menuEjecucion(menu_activado, listaTotalEmpleados, listaTotalAutos, listaTotalEquipos, lista_empleados_registrados, lista_habilitados, score_final):
    f = Fia()
    while(menu_activado):
        menu_principal()
        print("")
        opcion = input("Seleccione una opción: ")
        print("")

        if opcion == "1":
            f.alta_empleado(listaTotalEmpleados)
        elif opcion == "2":
            f.alta_auto(listaTotalAutos)
        elif opcion == "3":
            f.alta_equipo(listaTotalEquipos, listaTotalAutos, listaTotalEmpleados)
        elif opcion == "4":
            if len(listaTotalEquipos)>=2:
                f.simular_carrera(lista_empleados_registrados, listaTotalEquipos, listaTotalAutos, puntos_equipos=None)
            else:
                print("No tienes suficientes equipos para simular una carrera.")
            pass

        elif opcion == "5":
            if len(listaTotalEquipos)>=1:
                menu_consultas()
                print("")
                opcion_c = input("Seleccione una opción: ")
                print("")
                if opcion_c == "1":
                    print("Lo sentimos, esta opción no está permitida en todas las regiones.")
                elif opcion_c == "2":
                    print("Lo sentimos, esta opción no está permitida en todas las regiones.")
                elif opcion_c == "3":
                    f.consulta_3(lista_empleados_registrados)
                elif opcion_c == "4":
                    f.consulta_4(lista_empleados_registrados)
                elif opcion_c == "5":
                    f.consulta_5(lista_empleados_registrados)
                elif opcion_c == "6":
                    break
                else:
                    print("No se reconoce esa opción, por favor intente nuevamente.")
            else:
                print("No tienes suficientes equipos")
        elif opcion == "6":
            break
        else:
            print("No se reconoce esa opción, por favor intente nuevamente.")