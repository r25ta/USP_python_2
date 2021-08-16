def incomodam(n,item=1, palavra=""):
    if(n>=item):
        palavra +="incomodam "
        return incomodam(n, item+1, palavra)
    else:
        return palavra
        
def elefantes(n, item=1, frase=""):
    if(n>=item):
        if(item==1):
            frase= "Um elefante incomoda muita gente\n" 
            return elefantes(n,item + 1,frase)
        
        else:
            frase += str(item) + " elefantes " + incomodam(item) + "muito mais\n"
            if(n>item):
                frase +=str(item) + " elefantes incomodam muita gente\n"
            
            return elefantes(n,item + 1,frase)
            
    else:
        return frase    
"""    
if __name__=="__main__":
    print(elefantes(100))
#    print(elefantes(2))
#    print(elefantes(1))
#    print(elefantes(0))
"""