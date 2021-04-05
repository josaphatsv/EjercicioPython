class Operaciones:
    """Clase Arimetica para realizar las operaciones de sumar, restar, etc.."""
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
    
    def sumar(self):
        """Se realiza la operacion con los atributos de la clase"""
        return self.op1 + self.op2
    
#Creamos un nuevo objeto
aritmetica = Operaciones(2,4)
print("Restulado de la suma: ",aritmetica.sumar())


        