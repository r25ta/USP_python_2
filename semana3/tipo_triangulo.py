class Triangulo():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return (self.a + self.b + self.c)
    
    def tipo_lado(self):
        if (self.a == self.b == self.c):    
            return "equilátero"

        elif((self.a == self.b) or (self.a==self.c) or (self.b==self.c)):
            return "isósceles"
        else:
            return "escaleno"
        
        
if __name__ == "__main__":
    triangulo = Triangulo(5,5,5)
    print(triangulo.a)
    print(triangulo.b)
    print(triangulo.c)
    print(triangulo.perimetro())
    print(triangulo.tipo_lado())

    triangulo1 = Triangulo(1,2,3)
    print(triangulo1.a)
    print(triangulo1.b)
    print(triangulo1.c)
    print(triangulo1.perimetro())
    print(triangulo1.tipo_lado())
    
    triangulo2 = Triangulo(10,10,30)
    print(triangulo2.a)
    print(triangulo2.b)
    print(triangulo2.c)
    print(triangulo2.perimetro())
    print(triangulo2.tipo_lado())

    triangulo3 = Triangulo(30,10,30)
    print(triangulo3.a)
    print(triangulo3.b)
    print(triangulo3.c)
    print(triangulo3.perimetro())
    print(triangulo3.tipo_lado())

    triangulo4 = Triangulo(30,10,10)
    print(triangulo4.a)
    print(triangulo4.b)
    print(triangulo4.c)
    print(triangulo4.perimetro())
    print(triangulo4.tipo_lado())