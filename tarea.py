class Tarea:
    def __init__(self, titulo, responsable, descripcion, comentarios):
        self.titulo = titulo
        self.responsable = responsable
        self.estado = "pendiente"
        self.descripcion = descripcion
        self.comentarios = comentarios
        self.crear_tarea = "Sin crear"
        
    def crear(self):
        self.crear_tarea = "Creada"

    def completar(self, nuevo_estado):
        self.estado = nuevo_estado

    def reasignar(self, nuevo_responsable):
        self.responsable = nuevo_responsable

    def mostrar(self):
        print(f"Título: {self.titulo}, Estado: {self.estado}, Responsable: {self.responsable}")