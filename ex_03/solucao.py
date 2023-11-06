import datetime

# Solicita informações ao colaborador
nome = input("Digite o nome do colaborador: ")
data_admissao = input("Digite a data de admissão (Dia/Mes/Ano): ")
salario_atual = float(input("Digite o salário atual: (ex: 5000)"))
valor_emprestimo = float(input("Digite o valor do empréstimo: (ex: 5000)"))

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
    print(f"Valor empréstimo: {valor_emprestimo} reais")
    print("Notas de maior valor:")
    for nota in notas_maior_valor:
        print(f"* {nota};")
    print("Notas de menor valor:")
    for nota in notas_menor_valor:
        print(f"* {nota};")
    print("Notas meio a meio:")
    print(f"{valor_notas_maior} reais em notas de maior valor:")
    for nota in notas_maior_valor:
        print(f"* {nota};")
    print(f"{valor_notas_menor} reais em notas de menor valor:")
    for nota in notas_menor_valor:
        print(f"* {nota};")

