from Clases.clasePiloto import Piloto

def consulta_4(lista_a_ordenar):
    lista_filtrada = [obj for obj in lista_a_ordenar if isinstance(obj, Piloto)]
    
    lista_ord = sorted(lista_filtrada, key=lambda piloto: piloto._score, reverse=True)
    for i in lista_ord:
        print (i)

#TERMINADA