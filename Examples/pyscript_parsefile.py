#!/usr/bin/env python

"""A simple python script template.
"""

import os
import sys
import argparse
import statistics, math #bibliotecas usadas para o calculo de medias e desvio padrao populacional e amostral
# bibliotecas para fazer histograma
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

def main(arguments):
    
    # ao rodar o script, o usuário deverá fornecer o nome do arquivo de entrada no terminal:
    # a biblioteca argparse é usada para tal
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))
    ##parser.add_argument('-o', '--outfile', help="Output file",
    ##                    default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    print(args)

    # O nome do arquivo de entrada especificado no terminal 
    # é acessado através da função argv da biblioteca sys (sys.argv[1:])
    input_file = sys.argv[1:][0]
    
    # Lê o arquivo de entrada
    ifile = open(input_file, 'r')
    
    # Para linha por linha do arquivo de entrada e 
    # salva cada coluna do arquivo de entrada em listas
    idade = []
    altura = []
    massa = []
    for line in ifile:
    	#print(line)
        #print(line.split(), ' ', len(line.split()))
        columns = line.split()
        idade.append(eval(columns[0]))
        altura.append(eval(columns[1]))
        massa.append(eval(columns[2]))
    
    # calcula a média de cada uma das colunas do arquivo de entrada:
    # idade, altura e massa:
    print ('media idade = ', media(idade), '   mean(idade): ', statistics.mean(idade), '\n')
    print ('desvio padrao idade: ', sstddev(idade), '  stats.stdev(idade): ', statistics.stdev(idade), '  statistics.pstdev(idade): ', statistics.pstdev(idade), '\n')
    print ('media altura = ', media(altura), '   mean(altura): ', statistics.mean(altura), '\n')
    print ('media massa = ', media(massa), '   mean(massa): ', statistics.mean(massa), '\n')

    # histogramas
    fig, axs = plt.subplots(1, 3)
    axs[0].hist(idade, bins=30, range=(16,46), color='red')
    axs[0].set_title('idade')
    axs[0].set_xlabel('idade (anos)')
    axs[0].set_ylabel('frequencia/ano')

    axs[1].hist(altura, bins=8, range=(1.6,2.0), color='green')
    axs[1].set_title('altura')
    axs[1].set_xlabel('altura (m)')
    axs[1].set_ylabel('frequencia/0.05 m')

    axs[2].hist(massa, bins=8, range=(40,120), color='grey')
    axs[2].set_title('massa')
    axs[2].set_xlabel('massa (Kg)')
    axs[2].set_ylabel('frequencia/10 Kg')

    plt.show()

    #plot_hist(idade, 30, (16,46), 'red')
    #plot_hist(altura, 40, (1.6,2.0), 'green')
    #plot_hist(massa, 80, (40, 120), 'grey')

def media(input_list):
    # essa funcao calcula a media dos itens da lista input_list
    ##sum_num = 0
    ##for i in input_list:
        ##sum_num = sum_num + i
    #return sum_num/len(input_list)
    return sum(input_list)/len(input_list)


def sstddev(input_list):
    # cacula o desvio padrão amostral
    # usa a biblioteca statistics do python
    # https://docs.python.org/3/library/statistics.html
    
    N = len(input_list)
    m = statistics.mean(input_list)
    variance = 0
    for i in input_list:
        variance = variance + pow((i - m), 2)
    
    variance = variance/N
    sample_stddev = math.sqrt((N/(N - 1))*variance)

    return sample_stddev

def plot_hist(input_list, n_bins, hist_range, cor):
    # essa função pega como input uma lista 
    # e faz um histograma usando bibliotecas do
    # matplotlib: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html
    # outras opções de módulos que tb fazem histogramas são:
    # plotly, rootpy.

    fig, ax = plt.subplots()
    ax.hist(input_list, bins=n_bins, range=hist_range, color=cor)
    plt.show()

    ##n_bins = [16 + i for i in range(30)]
    ##fig, ax = plt.subplots()
    ##ax.hist(idade, bins=n_bins, color='red')
    ##plt.show()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
