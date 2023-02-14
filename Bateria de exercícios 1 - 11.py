"""
#### Exercício 1
# Faça um programa que peça dois números e imprima o maior deles

x = int(input("Digite um número: "))
y = int(input("Digite um número: "))
print("Números digitados: ",x,"e",y)
print("O maior número é:",max(x,y))


#### Exercício 2
# Faça um programa que peça o valor e mostre na tela se o valor é positivo ou negativo

x = float(input("Digite um número: "))
if x > 0:
    print("{} é positivo".format(x))
else:
    print("{} é negativo".format(x))


#### Exercício 3
# Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra, escrever: F - Feminino,
# M - Masculino, Sexo Inválido

print("Qual o seu sexo?")
print("")
print("Digite 'F' para sexo Feminino" )
print("")
print("Digite 'M' para sexo masculino")
print("")

sexo = input("Sexo: ")

if sexo in ("F,f"): #sexo == "F" or sexo == "f"
    print("O seu sexo é feminino!")
elif sexo in ("M,m"):
    print("O seu sexo é masculino!")
else:
    print("Sexo inválido!")


#### Exercício 4
# Faça um programa que verifique se uma letra digitada é vogal ou consoante
lista_alfabeto = ["a","e","i","o","u"]
letra = input("Digite um caractere:" )
if letra in lista_alfabeto:
    print("O caractere digitado é vogal!")
else:
    print("O caractere digitado é consoante!")

#### Exercício 6
# Faça um programa que leia três números e mostre o maior deles
n1 = int(input(("Digite um número: ")))
n2 = int(input(("Digite um número: ")))
n3 = int(input(("Digite um número: ")))
lista_numeros = (n1,n2,n3)
print("O maior número digitado é {}".format(max(lista_numeros)))


#### Exercício 7
# Faça um programa que leia três números e mostre o maior e o menor deles

n1 = int(input(("Digite um número: ")))
n2 = int(input(("Digite um número: ")))
n3 = int(input(("Digite um número: ")))
lista_numeros = (n1,n2,n3)
print("O maior número digitado é {}".format(max(lista_numeros)))
print("O menor número digitado é {}".format(min(lista_numeros)))

#### Exercício 8
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato
refrigerante = float(6.25)
suco = float(5.50)
agua = float(2.35)

print("")
print("As opções de bebidas disponíveis são: ")
print("")
print("Refrigerante, por apenas R$ {:.2f}".format(refrigerante))
print("")
print("Suco, por apenas R$ {:.2f}".format(suco))
print("")
print("Água, por apenas R$ {:.2f}".format(agua))
print("")
print("Digite 1 para 'REFRIGERANTE")
print("Digite 2 para 'SUCO")
print("Digite 1 para 'ÁGUA")

compra = ""
while compra != ("3"):
    print("")
    compra = input("Escolha um produto: ")
    if compra == ("3"):
        print("Compra realizada com sucesso!")
    else:
        print("Saldo insuficiente! Escolha outro produto.")

#### Exercício 9
# Faça um programa que leia três números e mostre-os em ordem decrescente

n1 = int(input(("Digite um número: ")))
n2 = int(input(("Digite um número: ")))
n3 = int(input(("Digite um número: ")))
lista_numeros = [n1,n2,n3]
lista_numeros.sort(reverse = True)
print(lista_numeros)


#### Exercício 10
#Faça um programa que pergunte em que turno você estuda. Peça para digitar M - Matutino ou V - Vespertino ou N - Noturno. Imprima a mensagem " Bom dia"
#"Boa tarde" , "Boa noite" ou "Valor Inválido", conforme o caso.

print("Em qual turno você estuda?")
print("")
print("Digite 'M' para Matutino" )
print("")
print("Digite 'V' para Vespertino")
print("")
print("Digite 'N' para Noturno")
print("")
nome = input("Digite o seu nome: ")
turno = input("Turno: ")
if turno in ("M,m"): #sexo == "F" or sexo == "f"
    print("Bom dia, {}!".format(nome))
elif turno in ("V,v"):
    print("Boa tarde, {}!".format(nome))
elif turno in ("N,n"):
    print("Boa noite, {}!".format(nome))
else:
    print("Valor inválido!")



"""
import timeit

# Exercício 5
# Faça um programa que leia a data e a hora do último dia de aula e calcule quanto tempo para falta para o curso acabar

#### Exercício 11
#As organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará
#os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# Salários até R$ 280,00 (incluindo): aumento de 20%
# Salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# Salários de R$ 1500,00 em diante: Aumento de 5 %.
# Após ser realizado, informe na tela:
# O salário antes do reajuste;
# O percentual de aumento aplicado;
# O valor do aumento;
# O novo salário, após o aumento.







