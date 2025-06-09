#ejemplo de patron de comportamiento Observer

class Suscriptor:
    def actualizar(self, mensaje):
        pass

class Usuario(Suscriptor):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"{self.nombre} recibió notificación: {mensaje}")

class CanalYouTube:
    def __init__(self, nombre):
        self.nombre = nombre
        self.suscriptores = []

    def suscribir(self, usuario):
        self.suscriptores.append(usuario)

    def desuscribir(self, usuario):
        self.suscriptores.remove(usuario)

    def subir_video(self, titulo):
        print(f" {self.nombre} subió un nuevo video: {titulo}")
        self.notificar_todos(f"Nuevo video: {titulo}")

    def notificar_todos(self, mensaje):
        for sub in self.suscriptores:
            sub.actualizar(mensaje)

canal = CanalYouTube("Dalas Reviews")
juan = Usuario("Juan")
maria = Usuario("María")
Pepe = Usuario("Pepe")

canal.suscribir(juan)
canal.suscribir(maria)
canal.suscribir(Pepe)

canal.desuscribir(Pepe)


canal.subir_video("Critica a la sirenita de Disney")
