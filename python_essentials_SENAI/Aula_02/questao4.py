aluno = input("Digite o nome do aluno: ")
horasLetivas = int(input(f"Digite a quantidade de horas letivas de {aluno} no mês: "))
horasFaltas = int(input(f"Digite a quantidade de horas que {aluno} faltou: "))

if horasFaltas/horasLetivas > 0.25:
    print(f"{aluno}, você reprovou por falta!")
else:
    print(f"{aluno}, você não reprovou por falta! Congratulations!")