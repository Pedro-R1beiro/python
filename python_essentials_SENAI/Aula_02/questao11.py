#questao 13

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Ainda não pode votar.")
elif (idade >= 16 and idade <= 17) or idade > 70:
    print("Voto opcional.")
else:
    print("Voto obrigatório.")