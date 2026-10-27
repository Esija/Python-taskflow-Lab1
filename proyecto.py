class Proyecto:
    def __init__(self, titulo, responsable, descripcion, comentarios):
        self.titulo = titulo
        self.responsable = responsable
        self.estado = "pendiente"
        self.descripcion = descripcion
        self.comentarios = comentarios
        self.crear_proyecto = "Sin crear"
        
    def crear(self):
        self.crear_proyecto = "Creada"

    def completar(self):
        self.estado = "completada"

    def reasignar(self, nuevo_responsable):
        self.responsable = nuevo_responsable

    def mostrar(self):
        print(f"Título: {self.titulo}, Estado: {self.estado}, Responsable: {self.responsable}")