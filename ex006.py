#Digite um nome, calcule e retorne quantas letras tem esse nome.

string1 = str(input("Digite um nome: ")).strip()

contagem = len(string1.replace(" ", ""))

print(f"O nome tem {contagem} letras. ")