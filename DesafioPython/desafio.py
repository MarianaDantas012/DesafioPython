import pandas as pd
import random

# DESAFIO 1

dd = pd.read_csv("PlanilhaDietaDeFrutas.csv", sep=";")
print("Segue dados da planilha \n", dd)

frutas = dd['Frutas']

random.seed(23)
print("A fruta aleatória é ", random.choice(frutas))


# DESAFIO 2


class DataHorario:
    def __init__(self, diac, mesc, anoc, horac, minutoc):
        self.diac = diac
        self.mesc = mesc
        self.anoc = anoc
        self.horac = horac
        self.minutoc = minutoc


dia = input("digite o dia (dd) ")
mes = input("digite o mes (mm) ")
ano = input("digite o ano (aaaa) ")
hora = input("digite a hora (hh) ")
minuto = input("digite os minutos (mm) ")

data_hora = DataHorario(dia, mes, ano, hora, minuto)


data = (data_hora.anoc + "-" + data_hora.mesc + "-" + data_hora.diac + " " + data_hora.horac + ":" + data_hora.minutoc + ":" + "00")
data = dd[dd['Data_horario'] == data]

dia = int(dia)
if dia>31:
        print("Dia Invalido")

else:
        print("Voce deve comer \n", data['Frutas'])

