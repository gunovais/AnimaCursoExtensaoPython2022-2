print("Alo mundo!")
nome = "Gustavo Novais"
idade = 22
print(nome)
print("Minha idade é "+str(idade)+" anos")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"Boa noite, {nome}")
print("Sua idade é {}".format(idade))
dobro = idade*2
print("O dobro da sua idade é {}".format(dobro))
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("Você não pode beber e nem dirigir")
