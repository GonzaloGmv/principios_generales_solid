import threading
import time
import random
from queue import Queue


class DataBaseManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.cola_pedidos = Queue()
        self.productores = []
        self.consumidores = []

    # Función para el productor (pedido)
    def generar_pedido(self, cliente):
        pizzas = ["Pepperoni", "Margarita", "Hawaiana", "Vegetariana"]
        pizza = random.choice(pizzas)
        tamaño = random.choice(["Pequeña", "Mediana", "Grande"])
        cantidad = random.randint(1, 5)
        precio = random.uniform(5, 20)
        pedido = {
            "Cliente": cliente,
            "Pizza": pizza,
            "Tamaño": tamaño,
            "Cantidad": cantidad,
            "Precio": precio
        }
        self.cola_pedidos.put(pedido)
        print(f"{cliente} ha realizado un pedido: {cantidad} pizza(s) de {tamaño} {pizza}")

    # Función para el consumidor (cliente)
    def servir_pedido(self):
        while True:
            pedido = self.cola_pedidos.get()
            if pedido is None:
                break
            tiempo_servicio = random.uniform(0.5, 2.0)
            time.sleep(tiempo_servicio)
            print(f"Pedido para {pedido['Cliente']} servido en {tiempo_servicio:.2f} segundos")

    # Iniciar productores (clientes)
    def iniciar_productores(self, num_productores):
        for i in range(num_productores):
            cliente = f"Cliente-{i + 1}"
            productor = threading.Thread(target=self.generar_pedido, args=(cliente,))
            self.productores.append(productor)

    # Iniciar consumidores (empleados)
    def iniciar_consumidores(self, num_consumidores):
        for _ in range(num_consumidores):
            consumidor = threading.Thread(target=self.servir_pedido)
            self.consumidores.append(consumidor)

    # Iniciar la simulación
    def iniciar_simulacion(self):
        for productor in self.productores:
            productor.start()

        for consumidor in self.consumidores:
            consumidor.start()

    # Esperar a que todos los productores terminen
    def esperar_productores(self):
        for productor in self.productores:
            productor.join()

    # Indicar a los consumidores que no hay más pedidos y esperar a que terminen
    def terminar_consumidores(self):
        for _ in range(len(self.consumidores)):
            self.cola_pedidos.put(None)

        for consumidor in self.consumidores:
            consumidor.join()