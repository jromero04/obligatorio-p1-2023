class Piloto:
    def __init__(self, nombre, score):
        self._nombre = nombre
        self._score = score
        
    def __repr__(self):
        return f"El piloto {self._nombre} cuyo score es {self._score}"


def consulta_4(lista_a_ordenar):
    lista_ord = sorted(lista_a_ordenar, key=lambda piloto: piloto._score, reverse=True)
    for i in lista_ord:
        print (i)
        
p1 = Piloto("Marcos", 98)
p2 = Piloto("Julian", 12)
p3 = Piloto("Martin", 80)

lista_pilotos = [p1, p2, p3]
consulta_4(lista_pilotos)