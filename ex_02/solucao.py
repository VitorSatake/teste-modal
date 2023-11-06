'''
2) A ModalGR possui um arquivo texto contendo o nome completo, e-mail e data de 
nascimento de seus consultores, separados por pipeline (|). O time de RH deseja que todo 
início de cada mês seja gerado um novo arquivo texto com apenas os dados dos 
aniversariantes do mês corrente, para assim, enviarem uma mensagem personalizada de 
felicitações. Você foi escolhido para criar uma solução que atenda esses quesitos.

'''


import datetime

# Caminho para o arquivo de dados dos consultores
arquivo_consultores = 'ex_02/consultores.txt'

# Caminho para o arquivo de aniversariantes do mês
arquivo_aniversariantes = 'ex_02/aniversariantes.txt'

# Obtém o mês atual
mes_corrente = datetime.datetime.now().month

# Inicializa uma lista para armazenar os aniversariantes do mês, onde ele será criado
aniversariantes = []

# Lê o arquivo de dados dos consultores
with open(arquivo_consultores, 'r') as arquivo:
    linhas = arquivo.readlines()

# Itera pelas linhas para identificar os aniversariantes
for linha in linhas:
    dados = linha.strip().split('|')
    
    # Verifica se a linha contém todos os campos esperados
    if len(dados) == 3:
        data_nascimento = datetime.datetime.strptime(dados[2], '%d/%m/%Y')
        
        if data_nascimento.month == mes_corrente:
            aniversariantes.append('|'.join(dados))

# Cria um arquivo com os aniversariantes do mês
with open(arquivo_aniversariantes, 'w') as arquivo:
    for aniversariante in aniversariantes:
        arquivo.write(aniversariante + '\n')

# Agora você pode enviar mensagens de felicitações para os aniversariantes

print('Aniversariantes do mês foram identificados do arquivo "consultores.txt" e salvos em', arquivo_aniversariantes)
