# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

caso = open("base_caso.csv").readlines()

eixo_x = []
eixo_y = []
eixo_y2 = []
eixo_y3 = []

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
totais_meses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
totais_meses_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
totais_meses_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

mes_atual = 4

estado = "GO"

print("Covid-19\n")

for i in range(len(caso)) :
	if i != 0 :
		linha = caso[i].split(",")

		data = linha[0].split("-")
		dia = int(data[2])
		mes = int(data[1])
		ano = int(data[0])

		if linha[1] == estado :
			for i in range(len(meses)) :
				if mes == i + 1 :
					totais_meses[i] += int(linha[4])
					totais_meses_2[i] += int(linha[5])

					eixo_x.append(meses[i])
					eixo_y.append(totais_meses[i])
					eixo_y2.append(totais_meses_2[i])

titulo_grafico = "Total de Casos Confirmados e de Casos de Mortes por mês no Estado"
label_eixo_x = "Eixo X"
label_eixo_y = "Eixo Y"

plt.title(titulo_grafico)
plt.xlabel(label_eixo_x)
plt.ylabel(label_eixo_y)

plt.bar(eixo_x, eixo_y, label = "Casos Confirmados")
plt.bar(eixo_x, eixo_y2, label = "Casos de Mortes")

plt.legend()

plt.show()

for i in range(len(meses)) :
	if i < mes_atual:
		print(meses[i] + ": " + str(totais_meses[i]))
