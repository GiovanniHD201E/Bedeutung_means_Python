# Ziele: Komplexe can simple in real world werden. Three languages.
# -*- coding: utf8 -*-

N = 3

class Hörsen_has:
    def __init__(self):
        """Já viajei. Agora preciso relatar a viagem sem levantar
        sem me distrair com meus pensamentos.
        1. Tem que ter um tabuleiro 3x3
        2. Tem que haver um sistema simples e eficiente de posicionamento
        3. Tem de haver um cavalo como referência para o posicionamento
        dentro do tabuleiro.
        4. Pode haver a mimetização dos gestos para uma senha inteligente.
        5. Implemente inicialmente sem sistema de heranca.
        """

        pass
        
def movimento(So=None, *Sf, **Trajetoria):
    So = tabuleiro()[0]
    return So
    pass

def tabuleiro(tipo="quadricular", Largura=N, Altura=N):
    casas = [(x, y+1) for x in [chr(z) for z in range(97, 97 + N)]\
             for y in range(N)]
    return casas

def main():
    x = tabuleiro()
    print(x)
    So = movimento()
    print("So =", So)
    pass

if __name__ == "__main__":
    main()
    pass
