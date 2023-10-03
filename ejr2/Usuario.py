class Usuario:
    def __init__(self, nombre, apellido, dinero, direccion, telefono, email, password, n_pedidos):
        self.nombre = nombre
        self.apellido = apellido
        self.dinero = dinero
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.password = password
        self.n_pedidos = n_pedidos
        
    def __str__(self):
        return f"Usuario: {self.nombre}, {self.apellido}, {self.dinero}, {self.direccion}, {self.telefono}, {self.email}, {self.password}, {self.n_pedidos}"
    