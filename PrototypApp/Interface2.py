import random
import itertools

def at():
    n = 0
    x = [
    "Queimei a mao no fogo",
    "Ich liebe dich, meine Tochter",
    "Ich liebe dich, Vati",
    "Está doendo muito",
    "Queimei minha mao no fogo",
    "O que fazer agora",
         ]
    
    pontu = [
        '.',
        '!',
        '?',
        ':',
        ]
    
    for n in range(1):
        p = random.choice(x) + random.choice(pontu) + '|'
        p2 = len(p)
#        if p2 < 34 : print(p)
        return p2
            
print('*' * at(), '|', at())

#p2 = at()       
