def conta_letras(frase,contar="vogais"):
    lst_vogais = [65,69,73,79,85]
    i=0
    frase = frase.upper().replace(" ","")
    contador = 0
    while i < len(frase):
        if(contar == "consoantes"):
            flag = True
            for ascii_vogal in lst_vogais:
                ascii_palavra_frase = ord(frase[i])
                if(ascii_palavra_frase == ascii_vogal):
                    flag = False
            
            if(flag):
                contador += 1
        else:
            for ascii_vogal in lst_vogais:
                ascii_palavra_frase = ord(frase[i])
                if (ascii_palavra_frase == ascii_vogal ):
                    contador += 1
                    break
            
        i += 1                        
#    print(contador)
    return contador
""""
def main():
#    conta_letras('programamos em python')
    # deve devolver 6

#    conta_letras('programamos em python', 'vogais')
    # deve devolver 6

#    conta_letras('programamos em python', 'consoantes')
    # deve devolver 13
    conta_letras("a b c d e f g h i j k l m n o p q r s t u v w x y z","consoantes")
    print(conta_letras("oi"))
main()
"""