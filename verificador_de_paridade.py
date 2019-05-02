# coding: utf-8

# Abel Antunes de Lima Neto - 117210287
# Verificador de erros em transmissao por paridade

''' Recebe um dado e verifica se ele esta correto
olha qual o tipo de paridade usado e o a soma dos bits iguais
a 1 se a paridade for par, a soma deve ser par, se for impar
a soma deve ser impar. Caso  contrario, o dado estah errado'''
def verifica(dado, paridade):
    
    quant = 0
    for bit in dado:
        if bit == "1":
            quant += 1
        elif (bit != "0"):
            print ("\nDados devem conter apenas 1 ou 0.")
            return

    if ((paridade == 1 and quant % 2 == 1) or (paridade == 0 and quant % 2 == 0)):
        return True
    else:
        return False

def menu():
    entrada = raw_input("Deseja paridade (p)ar ou (i)mpar? (\"s\" para sair) ")

    if (entrada == "p"):
        paridade = 0
    elif (entrada == "i"):
        paridade = 1
    elif (entrada == "s"):
        return
    else:
        print ("\nDigite p para par, i para impar ou s para sair\n")
        menu()
    

    dado = raw_input ("\nDigite um dado: ")
    result = verifica(dado, paridade) 

    if (result):
        print ("\nDado correto\n")
        menu()
    else:
        print ("\nDado errado\n")
        menu()
menu()
