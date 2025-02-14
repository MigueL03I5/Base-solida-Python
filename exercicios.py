nome = input(" Qual é seu nome? ")
#idade = input(" Qual é sua idade? ") pq precisa ser inteiro. 
idade = int(input(" Qual é sua idade? "))


#print(f"Olá, {nome}, você tem {idade} anos!") - Não será imprimida na tela pq será true e false (if)

if idade >= 18: 
    print(f"Olá, {nome}- Você é maior de idade. :) ")
else: 
    print(f"Olá, {nome}- Você é menor de idade. :) ")