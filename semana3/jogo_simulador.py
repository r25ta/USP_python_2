def main():
    pass

class Balde:
    
    
    
    capacidade = 0
    volume = 0
    derramado =0
    cheio = False
    
    
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.volume = 0
        self.derramado = 0
        self.cheio = False
        
        print("construtor da classe Balde")    

    def __str__(self):
        return "__str__ do Balde"
    
    def deposita(self,volume):
        print("Deposita de Balde",volume)
        
main()

        
class Simulador:
    def __init__(self, semente):
        print("contrutor do Simulador")
    
    def sorteia(self):
        print("metodo sorteia do Simulador")
        
    def deposita(self):
        print("metodo deposita do Simulador")
        
    def finaliza(self):
        print("metodo finaliza do Simulador")

main()