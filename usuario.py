class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.crear_usuario = "Sin crear"
        self.registrar_usuario = "Sin registrar"
        
    def crear(self):
        self.crear_usuario = "Creado"

    def registrar(self):
        self.registrar_usuario = "Registrado"

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        