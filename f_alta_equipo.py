from Clases.claseEmpleado import Empleado
from Clases.claseEquipo import Equipo
from Clases.claseAuto import Auto
from Clases.clasePiloto import Piloto
from Clases.claseMecanico import Mecanico
from Clases.claseJefe import Jefe

def alta_equipo(lista_equipos, lista_autos, lista_empleados):
    print("Alta de equipo\n")
    nombre_equipo = input("Ingrese nombre del equipo: ")        
    if nombre_equipo == "":
        print("Nombre de equipo ingresado incorrectamente.")
    else:
        nbr_eq = nombre_equipo
        modelo_auto = input("Ingrese modelo del auto: ")
        aux = Auto(modelo_auto, None, None)
        if aux not in lista_autos:
            print("El modelo de auto que ha proporcionado no se ha encontrado.")
        else:
            modelo_aut_eq = modelo_auto
            lista_ci_empleado_eq = []
            ci_piloto1 = int(input("Ingrese la CI del 1er piloto: "))
            aux = Piloto(ci_piloto1, None, None, None, None, None, None, None, None ,None ,None ,None ,None ,None , None)
            if aux not in lista_empleados:
                print("No se ha encontrado al piloto proporcionado.")
            else:
                lista_ci_empleado_eq.append(ci_piloto1)
                i = lista_empleados.index(aux)
                lista_empleados[i]._equipo = nbr_eq
                print("Primer piloto agregado correctamente")
                ci_piloto2 = int(input("Ingrese la CI del segundo piloto: "))
                aux = Piloto(ci_piloto2, None,None,None,None,None,None, None,None,None,None,None,None,None,None)
                if aux not in lista_empleados:
                    print("No se ha encontrado al piloto proporcionado.")
                else:
                    lista_ci_empleado_eq.append(ci_piloto2)
                    i = lista_empleados.index(aux)
                    lista_empleados[i]._equipo = nbr_eq
                    print("Segundo piloto agregado correctamente.")
                    ci_piloto_res = int(input("Ingrese la CI del piloto reserva: "))
                    aux = Piloto(ci_piloto_res, None,None,None,None,None,None, None, None,None,None,None,None,None,None)
                    if aux not in lista_empleados:
                        print("No se ha encontrado al piloto reserva proporcionado.")
                    else:
                        lista_ci_empleado_eq.append(ci_piloto_res)
                        i = lista_empleados.index(aux)
                        lista_empleados[i]._equipo = nbr_eq
                        print("Piloto reserva agregado correctamente.")
                        ci_mec1 = int(input("Ingrese la CI del primer mecánico: "))
                        aux = Mecanico(ci_mec1, None, None, None, None, None, None, None, None)
                        if aux not in lista_empleados:
                            print("No se ha encontrado al mecánico proporcionado.")
                        else:
                            lista_ci_empleado_eq.append(ci_mec1)
                            i = lista_empleados.index(aux)
                            lista_empleados[i]._equipo = nbr_eq
                            print("Primer mecánico agregado correctamente")
                            ci_mec2 = int(input("Ingrese la CI del segundo mecánico: "))
                            aux = Mecanico(ci_mec2, None, None, None, None, None, None, None, None)
                            if aux not in lista_empleados:
                                print("No se ha encontrado al mecánico proporcionado.")
                            else:
                                lista_ci_empleado_eq.append(ci_mec2)
                                i = lista_empleados.index(aux)
                                lista_empleados[i]._equipo = nbr_eq
                                print("Segundo mecánico agregado correctamente")
                                ci_mec3 = int(input("Ingrese la CI del tercer mecánico: "))
                                aux = Mecanico(ci_mec3, None, None, None, None, None, None, None, None)
                                if aux not in lista_empleados:
                                    print("No se ha encontrado al mecánico proporcionado.")
                                else:
                                    lista_ci_empleado_eq.append(ci_mec3)
                                    i = lista_empleados.index(aux)
                                    lista_empleados[i]._equipo = nbr_eq
                                    print("Tercer mecánico agregado correctamente")
                                    ci_mec4 = int(input("Ingrese la CI del cuarto mecánico: "))
                                    aux = Mecanico(ci_mec4, None, None, None, None, None, None,None, None)
                                    if aux not in lista_empleados:
                                        print("No se ha encontrado al mecánico proporcionado.")
                                    else:
                                        lista_ci_empleado_eq.append(ci_mec4)
                                        i = lista_empleados.index(aux)
                                        lista_empleados[i]._equipo = nbr_eq
                                        print("Cuarto mecánico agregado correctamente")
                                        ci_mec5 = int(input("Ingrese la CI del quinto mecánico: "))
                                        aux = Mecanico(ci_mec5, None, None, None, None, None, None,None, None)
                                        if aux not in lista_empleados:
                                            print("No se ha encontrado al mecánico proporcionado.")
                                        else:
                                            lista_ci_empleado_eq.append(ci_mec5)
                                            i = lista_empleados.index(aux)
                                            lista_empleados[i]._equipo = nbr_eq
                                            print("Quinto mecánico agregado correctamente")
                                            ci_mec6 = int(input("Ingrese la CI del sexto mecánico: "))
                                            aux = Mecanico(ci_mec6, None, None, None, None, None, None,None, None)
                                            if aux not in lista_empleados:
                                                print("No se ha encontrado al mecánico proporcionado.")
                                            else:
                                                lista_ci_empleado_eq.append(ci_mec6)
                                                i = lista_empleados.index(aux)
                                                lista_empleados[i]._equipo = nbr_eq
                                                print("Sexto mecánico agregado correctamente")
                                                ci_mec7 = int(input("Ingrese la CI del séptimo mecánico: "))
                                                aux = Mecanico(ci_mec7, None, None, None, None, None, None,None, None)
                                                if aux not in lista_empleados:
                                                    print("No se ha encontrado al mecánico proporcionado.")
                                                else:
                                                    lista_ci_empleado_eq.append(ci_mec7)
                                                    i = lista_empleados.index(aux)
                                                    lista_empleados[i]._equipo = nbr_eq
                                                    print("Séptimo mecánico agregado correctamente")
                                                    ci_mec8 = int(input("Ingrese la CI del octavo mecánico: "))
                                                    aux = Mecanico(ci_mec1, None, None, None, None, None, None,None, None)
                                                    if aux not in lista_empleados:
                                                        print("No se ha encontrado al mecánico proporcionado.")
                                                    else:
                                                        lista_ci_empleado_eq.append(ci_mec8)
                                                        i = lista_empleados.index(aux)
                                                        lista_empleados[i]._equipo = nbr_eq
                                                        print(lista_empleados[i])
                                                        print("Octavo mecánico agregado correctamente")
                                                        ci_jef = int(input("Ingrese la CI del jefe de equipo: "))
                                                        aux = Jefe(ci_jef, None, None, None, None, None, None, None)
                                                        if aux not in lista_empleados:
                                                            print("No se ha encontrado al jefe de equipo proporcionado.")
                                                        else:
                                                            lista_ci_empleado_eq.append(ci_jef)
                                                            i = lista_empleados.index(aux)
                                                            lista_empleados[i]._equipo = nbr_eq
                                                            print("Jefe de equipo agregado correctamente")
                                                            print(lista_ci_empleado_eq)
                                                            nuevo_eq = Equipo(nbr_eq, modelo_aut_eq, lista_ci_empleado_eq)
                                                            if nuevo_eq not in lista_equipos:
                                                                lista_equipos.append(nuevo_eq)
                                                                print("Equipo agregado correctamente.")
                                                                print(lista_equipos)
                                                            else:
                                                                print("El equipo ya está registrado.")
