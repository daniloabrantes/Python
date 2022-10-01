def palindromo(string):
    flag = False
    string_invertida = string[::-1]

    if(string == string_invertida):
        flag = True
    return flag


acao = input("Deseja iniciar o Programa?\n SIM/NAO: ")
while acao != "NAO":

    #---------------------------------------------------------------------------#
    palavra = input("Digite uma palavra: ")
    if palindromo(palavra):
        print(palavra, "é palíndromo")
    else:
        print(palavra, "não é palíndromo")
#---------------------------------------------------------------------------#
    acao = input("Deseja continuar o programa?\n SIM/NAO: ")
