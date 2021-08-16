def alphabet_position_versao_1(text):
    print(text)
    alfabeto = list("abcdefghijklmnopqrstuvwxyz")
    result = ""
    for word in text:
        if word.lower() in alfabeto:
            result += str(alfabeto.index(word.lower())+1) + " "
    return result.strip()
    

def alphabet_position_versao_2(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')

def alphabet_position_original(text):
    alphabet = {"a":"1",
                "b":"2",
                "c":"3",
                "d":"4",
                "e":"5",
                "f":"6",
                "g":"7",
                "h":"8",
                "i":"9",
                "j":"10",
                "k":"11",
                "l":"12",
                "m":"13",
                "n":"14",
                "o":"15",
                "p":"16",
                "q":"17",
                "r":"18",
                "s":"19",
                "t":"20",
                "u":"21",
                "v":"22",
                "w":"23",
                "x":"24",
                "y":"25",
                "z":"26"}
    
    new_text = ""
    text = text.lower().strip() 
    for word in text:
        if word in alphabet:
            new_text+=" "+(alphabet.get(word))

    return new_text.lstrip()
    
def main():
    print(alphabet_position_original(".The sunset sets at twelve o' clock."))
    
main()