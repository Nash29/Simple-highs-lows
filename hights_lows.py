# pagina 455 info sobre datas important

# importa csv
import csv
from datetime import datetime

from matplotlib import pyplot as plt


# armazena em filename
filename = 'sitka_weather_07-2014.csv'

# Abre o arquivo
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader) # next -> devolve a próxima linha do arquivo
	
	'''
	# Exibindo cabeçalho e suas posições
	for index, column_header in enumerate(header_row):
		print(index, column_header)
	'''
	
	# Obtém as datas e as temperaturas maximas do arquivo
	dates, highs = [], []
	for row in reader:
		# converte as datas para um datetime
		current_date = datetime.strptime(row[0], '%Y-%m-%d')
		dates.append(current_date)
		
		
		# converte para inteiro
		high = int(row[1])
		highs.append(high)
		
	print(highs)
	
	
# Faz a plotagem dos dados
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')


# Formata o grafico
plt.title('Daily high temperatures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
fig.autofmt_xdate()# desenha as datas em diagonal
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()










