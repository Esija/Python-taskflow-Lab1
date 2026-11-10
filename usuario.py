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
        
    def obtener_nombre_concreto(self):
        if self.nombre == "David":
            print(f"Las tareas de {self.nombre} son: Tarea 1, Tarea 2, Tarea 3")
        else:
            print(f"No hay tareas asignadas a {self.nombre}")
    
    def obtener_tareas_de_cualquier_usuario(self, nombre_usuario):
        if self.nombre == nombre_usuario:
            print(f"Las tareas de {self.nombre} son: Tarea 1, Tarea 2, Tarea 3")
        else:
            print(f"No hay tareas asignadas a {nombre_usuario}")
    