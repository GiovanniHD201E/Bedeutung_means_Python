def stars(width=10):
    x = '*' * width
    print(x)

def m(text = "queimei a mão no fogão"):
    print('*' * 10)
    print(text)

texto = 'Queimei a mäo nao fogo'
    
"""padronizando a impressão de saída com a função print"""


tip = [
    'Para ver o que este programa faz, você precisa chamar uma das rotinas definidas no programa:',
    'Este programa não está pronto,',
    'por enquanto as duas executam a mesma tarefa',
    'm() ou stars(). ESCREVA:   \n   m() e tecle ENTER']

print(tip[3].split('.')[1])
