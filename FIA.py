from datetime import datetime

from Clases.claseEmpleado import Empleado
from Clases.claseEquipo import Equipo
from Clases.claseAuto import Auto
from Clases.clasePiloto import Piloto
from Clases.claseMecanico import Mecanico
from Clases.claseJefe import Jefe

class Fia:
    def __init__(self):
        pass
        

    def alta_empleado(self, lista_empleados):
            print("Alta de empleado")

            valido = False
            while not valido:
                nbr_emp = input("Ingrese nombre: ")
                try:
                    int(nbr_emp)
                    print("Nombre no válido.")
                    break
                except ValueError:
                    if nbr_emp == "":
                        print("Nombre no válido.")
                        break
                    else:
                        nombre = nbr_emp
                        apell_emp = input("Ingrese apellido: ")
                        try:
                            int(apell_emp)
                            print("Apellido no válido.")
                            break
                        except ValueError:
                            if apell_emp == "":
                                print("Apellido no válido.")
                                break
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
                                if int(anio) < 2010 and int(anio) > 1800:
                                    fecha_nacimiento = fecha_nac_eq
                                else:
                                    print(f"El {anio} no es correcto.")
                                    break
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
        
    def alta_auto(self, lista_autos):
        print("Alta de auto \n")
        car_model = input("Ingrese el modelo: ")     
        if car_model == " ":
            print("Modelo ingresado incorrectamente")
        else:
            modelo = car_model
            año_auto = int(input("Ingrese el año del auto: "))
            if año_auto not in range(1850, 2024):
                print("Año ingresado inválido")
            else:
                año = año_auto
                car_score = int(input("Ingrese el score del auto: "))
                if car_score  not in range(1, 100):
                    print("Score ingresado incorrectamente")
                else:
                    score = car_score
                    nuevo_auto = Auto(modelo, año, score)
                    if nuevo_auto not in lista_autos:
                        lista_autos.append(nuevo_auto)
                        print("Auto agregado correctamente.")
                    else:
                        print("El auto ya está registrado.")
    
    def alta_equipo(self, lista_equipos, lista_autos, lista_empleados):
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
                                                                nuevo_eq = Equipo(nbr_eq, modelo_aut_eq, lista_ci_empleado_eq)
                                                                if nuevo_eq not in lista_equipos:
                                                                    lista_equipos.append(nuevo_eq)
                                                                    print("Equipo agregado correctamente.")
                                                                else:
                                                                    print("El equipo ya está registrado.")
                                                                    

    
    lista_habilitados = []

    def pilotos_lesionados(self, lista_empleados_registrados, lista_habilitados, score_final):
        respuesta = input("¿Hay pilotos lesionados? (s/n): ")
        if respuesta.lower() != 's':
            print("No hay pilotos lesionados.")
            return

        pilotos_les = input("Ingrese el numero de todos los pilotos lesionados separados entre comas: ")
        lista_lesionados = pilotos_les.split(",")
        print(lista_lesionados)
        
        for n_pil in lista_lesionados:
            try:
                paux = next(emp for emp in lista_empleados_registrados if isinstance(emp, Piloto) and str(emp._nro_auto) == n_pil)
                lista_habilitados.append(paux)
            except StopIteration:
                print(f"No se encontró un piloto con el número {n_pil} en la lista de empleados registrados.")
        print(lista_habilitados)

    def pilotos_abandonan(self, lista_habilitados, score_final):
        respuesta = input("¿Algun piloto abandonó en el transcurso de la carrera? (s/n): ")
        if respuesta.lower() != 's':
            print("No hay pilotos que abandonaron.")
            return

        pilotos_abandonan = input("Ingrese el numero de todos los pilotos que abandonan separados entre comas: ")
        lista_abandonan = pilotos_abandonan.split(",")
        print(lista_abandonan)

        lista_habilitados[:] = [emp for emp in lista_habilitados if isinstance(emp, Piloto) and str(emp._nro_auto) not in lista_abandonan]
        print("Los pilotos habilitados para correr son", lista_habilitados)

    def calcular_suma_score_mecanicos(self, lista_empleados_registrados, lista_equipos):
        suma_score_mecanicos = 0
        for equipo in lista_equipos:
            for cedula in equipo._ci_empleado_eq:
                try:
                    emp = next(emp for emp in lista_empleados_registrados if emp._cedula == cedula)
                    if isinstance(emp, Mecanico):
                        suma_score_mecanicos += emp._score
                except StopIteration:
                    print(f"No se encontró un empleado con la cédula {cedula} en la lista de empleados registrados.")
        return suma_score_mecanicos

    def calcular_suma_score_pilotos(self, lista_empleados_registrados, lista_equipos):
        suma_score_pilotos = 0
        for equipo in lista_equipos:
            for cedula in equipo._ci_empleado_eq:
                try:
                    emp = next(emp for emp in lista_empleados_registrados if emp._cedula == cedula)
                    if isinstance(emp, Piloto):
                        suma_score_pilotos += emp._score
                except StopIteration:
                    print(f"No se encontró un empleado con la cédula {cedula} en la lista de empleados registrados.")
        return suma_score_pilotos

    def obtener_scores_autos_equipos(self, lista_equipos, lista_autos):
        suma_score_autos = 0
        for equipo in lista_equipos:
            if isinstance(equipo, Equipo):
                modelo_auto_equipo = equipo._modelo_aut_eq
                for auto in lista_autos:
                    if auto._modelo == modelo_auto_equipo:
                        suma_score_autos += auto._score
                        break
                else:
                    print(f"No se encontró un auto con el modelo {modelo_auto_equipo}.")
        return suma_score_autos
    
    def empleados_registrados(self, lista_empleados, lista_empleados_registrados, lista_equipos):
        for emp in lista_empleados:
            if isinstance(emp, Piloto):
                cedula = emp._cedula
            elif isinstance(emp, Jefe):
                cedula = emp._cedula
            elif isinstance(emp, Mecanico):
                cedula = emp._cedula
            else:
                continue

            for equipo in lista_equipos:
                if cedula in equipo._ci_empleado_eq and emp not in lista_empleados_registrados:
                    lista_empleados_registrados.append(emp)
        print(f"Los empleados registrados son {lista_empleados_registrados}")

    def simular_carrera(self, lista_empleados_registrados, lista_equipos, lista_autos, puntos_equipos=None):
    # Crear un diccionario para almacenar los puntos totales de cada equipo si no se proporciona
        if puntos_equipos is None:
            puntos_equipos = {equipo._nombre_eq: 0 for equipo in lista_equipos}
        
        # Asignar puntos según la posición
        puntos_por_posicion = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
        
        # Crear una lista para almacenar los scores finales de cada equipo en esta carrera
        scores_finales = []
        
        for equipo in lista_equipos:
            suma_score_mecanicos = self.calcular_suma_score_mecanicos(lista_empleados_registrados, [equipo])
            suma_score_pilotos = self.calcular_suma_score_pilotos(lista_empleados_registrados, [equipo])
            suma_score_autos = self.obtener_scores_autos_equipos([equipo], lista_autos)
            
            score_final = suma_score_mecanicos + suma_score_pilotos + suma_score_autos
            
            # Añadir el score final y el nombre del equipo a la lista
            scores_finales.append((score_final, equipo._nombre_eq))
        
        # Ordenar la lista de scores finales en orden ascendente
        scores_finales.sort()
        
        # Actualizar los puntos de los equipos según su posición en esta carrera
        for i in range(len(scores_finales)):
            score_final, nombre_equipo = scores_finales[i]
            puntos = puntos_por_posicion[i] if i < len(puntos_por_posicion) else 0
            puntos_equipos[nombre_equipo] += puntos
        
        print("El campeonato de constructores está de la siguiente manera:")
        for nombre_equipo, puntos in puntos_equipos.items():
            print(f"Equipo {nombre_equipo}: {puntos} puntos")
        
        return puntos_equipos
          
    def consulta_3(self, lista_a_buscar):
        lista_filtrada = [obj for obj in lista_a_buscar if isinstance(obj, Piloto)]
        
        lista_ord = sorted(lista_filtrada, key=lambda piloto: piloto._salario, reverse=True)
        for i in lista_ord:
            print (i)
            
    def consulta_4(self, lista_a_ordenar):
        lista_filtrada = [obj for obj in lista_a_ordenar if isinstance(obj, Piloto)]
        
        lista_ord = sorted(lista_filtrada, key=lambda piloto: piloto._score, reverse=True)
        for i in lista_ord:
            print (i)
            
    def consulta_5(self, lista_para_buscar):
        lista_filtrada = [obj for obj in lista_para_buscar if isinstance(obj, Jefe)]
        for i in lista_filtrada:
            print(i)
