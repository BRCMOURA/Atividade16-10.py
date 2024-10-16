# #Informe idade e informar se é maior ou menor de idade

idade = int(input("Digite sua idade:"))

if idade >= 18:
    print('A pessoa é maior de idade')

else:
    print('A pessoa é menor de idade')


# #Usuário informa dois números aleatórios, e o sistema vai comparar se os números são iguais ou diferentes

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

print('O primeiro número é:', num1)
print('O segundo número é:', num2)

if num1 == num2:
    print('Os números são iguais')

else:
    print('Os números são diferentes')

#Verificar se um número é positivo, negativo ou zero

num = int(input("Digite um número:"))

if num > 0:
    print('O número é positivo')

elif num == 0:
    print('O número é zero')

else:
    print('O número é negativo')
