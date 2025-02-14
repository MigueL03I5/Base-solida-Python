while True: 
    nome = input ("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    email = input("Digite seu E-mail: ")

    print("\nConfira seus dados: ")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"E-mail: {email}")

    confirmacao = input("\nOs dados estão corretos: ").strip().upper()

    if confirmacao == "S":
        print("Cadastro finalizado...\n")
        break 
    else:
        print("\nVamos refazer seu cadastro...")


