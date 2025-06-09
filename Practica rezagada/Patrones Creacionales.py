class Logger:
    _instance = None  # Variable de clase para almacenar la única instancia

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # Crear la instancia si no existe
        return cls._instance

    def log(self, mensaje):
        print(f"Log: {mensaje}")  # Método para registrar mensajes


# Uso del Logger Singleton
logger1 = Logger()  # Primera instancia
logger2 = Logger()  # Segunda instancia
logger3 = Logger()  # Tercera instancia

# Verificamos que ambas variables apuntan a la misma instancia
print(logger1 is logger2 is logger3)  # Salida: True

# Registramos mensajes
logger1.log("Este es el primer mensaje.")
logger2.log("Este es el segundo mensaje.")
logger3.log("Este es el tercer mensaje.")
