import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def dadosDataset():
    numeroCasos = []
    numeroMortes = []
    numeroRecuperados = []

    with open('dataset.csv', 'r', encoding = "ISO-8859-1") as arquivo:
            leitor = csv.reader(arquivo, delimiter=',')

            for linha in leitor: 
                if(linha[2].lower() == 'confirmed'):
                    continue
                else:                    
                    numeroCasos.append(int(linha[2]))
                    numeroMortes.append(int(linha[3]))
                    numeroRecuperados.append(int(linha[4]))                            
    
    print("\nAgora será feita uma análise sobre os dados de COVID-19 na Túrquia no período de 10/03/2020 até 27/10/2020")
    #Correlação 1
    correlacaoCasosMortes = np.corrcoef(numeroCasos, numeroMortes)
    correlacaoCasosMortes = correlacaoCasosMortes[0][1]
    print('\nÍndice de correlacao entre casos confirmados e mortes: ', correlacaoCasosMortes, '\n')
    
    #Correlação 2

    correlacaoCasosRecuperados = np.corrcoef(numeroCasos, numeroRecuperados)
    correlacaoCasosRecuperados = correlacaoCasosRecuperados[0][1]
    print('Índice de correlacao entre casos confirmados e recuperados: ',correlacaoCasosRecuperados, '\n')

    print('Observando os valores dos indices de correlações é possível perceber que o há uma correlação maior entre o número de casos confirmados e o número de mortes, pois o índice está mais próximo de 1 do que o índice apresentado para a correlação entre casos confirmados e recuperados.')
    print('\n')
    print('É possível perceber também que há uma correlação linear positiva forte em ambos os casos.')

    #Gráfico 1
    plt.scatter(numeroCasos, numeroMortes)
    plt.xlabel('Quantidade de Casos')
    plt.ylabel('Quantidade do Mortes')
    plt.title('Gráfico de correlação entre casos confirmados e mortes')
    plt.show()
    
    #Gráfico 2
    plt.scatter(numeroCasos, numeroRecuperados)
    plt.xlabel('Quantidade de Casos')
    plt.ylabel('Quantidade de Recuperados')
    plt.title('Gráfico de correlação entre casos confirmados e recuperados')
    plt.show()
    
    
    #Estudo da Regressão linear numero casos confirmados e mortes
    print("\nEstudo da Regressão linear numero casos confirmados e mortes: ")
    m, b, r_value, p_value, std_err = stats.linregress(numeroCasos, numeroMortes)
    print("Valor de m: ", m, "\nValor de b: ", b)    

    linha_reg = [m*i + b for i in range(max(numeroCasos))]
     
    plt.scatter(numeroCasos, numeroMortes)
    plt.plot(linha_reg, 'r')    
    plt.xlabel('Quantidade de Casos')
    plt.ylabel('Quantidade do Mortes')
    plt.title('Gráfico de correlação entre casos confirmados e mortes')
    plt.show()


    #Estudo da Regressão linear numero casos confirmados e recuperados
    print("Estudo da Regressão linear numero casos confirmados e recuperados: ")
    m, b, r_value, p_value, std_err = stats.linregress(numeroCasos, numeroRecuperados)
    print("Valor de m: ", m, "\nValor de b: ", b)    

    linha_reg = [m*i + b for i in range(max(numeroCasos))]
         
    plt.scatter(numeroCasos, numeroRecuperados)
    plt.plot(linha_reg, 'r')
    plt.xlabel('Quantidade de Casos')
    plt.ylabel('Quantidade de Recuperados')
    plt.title('Gráfico de correlação entre casos confirmados e recuperados')
    plt.show()

    #Previsões
    m, b, r_value, p_value, std_err = stats.linregress(numeroCasos, numeroMortes)
    
    print("\n5 Previsões de casos/mortes baseado na equação de Regressão Linear")
    previsao1 = int(m*(200000) + b)
    print("Previsão feita para a possibilidade de 200.000 casos: ", previsao1, "mortes")
    previsao2 = int(m*(10000) + b)
    print("Previsão feita para a possibilidade de 10000 casos: ", previsao2, "mortes")
    previsao3 = int(m*(15000) + b)
    print("Previsão feita para a possibilidade de 15000 casos: ", previsao3, "mortes")
    previsao4 = int(m*(2500) + b)
    print("Previsão feita para a possibilidade de 2500 casos: ", previsao4, "mortes")
    previsao5 = int(m*(20000) + b)
    print("Previsão feita para a possibilidade de 20.000 casos: ", previsao4, "mortes\n")


dadosDataset()