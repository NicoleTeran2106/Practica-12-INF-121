#Ejemplo patron creacional Singleton
#El patrón Singleton asegura que una clase tenga una única instancia y proporciona un punto de acceso global a ella.
class Logger:
    _instance = None  

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  
        return cls._instance

    def log(self, mensaje):
        print(f"Log: {mensaje}")  


logger1 = Logger()  
logger2 = Logger() 
logger3 = Logger()  

print(logger1 is logger2 is logger3)  

logger1.log("Este es el primer mensaje.")
logger2.log("Este es el segundo mensaje.")
logger3.log("Este es el tercer mensaje.")
