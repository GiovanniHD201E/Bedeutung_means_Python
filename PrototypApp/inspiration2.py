import random

Optionen1 = "VG", "Vic", "Victor"
Optionen2 = "Angela de Sá", "Angela"


def Enfim():
    for n in range(5*len(Optionen1)*len(Optionen2)):
        texto1 = str(random.choice(Optionen1))
        texto2 = str(random.choice(Optionen2))
        if len(texto1) == len(texto2):
            print("\nTentativa", (n + 1), "\n")
            print(texto1)
            print(texto2)
            return print(texto1, texto2)
        else:
            print("\nTentativa", (n + 1), "\n")
            print(texto2)
            print(texto1)
    return ("Foram feitas", (n+1), "tentativas sem sucesso")

    
