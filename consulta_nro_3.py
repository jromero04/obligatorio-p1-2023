from Clases.clasePiloto import Piloto

def consulta_3(lista_a_buscar):
    lista_filtrada = [obj for obj in lista_a_buscar if isinstance(obj, Piloto)]
    
    lista_ord = sorted(lista_filtrada, key=lambda piloto: piloto._salario, reverse=True)
    for i in lista_ord:
        print (i)
        
        
#Tengo que ver como crear una lista de todos los pilotos que vayan a correr la carrera
# y ahí la lista que le paso es esa