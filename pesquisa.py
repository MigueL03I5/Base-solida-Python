import json

# Carregar os dados do JSON
with open("superheroes.json", "r", encoding="utf-8") as file:
    nome = json.load(file)
    superheroes = nome["herois"]

# Função para listar todos os usuários
def listar_superheroes():
    for superhero in superheroes:
        print(f"superhero: {superhero['superhero']}, publisher: {superhero['publisher']}, alter_ego: {superhero['alter_ego']}, first_appearance: {superhero['first_appearance']}, characters: {superhero['characters']}")

# Função para buscar um heroi pelo publisher
def buscar_superhero(publisher):
    for superhero in superheroes:
        if superhero["publisher"] == publisher:
            return superhero
    return None

# Função para adicionar um novo herói
def adicionar_superhero():
    superhero = input("Digite o nome do herói: ")
    publisher = input("Digite o nome da editora: ")
    alter_ego = input("Digite o nome do alter ego: ")
    first_appearance = input("Digite onde foi sua primeira aparição: ")
    characters = input("digite algumas edições desse herói: ")
    superheroes.append({"nome": superhero, "publisher": publisher, "alter_ego": alter_ego, "first_appearance": first_appearance, "characters": characters})
    print("Usuário adicionado com sucesso!")

# Função para salvar as alterações no JSON
def salvar_alteracoes():
    with open("superheroes.json", "w", encoding="utf-8") as file:
        json.dump({"usuarios": superheroes}, file, indent=2, ensure_ascii=False)
    print("Dados salvos com sucesso!")

# Exemplo de interação com as funções
if __name__ == "__main__":
    while True:
        print("\n1. Listar os Super heróis")
        print("2. Buscar Super heróis pela editora")
        print("3. Adicionar Super heróis")
        print("4. Salvar alterações")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_superheroes()
        elif opcao == "2":
            publisher = input("Digite a editora: ")
            superhero = buscar_superhero(publisher)
            if superhero:
                print(f"Herói encontrado: {superhero}")
            else:
                print("Heroi não encontrado.")
        elif opcao == "3":
           adicionar_superhero()
        elif opcao == "4":
            salvar_alteracoes()
        elif opcao == "5":
            break
        else:
            print("Opção inválida, tente novamente.")