'''Creación de una clase en Python que representa una matriz.
Para este ejercicio, deberás crear una clase que representa una matriz. Las operaciones que esta clase debe permitir son la creación de una matriz a partir de una lista de listas, la impresión de la matriz en una forma legible, y el cálculo de la transpuesta de la matriz. Asegúrate de que cada método tenga una única responsabilidad.'''

class Matriz:
    def __init__(self, elementos):
        self.elementos = elementos

class Transpuesta(Matriz):
    def __init__(self, elementos):
        super().__init__(elementos)
        
    def transpuesta(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))])
    
class Imprimir(Matriz):
    def __init__(self, elementos):
        super().__init__(elementos)
        
    def imprimir(self):
        for fila in self.elementos:
            print(fila)

class Lanzador(Imprimir, Transpuesta):
    def __init__(self):
        self.elementos = []
        self.can_filas = int(input("Ingrese la cantidad de filas: "))
        self.can_columnas = int(input("Ingrese la cantidad de columnas: "))
        self.crear_matriz()
        super().__init__(self.elementos)
    
    def crear_matriz(self):
        for i in range(self.can_filas):
            fila = []
            for j in range(self.can_columnas):
                fila.append(int(input("Ingrese el elemento " + str(i) + " " + str(j) + ": ")))
            self.elementos.append(fila)
    
    def lanzar(self):
        print("La matriz es: ")
        self.imprimir()
        print("La transpuesta es: ")
        self.transpuesta()
        self.imprimir()



class Main:
    def __init__(self):
        self.lanzador = Lanzador()
        self.lanzador.lanzar()

if __name__ == "__main__":
    Main()



