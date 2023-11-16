from datetime import datetime

from Clases.claseEmpleado import Empleado
from Clases.clasePiloto import Piloto
from Clases.claseMecanico import Mecanico
from Clases.claseJefe import Jefe

def alta_empleado(lista_empleados):
    print("Alta de empleado")

    valido = False
    while not valido:
        nbr_emp = input("Ingrese nombre: ")
        if not isinstance(nbr_emp, str) or nbr_emp.isspace() == True:
            print("Nombre no válido.")
        else:
            nombre = nbr_emp
            apell_emp = input("Ingrese apellido: ")
            if not isinstance(nbr_emp, str) or apell_emp.isspace() == True:
                print("Apellido no válido. Intente de nuevo")
            else:
                apellido = apell_emp
                ci_emp = input(
                "Ingrese la cedula, con dígito verificador y sin guiones ni espacios: "
                )
                ci_emp_int = int(ci_emp)
                if not (
                    isinstance(ci_emp_int, int) and (ci_emp_int in range(1000000, 99999999))
                ):
                    print(len(str(ci_emp)), " Cédula no válida. Intente nuevamente.")
                else:
                    cedula = ci_emp_int
                    fecha_nac_eq = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
                    anio = fecha_nac_eq[-4:]
                    try:
                        datetime.strptime(fecha_nac_eq, "%d/%m/%Y")
                        if int(anio) < 2010 and int(anio) > 1900:
                            print(fecha_nac_eq)
                            fecha_nacimiento = fecha_nac_eq
                        else:
                            print(f"El {anio} no es correcto.")
                    except:
                        print(f"La {fecha_nac_eq} es incorrecta.")
                    nacion_emp = input("Ingrese la nacionalidad: ")
                    if not isinstance(nacion_emp, str) or nacion_emp.isspace() == True:
                        print("Nacionalidad no válida. Intente nuevamente.")
                    else:
                        nacionalidad = nacion_emp
                        salario_emp = int(input("Ingrese salario: "))
                        if not isinstance(salario_emp, int) or salario_emp == 0:
                            print("Salario incorrectamente ingresado. Intente nuevamente")
                        else:
                            salario = salario_emp
                            cargo_emp = int(
                            input(
                                "Digite el numero asociado al cargo: \n 1. Piloto \n 2. Piloto de reserva \n 3. Mecánico \n 4. jefe de equipo \n "))   
                            if not cargo_emp in range(1, 5):
                                    print("Cargo incorrectamente ingresado. Intente nuevamente")
                            else:
                                if cargo_emp == 1:
                                    cargo = "Piloto"
                                    score_piloto = int(input("Ingrese el score del piloto: "))
                                    if score_piloto not in range(1, 100):
                                        print("Score ingresado de manera incorrecta.")
                                    else:
                                        score = score_piloto
                                        numero_auto = int(input("Ingrese el numero del auto: "))
                                        if numero_auto not in range(1, 100):
                                            print("Numero de auto inválido.")
                                        else:
                                            nro_auto = numero_auto
                                            nuevo_empleado = Piloto(
                                                cedula,
                                                nombre,
                                                apellido,
                                                fecha_nacimiento,
                                                nacionalidad,
                                                salario,
                                                cargo,
                                                None,
                                                score,
                                                nro_auto,
                                                0,
                                                False,
                                                False,
                                                False,
                                                False
                                            )
                                            if nuevo_empleado not in lista_empleados:
                                                lista_empleados.append(nuevo_empleado)
                                                print("Empleado agregado correctamente.")
                                            else:
                                                print("El empleado ya está registrado.")
                                            

                                if cargo_emp == 2:
                                    cargo = "Piloto de reserva"
                                    score_piloto = int(input("Ingrese el score del piloto: "))
                                    if score_piloto not in range(1, 99):
                                        print("Score ingresado de manera incorrecta.")
                                    else:
                                        score = score_piloto
                                        numero_auto = int(input("Ingrese el numero del auto: "))
                                        if numero_auto not in range(1, 99):
                                            print("Numero de auto inválido.")
                                        else:
                                            nro_auto = numero_auto
                                        nuevo_empleado = Piloto(
                                            cedula,
                                            nombre,
                                            apellido,
                                            fecha_nacimiento,
                                            nacionalidad,
                                            salario,
                                            cargo,
                                            None,
                                            score,
                                            nro_auto, 
                                            0, 
                                            False,
                                            False,
                                            False,
                                            False
                                        )
                                        if nuevo_empleado not in lista_empleados:
                                                lista_empleados.append(nuevo_empleado)
                                                print("Empleado agregado correctamente.")
                                        else:
                                            print("El empleado ya está registrado.")

                                elif cargo_emp == 3:
                                    cargo = "Mecánico"
                                    score_mec = int(input("Ingrese el score del mecanico: "))
                                    if score_mec not in range(1, 100):
                                        print("Informacion invalida")
                                    else:
                                        score = score_mec
                                    nuevo_empleado = Mecanico(
                                        cedula,
                                        nombre,
                                        apellido,
                                        fecha_nacimiento,
                                        nacionalidad,
                                        salario,
                                        cargo,
                                        None,
                                        score,
                                    )
                                    if nuevo_empleado not in lista_empleados:
                                        lista_empleados.append(nuevo_empleado)
                                        print("Empleado agregado correctamente.")
                                    else:
                                        print("El empleado ya está registrado.")

                                elif cargo_emp == 4:
                                    cargo = "Jefe de equipo"
                                    nuevo_empleado = Jefe(
                                        cedula, nombre, apellido, fecha_nacimiento, nacionalidad, salario, cargo, None
                                    )
                                    if nuevo_empleado not in lista_empleados:
                                        lista_empleados.append(nuevo_empleado)
                                        print("Empleado agregado correctamente.")
                                    else:
                                       print("El empleado ya está registrado.")
        valido = True