# Make questions about relatives and presents a summary
""" Das Ziel: durch Induktive Rationale entscheiden Relationen
zwischen zwei beliebgen Namen enthalten in Antworten.
Sei zwei Antworten A1, A2 = P1.Name1, P2.Name2



"""
def iniciar():
    nome = input("Qual o seu nome?\n  ")
    print(saud(nome))
    print(avos(nome))
    

def saud(seu_nome, bom = "Bom dia", /):
    return f"{bom}, {seu_nome}"


def avos(seu_nome):
    F = ["Qual o seu nome?",  "Qual a sua idade?", "Qual o nome da sua mãe?",
         "Qual nome da mãe da sua mãe?", "Qual o nome da sua filha?",
         "Qual o nome do seu pai?", "Qual o nome da mãe do seu pai?"]
    T = ("seu nome", "sua idade", "sua mãe", "avó materna", "sua filha",
         "seu pai", "avó paterna")
    N = []
    for i in range(len(F)):
        r = str(input(F[i] + "\n"))
        N.append(r)

    W = {T[x]:N[x] for x in range(len(T))}

    return W
                
if __name__ == '__main__':
    #print(avos())
    print(iniciar())
