import random	#In order to choose a sentence at random | Das Ziel...
import itertools	#Estou aprendendo a usar este

def size_of(qc):
    tam = len(qc)
    for n in range(tam):
        if (len(qc[-1]) == 1) & (len(qc[0]) == 1):
            resp = "Você inseriu uma palavra com", tam, "caracteres?"
            return resp
    return tam
	

def lemos():
    Id_LM01 = [
    "Giovanni",           
    "Gio"
    ]

    Id_LM02 = [
    "Angela"
    ]

    Id_LM03 = [
    "Victor",
    "VG"
    ]

    Id_LM04 = [
    "Julia Nildesleben",
    "Julia"
    ]
    
    komplement = [
        '.',
        '!',
        '?',
        ':',
        '*',
        '|',
        '_',
        '()',
        ',',
        '13',
        '6',
        'anos',
        ',,',
        '""',
        ' '
        ]

    gio = []
    tamgio = []
    for Gio in range(len(Id_LM01)):
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

            
