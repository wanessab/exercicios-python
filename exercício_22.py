"""
#Exercício 22.1
lanchonete = {
    "salgado": 4.50,
    "lanche":6.50,
    "suco":3.00,
    "refrigerante":3.50,
    "doce":1.00,
}
print(lanchonete)

notas_alunos = {
    "Pedro": 8.5,
    "Alice": 9.9,
    "Samanta": 7.0,
    "Rogerio": 4.0,
    "Bianca": 0,
}
print(notas_alunos)
media = sum(notas_alunos.values())/len(notas_alunos)
print(media)
"""
dic_dados={}
dic_dados["nome"]=input("Digite o nome: ")
dic_dados["idade"]=input("Digite idade:")
dic_dados["tel"]= input("Digite tel: ")
dic_dados["end"]=input("Digite end: ")

print(dic_dados)
print(sorted(dic_dados.keys()))
