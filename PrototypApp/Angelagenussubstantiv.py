GenusSub = {
    'Heft' : 'M',
    'Blatt' : 'F',
    'Stift' : 'M',
    'Stuhl' : 'F',
    'Buch' :  'M',
    'Tisch'  :'F',
    'Computer':'M',
    'Wörterbucher':'M',
    'Terminal':'das',
    'Messer':'das',
    'Gabel':'M',
    'Löffel':'F',
    'Caneta':'F',
    'Wecker':'M',
    'Brille':'M',
    'Lineal':'M',
    'Arm':'F',
    'Bett':'das',
    'Wasser':'das',
    'Dictionär':'M',
    'Armario':'M',
    'Tür':'F',
    'Fenster':'das',
    'Sonne':'der',
    'Mond':'der',
    'Schiff':'der',
    'Erdnuss':'die',
    'Vase':'die',
    'Handy':'das',
    'Zug':'der',
       
    
    
    }

GendoArt = {
    'O' : 'M',
    'A' : 'F',
    'meu' : 'M',
    'minha': 'F'
    }

ArtdoGen = {
    'M' :  'A ',
    'F' :  'O ',
    }


A = input('Digite o artigo com letra maiúscula ' + '  ')
S = input('Digite o substantivo ' + '  ')

GA = CapturaGenArt = GendoArt[A]
GS = CapturaGenSub = GendoSub[S]

if GA == GS:
    print('Continue digitando ou tecle enter \n')
    print(A +' ' + S, end=' ')
    A, S = input(' '), input(' ')
else:
    A = ArtdoGen[GendoArt[A]]
    
print(A + S)





