""" Modul angel : calcula o comprimento das expressões
"""
#Ausdruck = input("Escreva uma frase curta" + " ")
#Expression = input("Agora escreva outra frase com o mesmo significado " + " ")
def länge(Ausdruck="na capital alemã. ", Expression="em Berlim. "):
    ae = []
    la = len(Ausdruck)
    ae.append(Ausdruck)
    ae.append(la)
    le = len(Expression)
    ae.append(Expression)
    ae.append(le)
    dif = la - le
    dife = "diferença = "
    ae.append(dife)
    ae.append(dif)
    return ae

"""class Funktion:
    def exemplo(self='länge()'):
        print("Ainda não temos um exemplo sobre a função )" + self + "(")

    Ajuda = "A ajuda para a Função estará disponível ainda hoje" 
"""
c1 = länge()

"""A saída após digitar l será """
# ['na capital alemã. ', 18, 'em Berlim. ', 11]
"""
Esta informação foi a primeira a integrar nosso banco de dados de expressões
equivalentes classificadas pelo comprimento.
Um exemplo do seu uso poderia ser assim:"""

linha1 = "O museu que contém parte do trabalho de Tales "
linha2 = "de Mileto fica em Berlim| "

c2 = länge(linha1, linha2)

"""que resulta em """
# ['O museu que contém parte do trabalho de Tales ', 46,
#  'de Mileto fica em Berlim| ', 26]

    


