class Caja:
    def __init__(self,largo,ancho,alto):
        self.largo=largo
        self.ancho=ancho
        self.alto=alto
    
    def volumen(self):
        return self.largo*self.ancho*self.alto
    
largo=float(input("Ingrese el largo de la caja: "))
ancho=float(input("Ingrese el ancho de la caja: "))
alto=float(input("Ingrese la altura de la caja: "))
caja=Caja(largo,ancho,alto)
print("El volumen de la caja es:",caja.volumen())
