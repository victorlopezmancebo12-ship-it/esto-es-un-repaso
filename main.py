class RescateDatos:
    def __init__(self, tecnicos_disponibles=3, tiempo_limite=120):
        self.tecnicos_disponibles = tecnicos_disponibles
        self.tiempo_limite = tiempo_limite
        self.tareas = [
            {"id": "A", "nombre": "Identificar servidores afectados", "duracion": 15},
            {"id": "B", "nombre": "Priorizar datos críticos", "duracion": 20},
            {"id": "C", "nombre": "Activar protocolo de recuperación", "duracion": 10},
            {"id": "D", "nombre": "Asignar técnicos a servidores", "duracion": 5},
            {"id": "E", "nombre": "Recuperar datos de servidor 1", "duracion": 30},
            {"id": "F", "nombre": "Recuperar datos de servidor 2", "duracion": 25},
            {"id": "G", "nombre": "Validar integridad de datos recuperados", "duracion": 15},
            {"id": "H", "nombre": "Generar informe preliminar para dirección", "duracion": 10},
            {"id": "I", "nombre": "Comunicar a clientes afectados", "duracion": 20},
            {"id": "J", "nombre": "Coordinar con equipo legal", "duracion": 15},
            {"id": "K", "nombre": "Preparar plan de contingencia", "duracion": 25},
        ]
        # Aquí puedes agregar más atributos según lo que necesites

if __name__ == "__main__":
    rescate = RescateDatos()
    # Aquí puedes llamar métodos para simular el rescate, mostrar cronograma, etc

    git commit "prueba"