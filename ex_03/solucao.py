'''
3) A ModalGR criará um programa de empréstimo para os colaboradores que possuem tempo 
de casa superior a 5 anos. O colaborador poderá simular um empréstimo de até 2 vezes o valor 
de seu respectivo salário, desde que esse valor seja múltiplo de 2. Esse programa dará a 
possibilidade de retirada em dinheiro vivo, de acordo com as seguintes opções:
➢ Notas de maior valor: considerando primeiramente as notas de 100 e 50 reais, e em 
seguida, as inferiores;
➢ Notas de menor valor: considerando as notas de 20, 10, 5 e 2 reais.
➢ Notas meio a meio: metade do valor em notas maiores e a outra metade em notas 
menores.
Essas opções deverão ser exibidas ao colaborador, para assim, realizar a escolha de acordo com 
sua necessidade.
Visando atender esse quesito, você foi escolhido para nos ajudar nessa solução! 
A ideia é ter os seguintes campos para inserção: do nome do colaborador, data de admissão, 
salário atual, valor de empréstimo, e em seguida, exibir as opções de retirada, por exemplo:
Valor empréstimo: 8.550 reais
Notas de maior valor: 
➢ 85 x 100 reais;
➢ 1 x 50 reais.
Notas de menor valor: 
➢ 427 x 20 reais;
➢ 1 x 10 reais.
Notas meio a meio:
4.275 reais em notas de maior valor:
➢ 42 x 100 reais;
➢ 1 x 50 reais;
➢ 1 x 20 reais;
➢ 1 x 5 reais.
4.275 reais em notas de menor valor:
➢ 213 x 20 reais;
➢ 1 x 10 reais;
➢ 1 x 5 reais.
Observações: 
➢ Caso o colaborador não se enquadre nos requisitos mínimos de adesão ao programa 
de empréstimo, exiba a mensagem: Agradecemos seu interesse, mas você não atende 
os requisitos mínimos do programa.
➢ Caso o colaborador insira um valor de empréstimo que não seja múltiplo de 2, exiba a 
mensagem: Insira um valor válido!

'''



import datetime

# Solicita informações ao colaborador
nome = input("\nDigite o nome do colaborador: \n")
data_admissao = input("Digite a data de admissão (Dia/Mes/Ano): \n")
salario_atual = float(input("Digite o salário atual (ex: 5000):  \n"))
valor_emprestimo = float(input("Digite o valor do empréstimo (ex: 5000): \n"))

# Calcula o tempo de casa em anos
hoje = datetime.date.today()
data_admissao = datetime.datetime.strptime(data_admissao, "%d/%m/%Y").date()
tempo_de_casa = hoje.year - data_admissao.year

# Verifica se o colaborador atende aos requisitos mínimos
if tempo_de_casa <= 5:
    print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
elif valor_emprestimo % 2 != 0:
    print("Insira um valor válido (múltiplo de 2).")
elif valor_emprestimo > (salario_atual * 2):
    print("O valor do empréstimo não pode ser superior a 2 vezes o salário atual.")
else:
    # Calcula as opções de retirada
    notas_maior_valor = []
    notas_menor_valor = []
    notas_meio_a_meio = []

    valor_notas_maior = min(valor_emprestimo, (salario_atual * 2) // 2)
    valor_notas_menor = valor_emprestimo - valor_notas_maior

    notas_maior_valor.extend([f"{valor_notas_maior // 100} x 100 reais", f"{valor_notas_maior % 100} x 50 reais"])
    notas_menor_valor.extend([f"{valor_notas_menor // 20} x 20 reais", f"{valor_notas_menor % 20 // 10} x 10 reais", f"{valor_notas_menor % 10 // 5} x 5 reais"])
    
    notas_meio_a_meio.extend(notas_maior_valor)
    notas_meio_a_meio.extend(notas_menor_valor)

    # Exibe as opções de retirada
    print(f"\nValor empréstimo: {valor_emprestimo} reais")
    print("\nNotas de maior valor:")
    for nota in notas_maior_valor:
        print(f"* {nota};")
    print("\nNotas de menor valor:")
    for nota in notas_menor_valor:
        print(f"* {nota};")
    print("\nNotas meio a meio:")
    print(f"\n{valor_notas_maior} reais em notas de maior valor:")
    for nota in notas_maior_valor:
        print(f"* {nota};")
    print(f"\n{valor_notas_menor} reais em notas de menor valor:")
    for nota in notas_menor_valor:
        print(f"* {nota};\n")

