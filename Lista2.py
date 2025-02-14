usuarios = [] # lista vazia para armazenar os cadastros 

def adicionar_usuario(): 
    nome = input("Digite seu nome: ")
    documento = input("Digite seu CPF (11 digitos) ou CNPJ: (14 Digitos): ")
    email = input("Digite seu Email: ")
    nascimento  = input("Digite sua data de nascimento: ")

    if len (documento) == 1 or len(documento) == 14: #validação basica
        usuarios.append({"Nome:" : nome, "Documento" : documento, "Email: " : email, "nascimento": nascimento})
    else: 
        print("\nDocumneto invalido! Tente novamente...")

def exibir_usuario(): 
    print("\n Lista de usuarios cadastrados: ")
    for usuarios in usuarios:
        print(usuarios)

        # fluxo do programa 
        for _ in range(3): 
            adicionar_usuario

        exibir_usuario() # exibe a lista no final