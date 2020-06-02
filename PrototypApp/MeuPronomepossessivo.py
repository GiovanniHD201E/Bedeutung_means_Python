GendoSub = {
    'Caderno' : 'M',
    'Folha' : 'F',
    'Lápis' : 'M',
    'Livro' :  'M',
    'Dicionário':'M',
    'Bolsa':'F',
    'Caneta':'F'    
    }

GendoArt = {
    'O' : 'M',
    'A' : 'F'
    }

ArtdoGen = {
    'M' :  'A ',
    'F' :  'O '
    }
"""
 Introduzimos Apresentamos Apresentaremos agora um novo estilo 
 de trabalho: 
 hiperatividade: mas esta recuperou trabalho 
 iniciado e não terminado anteriormente.
 O Polêmico GiosFormaTrump com o slogan
 |Format America Primeiro |)*(|
# Escrevo VCF1 para identificar Variáveis de Comunicacao, Formatação Primeiro
"""
|VCF1 tem conteúdo variável em função dos contêiners que a limitam|
|Podem existir várias camadas de contêiner: a tela a janela, etc..|
|O contêiner pode ser autoimposto como essa barra vertical aqui =>|
|Mas pode também ser limitado pelo aparelho, aplicativo, acordo...|
|Neste arquivo, são limitaas principalmente pelas aspas, e ...****|
|... o desejo de estabelecer um novo estilo de ajuste de texto, ..|
|O texto que varia com o formato. GioFormaTrump<Format America 1º>|
|Polêmico como o inspirador do nome, mas apesar do duplo sentido,*|
|apelo ao lado humorístico de Donald Trump: não quero destruir a *|
|América. Eu também sou americano. E hoje em dia, o termo formatar|
|um Vinchester não está mais em voga. E formatar um computador não|
|é mais entendido como um processo destrutivo, mas de configuraçao|
|no qual o conteúdo fica preservado. Nos tempos do Vinchester, a *|
|a formatação destruia o conteúdo do computador. God bless America|
|Vale quase tudo para garantir o alinhamento. Exceto duas coisas:*|
|1) Ficar visualmente mais feio do que se estivesse desalinhado; e|
|2) Destruir, digo, alterar o sentido ou objetivo global do texto.|
|VCF1 tornam-se alinhadas em fontes MONOespaçadas             *)*(|
|Conteúdo: buscam despertar a atenção para os detalhes vitais  ***|
"""
MA    =  "*************MENSAGEM PARA ÂNGELA MARAVILHOSA********************"
sB    =  "_________________________________________________________________"
tR    =  "-----------------------------------------------------------------"
VM    =  "-----LEIA TUDO QUE ESTIVER EM VERMELHO MAIÚSCULO-----------------"
VV    =  "VOU VERIFICAR SE VOCÊ PRESTOU ATENÇÃO****************************"
pE    =  "QUE DETALHE LHE CHAMOU ATENÇÃO NO NOME ANGELA, acima?************"
MB    =  ")*(Y)*(---***MUITO BEM, DELICIOSA Ângela!***---------------------"
NMA   =  "Não meu amor, tente de novo"
print(VM)
print(VV)
print(MA)
print(pE)
Res   =  input('Resposta' + ' ')
while Res != "Â":
    Res = input(NMA + ' ')
print(MB)

A = input('Digite o artigo com letra maiúscula' + '  ')
S = input('Digite o substantivo ' + '  ')

GA = CapturaGenArt = GendoArt[A]
GS = CapturaGenSub = GendoSub[S]

if GA == GS:
    print('Continue digitando ou tecle enter \n')
    print(A +' ' + S, end=' ')
    A, S = input(' '), input(' ')
else:
    A = ArtdoGen[GendoArt[A]]


S = input('Digite o substantivo ' + '  ')

GA = CapturaGenArt = GendoArt[A]
GS = CapturaGenSub = GendoSub[S]




