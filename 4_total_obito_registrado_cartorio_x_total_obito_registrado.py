# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

obito_cartorio = open("base_obito_cartorio.csv").readlines()
caso = open("base_caso.csv").readlines()

eixo_x1 = []
eixo_y1 = []

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
totais_meses_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

mes_atual = 4

estado = "GO"

print("Covid-19\n")

for i in range(len(obito_cartorio)) :
	if i != 0 :
		linha = obito_cartorio[i].split(",")

		data = linha[0].split("-")
		dia = int(data[2])
		mes = int(data[1])
		ano = int(data[0])

		if linha[1] == estado :
			for i in range(len(meses)) :
				if mes == i + 1 :
					totais_meses_1[i] += int(linha[9])
					eixo_x1.append(meses[i])
					eixo_y1.append(totais_meses_1[i])

caso = open("base_caso.csv").readlines()

eixo_x2 = []
eixo_y2 = []

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
totais_meses_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

mes_atual = 4

estado = "GO"

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
					totais_meses_2[i] += int(linha[5])
					eixo_x2.append(meses[i])
					eixo_y2.append(totais_meses_2[i])

titulo_grafico = "Totais, óbitos registrados em cartório X Casos de Mortes por mês no Estado"
label_eixo_x = "Eixo X"
label_eixo_y = "Eixo Y"

plt.title(titulo_grafico)
plt.xlabel(label_eixo_x)
plt.ylabel(label_eixo_y)

plt.bar(eixo_x1, eixo_y1, label = "Óbitos registrados")
plt.bar(eixo_x2, eixo_y2, label = "Casos de mortes")

plt.legend()

plt.show()

print("Total de óbitos registrados em cartório por mês no Estado")
for i in range(len(meses)) :
	if i < mes_atual:
		print(meses[i] + ": " + str(totais_meses_1[i]))

print("")

print("Total de Casos de Mortes por mês no Estado")
for i in range(len(meses)) :
	if i < mes_atual:
		print(meses[i] + ": " + str(totais_meses_2[i]))
