def nome_mais_curto(matriz):
    nome = ""
    menor_nome = ""
    for x in matriz:
        nome = str(x).strip()
    
        if(menor_nome!=nome):
            if(menor_nome==""):
                menor_nome = nome
            elif (len(menor_nome)>len(nome)):
                menor_nome = nome
            
    return menor_nome.capitalize()            
    
def main():
    matriz = ["JOÃO", "   Maria  ", "josé    ", "ANtôNIo", "anA             ","ANDRé"]  
    menor_nome = nome_mais_curto(matriz)
    print(menor_nome)
    
main()  