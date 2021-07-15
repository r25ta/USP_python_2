def maiusculas(str_frase):
#   LISTA ARMAZENA CODIGO ASCII SOMENTE DE LETRAS MAIUSCULAS DE A a Z
#   SISTEMA SEPARA SOMENTE AS LETRAS MAIUSCULAS
#   FUNÃO ORD() É RESPONSAVEL POR RETORNAR CODIGO ASCII
    lst_ascii_letras_maiusculas = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
    
    i=0
    letras_maiusculas = ""
    while i < len(str_frase):
        for cod_letra_Maiuscula in lst_ascii_letras_maiusculas:
            if(ord(str_frase[i]) == cod_letra_Maiuscula ):
                letras_maiusculas += str_frase[i]
        i +=1
        
#    print(letras_maiusculas)
    return letras_maiusculas

"""
def main():
    maiusculas('Programamos em python 2?')
# deve devolver 'P'

    maiusculas('Programamos em Python 3.')
# deve devolver 'PP'

    maiusculas('PrOgRaMaMoS em python!')
# deve devolver 'PORMMS'

main()
"""