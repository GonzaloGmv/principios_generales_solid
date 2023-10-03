import csv
import random
import string

# Función para generar un nombre aleatorio
def generar_nombre():
    nombres = ["Juan", "María", "Carlos", "Laura", "Pedro", "Ana", "Luis", "Sofía", "Diego", "Valeria"]
    apellidos = ["Gómez", "López", "Martínez", "Fernández", "Rodríguez", "Pérez", "Torres", "Sánchez", "Ramírez", "Díaz"]
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    return f"{nombre} {apellido}"

# Abrir un archivo CSV en modo escritura
with open('clientes.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')

    # Escribir la fila de encabezado
    writer.writerow(['Nombre', 'Apellido', 'Dinero', 'Direccion', 'Telefono', 'Email', 'Password', 'N_Pedidos'])

    # Generar datos ficticios para 100 clientes
    for _ in range(100):
        nombre_apellido = generar_nombre()
        dinero = round(random.uniform(100, 10000), 2)
        direccion = f"Calle {random.randint(1, 100)}, Ciudad"
        telefono = ''.join(random.choices(string.digits, k=10))
        email = f"{nombre_apellido.split()[0].lower()}@example.com"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        n_pedidos = random.randint(1, 10)

        # Escribir los datos del cliente en el archivo CSV
        writer.writerow([nombre_apellido.split()[0], nombre_apellido.split()[1], dinero, direccion, telefono, email, password, n_pedidos])

print("Archivo CSV 'clientes.csv' generado con éxito.")
