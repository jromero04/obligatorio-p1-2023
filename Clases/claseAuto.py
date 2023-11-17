#Los datos de un auto son: el modelo, su score (mismo criterio que en los casos anteriores) y color.

class Auto:
    def __init__(self, modelo, score, color):
        self._modelo = modelo
        self._score = score
        self._color = color

    def __eq__(self, otro_auto):
        return self._modelo == otro_auto._modelo

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo
        return nuevo_modelo
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, nuevo_score):
        self._score = nuevo_score
        return nuevo_score
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def pintar(self, nuevo_color):
        self._color = nuevo_color
        return nuevo_color