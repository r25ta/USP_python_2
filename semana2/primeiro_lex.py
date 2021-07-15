"""ESCREVA UMA FUNÇÃO QUE RECEBE UM ARRAY DE STRINGS COMO PARAMETRO 
    E DEVOLVE O PRIMEIRO STRING NA ORDEM LEXICOGRÁFICA,
    IGNORANDO-SE LETRAS MAIUSCULAS E MINÚSCULAS"""
def primeiro_lex(lista):
    menor_nome=""
    n_str1=0
    for item in lista:
        item = item.strip()
        if(menor_nome==""):
            menor_nome=item
            n_str1 = ord(menor_nome[0])
            
        if(menor_nome!=item):
            n_str2 = ord(item[0])
            if(n_str1 > n_str2):
                menor_nome=item
                n_str1 = n_str2
                
            elif(n_str1 == n_str2):
                x=0
                while x < len(menor_nome):                    
                    if(ord(menor_nome[x]) > ord(item[x])):
                        menor_nome = item
                        n_str1 = ord(item[x])
                        break
                    
                    elif(ord(menor_nome[x]) < ord(item[x])):
                        break
                    
                    x +=1
    return menor_nome
"""
def main():
    print(primeiro_lex(['AAAAAAAAAAAAA','b','Bárbara', 'JOSÉ  ', 'Bill']))   
    print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))   
    print(primeiro_lex(['AAAAAA', 'b']))   

main()

#Implementar funçao de teste
def testa_menor_string():
    teste_pontual(["ana","maria","José","Valdemar"],"ana")
    pass
"""
