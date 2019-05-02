# coding: utf-8

# Abel Antunes de Lima Neto - 117210287

''' Recebe um numero e retorna se ele eh ou nao
uma potencia de 2'''
def ehPotencia2 (numero):

    for i in range((numero/2) + 1):
        if (2 ** i ==  numero):
            
            return True
    return False

''' Recebe o dado digitado e retorna um
dicionario com o indice de cada paridade
e seus valores (0 ou 1)'''
def retornaParidades (entrada):
    
    dictSaida = {}
    indice = 0
    for b in entrada:
        indice += 1
        if (ehPotencia2(indice)):
            dictSaida[indice] = b
    
    return dictSaida

''' Recebe o dado de entrada e retorna um dicionario 
com o indice de cada paridade e a soma dos valores que
ela cobre'''
def retornaDictSomaParidade (dado):
    
    dictSomaParidades = {}
    paridades = retornaParidades(dado)
    for i in paridades.keys():
        valem = True
        cont = i
        soma = 0
        for num in range((i - 1), len(dado)):
            if (num != (i - 1) and valem):
                soma += int(dado[num])
            
            cont -= 1
           
            if (cont == 0):
                cont = i
                if (valem):
                    valem = False
                else:
                    valem = True
        dictSomaParidades[i] = soma
    
    return dictSomaParidades

''' Recebe o dado de entrada e executa as duas funcoes a cima
para obter os dicionarios com os indices e valores das paridades e
com indices e somas dos valores cobertos por aquelas paridades,
apos isso eh so verificar se a paridade eh 0 quando a soma eh par
ou se eh 1 quando a soma eh impar, caso contrario, possui erro.'''
def verifica (dado):
    
    dictParidadeIndice = retornaParidades(dado)
    dictSomaIndice = retornaDictSomaParidade(dado)
    erros = []
    #print dictParidadeIndice
    #print dictSomaIndice

    for key in dictSomaIndice:
        if ((dictSomaIndice[key] % 2 == 0) and (dictParidadeIndice[key] == "1") or 
                (dictSomaIndice[key] % 2 == 1) and (dictParidadeIndice[key] == "0")):
            
            erros.append(key)
    
    return erros


''' Esse metodo de correcao corrige um bit errado
ver quais paridades estao erradas e qual o bit em comum essas paridades
abrangem, esse bit eh o errado, apos isso inverte seu valor'''
def corrige (dado, erros):
    
    soma = 0
    for i in erros:
        soma += i

    if ((soma > len(dado))):
        saida = "Impossivel de corrigir."

    else:
        if (dado[soma - 1] == "1"):
            saida = dado[0 : (soma - 1)] + "0"
        else:
            saida = dado[0 : (soma - 1)] + "1"

        if len(saida) < len(dado):
            saida += dado[soma : len(dado)]
    
    return saida

''' Desconcidera os verificadores de paridade e retorna apenas o dado
enviado'''
def retornaDado (dado):
    
    saida = ""
    dictParidades = retornaParidades(dado)
    for i in range(len(dado)):
        if ((i + 1) not in dictParidades.keys()):
            saida += dado[i]
    
    return saida

''' Verifica se a entrada eh composta apenas por 0s e 1s'''
def verificaEntrada (dado):
    
    for i in dado:
        if (i != "1" and i != "0"):
            return False

    return True

def menu ():
    ent = raw_input ("Digite um dado para ser verificado (Dado ja com paridade): ")
    
    if (verificaEntrada(ent)):
        paridades = retornaParidades(ent)

        print "\nIndices que possuem verificadores de paridade(Comeca de 1): " + str(paridades.keys())
        erros = verifica(ent)

        print "Indices com paridades erradas(Comeca de 1): " + str(erros)

        if (len(erros) > 0):
            novo = corrige(ent, erros)

            if (novo != "Impossivel de corrigir."):
                print "Dado corrigido: " + novo
                print "Informacao do dado: " + retornaDado(novo)
        
            else:
                print novo
        else:
            print "Informacao do dado: " + retornaDado(ent)

    else: 
        print "Digite um valor binario. \n"
        menu()
    
menu()
