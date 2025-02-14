# para saber se consegue pegar o diploma, porém o curso tem que ter mais de 75% de frequencia
nome = input("Digite seu nome: ")
freq = int(input("  Em 8 dias de aulas, quantos dias você foi a aula: "))

if freq >= 6: 
    print(f"Parabéns {nome}, você pegara o diplona de curso")
else: 
        print(f"Olá, {nome}. Você não atingiu a frequencia do curso, sinto muito, mas você não pegara o seu diplona. ")