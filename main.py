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
genero = input("Informe o gênero M = Masculino, F = Feminino, O = Outros")
if idade >= 18 and genero == "M":
  print("Você precisa ou precisou prestar serviço militar obrigatório")


  

nome = input("Informe seu nome:")
nota = float(input("Digite sua nota: "))

if (nota==10):
  print(f"{nome}, Parabéns!")
elif (nota >= 6 and nota < 10):
  print(f"{nome},bom trabalho!")
else:
  print("Precisa melhorar")


preco=100
imposto=preco*0.05
print(imposto)

def calcular_imposto(preco_produto):
  imposto = preco_produto*0.05
  return imposto

preco=299
imposto=calcular_imposto(preco)
print(imposto)
  