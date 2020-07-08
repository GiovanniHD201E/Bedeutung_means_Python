# Dadas as Identidades dos membros da família Lemos de Medeiros, 
# o programa deve encontrar uma maneira de alinhá-los com objetivo 
# de formar uma moldura para um quadro. As diretrizes são as seguintes:
# Usar como entrada Id_LM0{1, 2, 3, 4}; A saída deve ser em duas linhas
# As duas linhas devem conter o mesmo número de caracteres
# Só é admitido um único espaço em branco entre cada nome ou 
# representação do nome
# Use tudo que aprendeste hoje para solucionar o problema, mas só se
# preocupe com este item depois de ter esboço da solução "ensetada".

import random	#In order to choose a sentence at random | Das Ziel...
import itertools	#Estou aprendendo a usar este

# Preciso medir o tamanho das palavras e a posição dos espaços entre elas

frases = (
"Ich liebe dich, meine Tochter!",
"Eu te amo, minha filha!",
"Ich liebe dich, Vatti!",
"Eu te amo, papai!",
"Vamos bricar de barco Viking?",
"Vou fazer ginástica!",
"Conta pro papai!",
"Eins, zwei, drei, vier, fünf...",
"Eins, zwei, drei, vier, ...,"
"... zehn, elf, zwölf, ..., força papai!",
"Você consegue!"
)

print("_|_", "Escreva: 'Daten', sem aspas, e pressione enter para ver os dados\n"
      "pré-concebidos ou escreva 'Funktionen' para ver as funções definidas\n"
      "neste módulo")
print("Clique na linha abaixo e tecle enter \n fam_lm()")

def size_of(qc=frases):
    tam = len(qc)
    for n in range(tam):
        if (len(qc[-1]) == 1) & (len(qc[0]) == 1):
            resp = "Você inseriu uma palavra com", tam, "caracteres?"
            return resp
    return tam
	

def fam_lm():   # AleaTexto() era o nome original
    Id_LM01 = [
    "Giovanni",           
    "Gio",
#    "Giova",
 #   "Giovanni Medeiros",
  #  "Giovanni G. de Medeiros Lemos",
   # "Giovanni Gomes de Medeiros Lemos",
    #"Giovanni Lemos",
    #"Giovanni G M Lemos",
    #"Giovanni G. de Medeiros L."
    ]

    Id_LM02 = [
    "Angela",
#    "Ângela",
 #   "Angela Medeiros",
  #  "Ângela de Sá Lemos de Medeiros",
   # "Angela S. Lemos de Medeiros",
    #"Angela S. L. de Medeiros",
    #"Angela S L Medeiros",
    #"Angela Lemos",
    #"Angela de Sa Lemos de Medeiros"
    ]

    Id_LM03 = [
#    "Victor Giovanni Lemos de Medeiros",
#    "Victor",
    "VG",
 #   "Victor Lemos",
  #  "Victor Medeiros",
   # "Victor de Medeiros",
    #"Victor Giovanni",
    #"Victor Giovanni L. de Medeiros"
    ]

    Id_LM04 = [
#    "Julia Nildesleben Lemos de Medeiros",
 #   "Julia Nildesleben",
    "Julia"
    ]
    
    pontu = [
        '.',
        '!',
        '?',
        ':',
        ]

    gio = []
    tamgio = []
    for Gio in range(len(Id_LM01)):
        #p2 = random.choice(Id_LM01)
        #p3 = len(p2)
        gio.append(Id_LM01[Gio])
        tamgio.append(len(Id_LM01[Gio]))
        
    ang = []
    tamang = []
    for Angela in range(len(Id_LM02)):
        print(Id_LM02[Angela], len(Id_LM02[Angela]))
        ang.append(Id_LM02[Angela])
        tamang.append(len(Id_LM02[Angela]))

    vic = []
    tamvic = []
    for Vic in range(len(Id_LM03)):
        print(Id_LM03[Vic], len(Id_LM03[Vic]))
        vic.append(Id_LM03[Vic])
        tamvic.append(len(Id_LM03[Vic]))

    jul = []
    tamjul = []
    for Julia in range(len(Id_LM04)):
        print(Id_LM04[Julia], len(Id_LM04[Julia]))
        jul.append(Id_LM04[Julia])
        tamjul.append(len(Id_LM04[Julia]))
    
    return gio, tamgio, ang, tamang, vic, tamvic, jul, tamjul

    #return p2, p3
            

Daten = ('frases', '"tudo que está escrito neste módulo com aspas simples"'
         '"comtêm um valor armazenado"', '"basta digitá-lo, sem aspas, e este"'
         '"ser-lhe-á revelado"')

Funktionen = "size_of(frases)", "fam_lm()"
