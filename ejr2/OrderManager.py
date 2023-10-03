import csv
import os

class OrderManager:
    def __init__(self, database_manager, authenticator, payment_processor):
        self.database_manager = database_manager
        self.authenticator = authenticator
        self.payment_processor = payment_processor

        
def guardar_pedido(pedido):
    archivo_csv = "pedidos.csv"
    existe_archivo = os.path.isfile(archivo_csv)

    with open(archivo_csv, mode='a', newline='') as file:
        fieldnames = ['Cliente', 'Pizza', 'Tamaño', 'Cantidad', 'Precio']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not existe_archivo:
            writer.writeheader()

        writer.writerow(pedido)

def leer_pedidos():
    archivo_csv = "pedidos.csv"
    existe_archivo = os.path.isfile(archivo_csv)

    with open(archivo_csv, mode='r', newline='') as file:
        reader = csv.DictReader(file)

        if not existe_archivo:
            return None

        pedidos = []
        for row in reader:
            pedidos.append(row)

        return pedidos