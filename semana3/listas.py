lst = [1,2,[3,4],[5,[100,200,["Ronaldo"]],23,11],1,7]
#IMPRIMIR RONALDO
print(lst[3][1][2])


lst1 = [1,2,3,4,"Five","Six","Seven",8,9,"Ten"]
#IMPRIME O INDICE 2 E TUDO DEPOIS
print(lst1[2:])

#IMPRIME TUDO ATÉ O ELEMENTO DO INDICE 5, não imprime o conteudo do indice 5
print(lst1[:5])

#METODO APPEND ADICIONA CONTEÚDO NO FINAL DA LISTA
lst1.append(11)
print(lst1)

#METODO POP RETIRA ELEMENTO DA LISTA
#METODO POP SEM ESPECIFICAR O INDICE RETIRAR O ULTIMO ELEMENTO DA LISTA
lst1.append("ULTIMO ELEMENTO")
print(lst1)
lst1.pop()
print("metodo pop() remove o ultimo elemento", lst1)

lst1.pop(2)
print("metodo pop(2) remove indice 2", lst1)

lst1.append(3)
lst1.reverse()
print("Metodo reverse()",lst1)

#Metodo sort() não classifica uma lista quando os elementos tem tipos diferentes (STR e INT)
lst1.sort()
print("Metodo sort() ordena",lst1)


