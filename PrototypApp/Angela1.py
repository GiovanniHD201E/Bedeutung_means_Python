GendoSub = {
    'Caderno' : 'M',
    'Folha' : 'F',
    'Lápis' : 'M',
    'Cadeira' : 'F',
    'Livro' :  'M',
    'Mesa'  :'F',
    'Tesoura':'F',
    'Computador':'M',
    'Dicionário':'M',
    'Parede':'F',
    'Bolsa':'F',
    'Lâmpada':'F',
    'Candelabro':'M',
    'Faca':'F',
    'Garfo':'M',
    'Colher':'F',
    'Caneta':'F',
    'Capa':'M',
    'Carregador':'M',
    'Relógio':'M',
    'Remédio':'M',
    'Óculos':'M',
    'Apontador':'M',
    'Celular':'M',
    'Tablet':'M',
    'Machado':'M',
    'Guilhotina':'F',
    'Forca':'F',
    'Régua':'M',
    'Interruptor':'M'
    'Barco':'M',
    'Arma':'F',
    'Cama':'F',
    'tijolo':'M',
    'Cal':'M',
    'agua':'F',
    'Dicionario':'M',
    'Armario':'M',
    'Boi':'M',
    'Vaca':'F',
    'Uva':'F',
    'Abacaxi':'M',
    'Porta':'F',
    'Janela':'F',
    'Arco iris':'M',
    'Sol':'M',
    'Lua':'F',
    'Boi':'M',
    'lua':'F',
    'Rapadura':'F',
    'Bota':'F',
    'Navio':'M',
    'Sacola':'F',
    'Amendoim':'M',
    'Vaso':'M',
    'Quadro':'M',
    'Piscina':'M',
    'Celular':'M',
    'Trem':'M',
    'Onibus':'M',
    'Aviao':'M',
    'Moto':'M',
    'Televisao':'M',
    'Radio':'M',
    'Relogio':'M',
    'Tabua':'F',
    'Asa':'F',
    'Pé':'M',
    'Sal':'M',
    'Frutas':'F',
    'Aniversario':'M',
    'Guarana':'M',
    'Vento':'M',
    'Pano':'M',
    'Roupa':'F',
    'Sapo':'M',
    'Cobra':'F',
    'Lago':'M',
    'Pato':'M',
    'Pasto':'M',
    'Bosque':'M',
    'Parque':'M'
    
    
    
    

    
    
    
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





