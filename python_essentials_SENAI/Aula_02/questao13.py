import os
os.system('cls')

valorIncial = float(input("Digite um valor inicial para depósito: "))
valorAtual = valorIncial

def saque(valor):
    global valorAtual
    if valor > 500:
        return "Erro: O valor do saque não pode ser maior que 500R$."
    elif valor < 0:
        return "Erro: O valor do saque não pode ser negativo."
    elif valor > valorAtual:
        return "Erro: O valor do saque é maior do que o saldo disponível."
    else:
        valorAtual -= valor
        return "Sucesso: Valor foi resgatado."
    
while True:
    print(f"Saldo dispoível: {valorAtual:.2f}")
    saqueValor = float(input("Digite o valor que deseja sacar (Para encerrar, digite 0): "))
    if saqueValor == 0:
        os.system('cls')
        break
    os.system('cls')
    print(saque(saqueValor))