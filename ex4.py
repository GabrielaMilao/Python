n1 = float(input('Diga o primeiro número: '))
op = input('Diga qual a operação: ')
n2 = float(input('Diga o segundo número: ')) 

if op == "+":
	print('A soma é: {}'.format(n1 + n2))
elif op == "-":
	print('A subtração é: {}'.format(n1 - n2))
elif op == "*":
	print('A multiplição é: {}'.format(n1 * n2))
elif op == "/":
	print('A divisão é: {}'.format(n1 / n2))
else:
	print('A operação não existe')

