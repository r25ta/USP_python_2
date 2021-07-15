def menor_nome(lista):
    menor_nome = ""
    for item in lista:
        item = item.strip()
        
        if menor_nome == "":
            menor_nome = item
        
        if len(menor_nome) > len(item):
            menor_nome = item
    
    return menor_nome.capitalize()

"""    
def main():
    menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
    # deve devolver 'José'

    menor_nome(['zé', ' lu', 'fê'])
    # deve devolver 'José'

    menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])
    # deve devolver José

main()
"""