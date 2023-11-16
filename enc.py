class Piloto:
    def __init__(self, nombre, ci, score):
        self._nombre = nombre
        self._ci = ci
        self._score = score
        
    def __repr__(self):
        return f"El piloto {self._nombre} cuyo score es {self._score}"

    def __eq__(self, otro_pil):
        return self._ci == otro_pil._ci
    
p1 = Piloto("Marcos", 123, 98)
p2 = Piloto("Julian", 222, 12)
p3 = Piloto("Martin", 132, 80)

lista_pilotos = [p1, p2, p3]
lista_cis = []

ci_piloto1 = int(input("Ingrese la CI del 1er piloto: "))
aux = Piloto(None, ci_piloto1, None)
if aux not in lista_pilotos:
    print("No se ha encontrado al piloto proporcionado.")
else:
    print("Se ha encontrado al piloto")
    lista_cis.append(ci_piloto1)
    
for i in lista_cis:
    print(i)