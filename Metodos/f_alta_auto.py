from Clases.claseAuto import Auto

def alta_auto(lista_autos):
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
