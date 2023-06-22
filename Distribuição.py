####################################################################################
### Distribuição de Frequência Com Intervalo de Classe e Sem Intervalo de Classe ###
####################################################################################

# https://colab.research.google.com/

# O link fornecido levará a IDE da Google para dados
# Essa IDE é mais usada para ciências de dados e análise de dados

import matplotlib.pyplot as plt # biblioteca de gráfico
import math # biblioteca de matemática

def distribuicao_sem_intervalos():
    
    # Calcula a distribuição de frequência sem intervalos de classes.
    
    valores = []
    while True:
        valor = input("Digite um valor ou 'fim' para terminar: ")
        if valor.lower() == "fim":
            break
        valores.append(float(valor))

    valores_ordenados = sorted(valores)
    tabela = {}
    total_valores = len(valores)
    for valor in valores_ordenados:
        if valor in tabela:
            tabela[valor] += 1
        else:
            tabela[valor] = 1

    print("Tabela de Frequência:")
    print("---------------------")
    print("Valor\tFrequência\tPorcentagem")
    print("---------------------")
    for valor, frequencia in tabela.items():
        porcentagem = (frequencia / total_valores) * 100
        print(f"{valor}\t{frequencia}\t\t{porcentagem:.2f}%")

    plt.bar(tabela.keys(), tabela.values())
    plt.xlabel("Valor")
    plt.ylabel("Frequência")
    plt.title("Distribuição de Frequência sem Intervalos de Classes")
    plt.show()

def distribuicao_com_intervalos():
  
    # Calcula a distribuição de frequência com intervalos de classes.
    
    valores = []
    while True:
        valor = input("Digite um valor ou 'fim' para terminar: ")
        if valor.lower() == "fim":
            break
        valores.append(float(valor))

    min_valor = min(valores)
    max_valor = max(valores)
    amplitude = max_valor - min_valor

    num_classes = math.ceil(1 + 3.3 * math.log(len(valores))) # Aplicação da fórmula de Sturges
    intervalo_classe = amplitude / num_classes

    tabela = {}
    total_valores = len(valores)
    for i in range(num_classes):
        classe_min = min_valor + (i * intervalo_classe)
        classe_max = classe_min + intervalo_classe
        classe = f"{classe_min:.2f} - {classe_max:.2f}"
        tabela[classe] = 0
        for valor in valores:
            if classe_min <= valor < classe_max:
                tabela[classe] += 1

    print("Tabela de Frequência:")
    print("---------------------")
    print("Classe\tFrequência\tPorcentagem")
    print("---------------------")
    for classe, frequencia in tabela.items():
        porcentagem = (frequencia / total_valores) * 100
        print(f"{classe}\t{frequencia}\t\t{porcentagem:.2f}%") # Exibir resultado

    plt.bar(range(len(tabela)), tabela.values())
    plt.xticks(range(len(tabela)), tabela.keys(), rotation=90)
    plt.xlabel("Classe")
    plt.ylabel("Frequência")
    plt.title("Distribuição de Frequência com Intervalos de Classes") # Motrar o gráfico
    plt.show()

escolha = input("Escolha a opção:\n1 - Sem intervalos de classes\n2 - Com intervalos de classes\n")

if escolha == "1":
    distribuicao_sem_intervalos()
elif escolha == "2":
    distribuicao_com_intervalos()
else:
    print("Opção inválida. Por favor, tente novamente.")
