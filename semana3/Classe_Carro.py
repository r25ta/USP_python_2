class Carro:
    def __init__(self 
                ,marca
                ,modelo
                ,cor
                ,ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.consumoMedio = 0
         
    def to_string(self):
        print("Carro de marca: %s modelo: %s cor: %s e ano: %d"%(self.marca,self.modelo,self.cor, self.ano))
        
    def consumoMedio(self,kmRodado):
        pass
        #self.consumoMedio = kmPercorrido/qtdeCombustivel
        #print("Consumo médio: %d"%(self.consumoMedio))         

def main():
    carro1 = Carro("VW","Gol GTi","Prata",1997)
    carro1.to_string()
    carro1.consumoMedio(2)
    
    carro2 = Carro("VW","Golf GTi","Prata",2000)
    carro2.to_string()
    
main()