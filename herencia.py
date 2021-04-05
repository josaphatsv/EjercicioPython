class Persona:
        def __init__(self, nombre, edad):
            self.nombre =nombre 
            self.edad = edad 
        def __str__(self):
            return "Nombre: " + self.nombre +", edad: "+str(self.edad)
    
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre,edad)
        self.sueldo= sueldo
    def __str__(self):
        return super().__str__()+", sueldo: "+str(self.sueldo)
        
persona = Persona("Juan", 28)
print(persona)
empleado=Empleado("Josue", 40, 1000.00)
print(empleado)
empleado.nombre="Josaphat"
empleado.sueldo=1200.00
print(empleado)