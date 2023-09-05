class Registro:
    def __init__(self ,Nombre,Usuario,Correo,Contraseña):
        self.Nombre = Nombre
        self.Usuario = Usuario
        self.Correo = Correo
        self.Contraseña = Contraseña
        self.Respuestas = []
        
    def responder_encuesta(self, pregunta, respuesta):
        self.respuestas_encuesta[pregunta] = respuesta
        
        
    def toDBconnection (self):
        return{
            "Nombre" : self.Nombre ,
            "Usuario" : self.Usuario ,
            "Correo" : self.Correo ,
            "Contraseña" : self.Contraseña,
            "Respuestas" : self.Respuestas
            }
            
            