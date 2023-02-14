pessoa1 = int(input("Informe a idade do cidadao 1 para matricular na auto escola X: "))
pessoa2 = int(input("Informe a idade do cidadao 2 para matricular na auto escola X:  "))
if pessoa1 >=18 and pessoa2 >= 18:
    print('Ambos cidadãos estão apto para a matricula')
elif  int(pessoa1) >= 18:
    print('Apenas o cidadão pessoa1 está apto para a matricula!')
elif  int(pessoa2) >= 18:
    print('Apenas cidadão Pessoa2 está apto para a matricula!')
else:
    print('Nenhum cidadao tem idade suficiente para realização de matricula em autoescola!')