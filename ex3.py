nome = input('Qual seu nome: ')
horas = int(input('Quantas horas você trabalhou? '))
quant = int(input('Quanto você recebe por hora? '))
tot = horas * quant
print ('{}, receberá: {:.2f} reais' .format(nome, tot))