"""ESCREVA UMA FUNÇÃO QUE RECEBE UM ARRAY DE STRINGS COMO PARAMETRO 
    E DEVOLVE O PRIMEIRO STRING NA ORDEM LEXICOGRÁFICA,
    IGNORANDO-SE LETRAS MAIUSCULAS E MINÚSCULAS"""
def ordem_lexicografica(str):
    return ord(str)
    
def menor_string(lista):
    menor_nome=""
    n_str1=0
    for item in lista:
        item = item.capitalize().strip()
        if(menor_nome==""):
            menor_nome=item
            n_str1 = ordem_lexicografica(menor_nome[0])
        
        
        if(menor_nome!=item):
            n_str2 = ordem_lexicografica(item[0])
            if(n_str1 > n_str2):
                menor_nome=item
            elif(n_str1 == n_str2):
                x=0
                while x < len(menor_nome):                    
                    if(ordem_lexicografica(menor_nome[x]) > ordem_lexicografica(item[x])):
                        menor_nome = item
                        n_str1 = ordem_lexicografica(item[x])
                        break
                    
                    elif(ordem_lexicografica(menor_nome[x]) < ordem_lexicografica(item[x])):
                        break
                    
                    x +=1
    print(menor_nome)


def main():
    lista = ['AAAAAAAAAAAAA','b','Bárbara', 'JOSÉ  ', 'Bill']
    menor_string(lista)   

main()

"""#Implementar funçao de teste
def testa_menor_string():
    teste_pontual(["ana","maria","José","Valdemar"],"ana")
    pass
"""
