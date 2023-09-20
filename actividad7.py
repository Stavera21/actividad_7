from dataclasses import dataclass

@dataclass
class Elemento:
    nombre:str
    def __eq__(self,other):
        if isinstance(self,other):
            return self.nombre == other.nombre

class Conjunto:
    contador = 0
    def __init__(self,nombre:str):
        self.lista_nombres:list = []
        self.nombre:str = nombre 
        Conjunto.contador += 1
        self.__id = Conjunto.contador
    @property
    def __id(self,Elementos):
        return self.__id
    
    def contiene(self,Elemento):
        for i in self.lista_nombres:
            if Elemento == i:
                return True
            else:
                return None
    
    def agregar_elementos(self,elemento:Elemento):
        if not self.contiene(elemento):
            self.lista_nombres.append(Elemento)
    
    def unir(self, conjunto):
        for elemento in Conjunto.lista_nombres:
            self.lista_nombres.append(elemento)
    
    @classmethod
    def intersectar(self, conjunto1, conjunto2):
        nuevo_conjunto = Conjunto(f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}")
        for elemento in conjunto1.lista_nombres:
            if conjunto2.contiene(elemento):
                nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto
    
    def __str__(self):
        elementos_str = " "
        for elemento in self.lista_nombres:
            if elementos_str:
                elementos_str += ", "
            elementos_str += elemento.nombre

        return f"Conjunto {self.nombre}: ({elementos_str})"