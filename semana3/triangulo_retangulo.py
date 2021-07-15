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
        
    def retangulo(self):
        hip = self.a
        catA = self.b
        catO = self.c
        
        if (self.b > hip):
            hip = self.b
            catA = self.a
            
        if(self.c > hip):
            hip = self.c
            catO = self.a
            catA = self.b
            
        if (hip**2 == catO**2 + catA**2):
            return True
        
        else:
            return False
        
        
if __name__ == "__main__":
    triangulo = Triangulo(5,5,5)
    print(triangulo.a)
    print(triangulo.b)
    print(triangulo.c)
    print(triangulo.perimetro())
    print(triangulo.tipo_lado())
    print(triangulo.retangulo())

    triangulo1 = Triangulo(3,5,4)
    print(triangulo1.a)
    print(triangulo1.b)
    print(triangulo1.c)
    print(triangulo1.perimetro())
    print(triangulo1.tipo_lado())
    print(triangulo1.retangulo())
    
    triangulo2 = Triangulo(10,10,30)
    print(triangulo2.a)
    print(triangulo2.b)
    print(triangulo2.c)
    print(triangulo2.perimetro())
    print(triangulo2.tipo_lado())
    print(triangulo2.retangulo())
    
    triangulo3 = Triangulo(8,17,15)
    print(triangulo3.a)
    print(triangulo3.b)
    print(triangulo3.c)
    print(triangulo3.perimetro())
    print(triangulo3.tipo_lado())
    print(triangulo3.retangulo())

    triangulo4 = Triangulo(50,30,40)
    print(triangulo4.a)
    print(triangulo4.b)
    print(triangulo4.c)
    print(triangulo4.perimetro())
    print(triangulo4.tipo_lado())
    print(triangulo4.retangulo())
    