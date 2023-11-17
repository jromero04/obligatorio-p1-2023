from Clases.clasePiloto import Piloto
from Clases.claseJefe import Jefe
from Clases.claseEquipo import Equipo as e




def empleados_registrados(lista_empleados, lista_empleados_registrados, lista_equipos):
   for emp in lista_empleados:
      for equipo in lista_equipos:
         if emp in equipo._ci_empleado_eq:
            print(equipo)
            lista_empleados_registrados.append(emp)
            print(f"Los empleados registrados son {lista_empleados_registrados}")


#def pilotos_lesionados(lista_equipos, lista_autos, lista_empleados_registrados):
 #  pilotos_les = input("Ingrese el numero de todos los pilotos lesionados separados entre comas.")
  # lista_lesionados = pilotos_les.split(",")
   #print(lista_lesionados)
   
   ##pasar identificador de nro a ci

   #for pil_les in lista_lesionados:
    #  if pil_les in 
   
   #elif piloto_les == "S":
     #       cual = int(input("Ingrese el numero del piloto lesionado: "))
      #      pil_les = Piloto(None, None, None, None, None, None, None, None, cual, None, None, None, None, None)
       #     if pil_les in lista_empleados:
        #        print(f"El piloto numero {cual} está lesionado")
         #       lista_lesionados.append(pil_les)
          #      print(lista_lesionados)
           #     #corre = False
            #    terminar_posta = False
             #   while not terminar_posta:
              #      otro = input("¿Hay otro piloto lesionado? S/N")
               #     if otro == "S":
                #        cual = int(input("Ingrese el numero del piloto lesionado: "))
                 #       pil_les = Piloto(None, None, None, None, None, None, None, None, cual, None, None, None, None, None)
                  #      if pil_les in lista_empleados:
                   #         print(f"El piloto numero {cual} está lesionado")
                    #        lista_lesionados.append(pil_les)
                     #       for i in lista_lesionados:
                      #          print(i)
                       #     #corre = False
                    #else:
                     #   print("No hay ningun otro lesionado")
                      #  terminar_posta = True
                       # termine = True
    
                        
#def pilotos_abandonan(lista_equipos, lista_autos, lista_empleados):
 #   termine = False
  #  while not termine:
   #     piloto_abandono = input("¿Algún piloto abandonó en el transcurso de la carrera? S/N")
    #    if piloto_abandono == "N":
     #       print("Ningún piloto abandonó.")
      #  elif piloto_abandono == "S":
       #     cual = int(input("Ingrese el numero del piloto que abandonó: "))
        #    pil_ab = Piloto(None, None, None, None, None, None, None, None, cual, None, None, None, None, None)
         #   if pil_ab in lista_empleados:
          #      print(f"El piloto numero {cual} abandonó la carrera")