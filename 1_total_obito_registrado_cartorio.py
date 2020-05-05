# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

#---------------------------------------------------------------------------------------------------------------------------------------------

def gerarListaArquivo(nomeArquivo) :
	return open(nomeArquivo).readlines()

def obterMeses() :
	meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	return meses

def gerarGrafico(tipo_grafico, eixo_x, eixo_y, titulo_grafico, label_eixo_x, label_eixo_y, legenda_grafico, cor_grafico) :
	plt.title(titulo_grafico)
	plt.xlabel(label_eixo_x)
	plt.ylabel(label_eixo_y)

	if tipo_grafico == 'linha' :
		plt.plot(eixo_x, eixo_y, label = legenda_grafico, color = cor_grafico)
	if tipo_grafico == 'barra' :
		plt.bar(eixo_x, eixo_y, label = legenda_grafico, color = cor_grafico)
		plt.legend()
	if tipo_grafico == 'ponto' :
		plt.scatter(eixo_x, eixo_y, label = legenda_grafico, color = cor_grafico)

	plt.show()

	return

def imprimirMeses(meses, totais_meses) :
	for i in range(len(meses)) :
		if i < mes_atual:
			print(meses[i] + ": " + str(totais_meses[i]))

#---------------------------------------------------------------------------------------------------------------------------------------------

mes_atual = 4

estado = "GO"

obito_cartorio = gerarListaArquivo("base_obito_cartorio.csv")
meses = obterMeses()
totais_meses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

eixo_x = []
eixo_y = []

tipo_grafico = {"l":"linha", "b":"barra", "p":"ponto"}

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
					totais_meses[i] += int(linha[9])
					eixo_x.append(meses[i])
					eixo_y.append(totais_meses[i])

gerarGrafico(tipo_grafico["l"], eixo_x, eixo_y, "Total de óbitos registrados em cartório por mês no Estado", "Eixo X", "Eixo Y", "Gráfico", "blue")

imprimirMeses(meses, totais_meses)
