#26
users = {
    "wanessab": 566998,
    "pedrom": 662233,
    "ricardon": 585223,
    "silvanab": 474545,
}
login = users.keys()
password = users.values()
usuario = ""
senha = ""
while usuario != login and senha != password:
    usuario = input("login: ")
    senha = int(input("Senha: "))
    if (usuario in users.keys()) and (senha in users.values()):
        print("Senha e usuário corretos!")
    else:
        print("Senha e usuário inválidos!")

