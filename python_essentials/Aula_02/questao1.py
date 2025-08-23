import os

def main():
    cor = input("Digite a cor do semáforo (Vermelho, Amarelo, Verde): ")

    if cor == "verde":
        print("Continue.")
    elif cor == "amarelo":
        print("Atenção!")
    elif cor == "vermelho":
        print("Pare!")
    else:
        print(f"Cor '{cor}' inválida!")
        input("Digite qualquer coisa para tentar novamente: ")
        os.system("cls")
        main()

main()