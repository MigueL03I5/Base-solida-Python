# Entre as decisão mostradas, você respondera em forma de uma pesquisa para uma empresa que quer saber se a sociedade da sua cidade gosta mais de doce ou salgado

nome = input("digite seu nome: ")
pesq = int(input("olá, somos uam empresa de pesquisa, poderia responder uma pergunta simples. Entre salgado ou doce, qual você concorda que não pode falta em uma festa: \n 1 - Salgado \n 2 - Doce"))

if pesq <= 1:
    print(f"Sua resposta foi 'salgado'.\n Obrigado pela sua resposta {nome}, ficamos muito feliz por você ter participado. \n @ Salgados realmente são indispensáveis em uma festinha, hem... ")
else: 
    print(f" Sua resposta foi 'DOCE'. \n Obrigado pela sua resposta {nome}, ficamos muito feliz por você ter participado.\n Doces são indispensaveis em uma festinha, hem... ")