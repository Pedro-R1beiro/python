profits = []
expenses = []

# CRUD Expenses (Gastos)

def valuesDashBoard():
    return "res"

def create(data, name, desc, value):
    try:
        array_referenced = eval(data)
        array_referenced.append({
            "name": name,
            "desc": desc,
            "value": value
        })
        return True
    except Exception:
        return False

def read(data):
    try:
        array_referenced = eval(data)
        indice = "Indice"
        name = "Name"
        desc = "Descrição"
        value = "Valor"
        
        table = f"|{indice.center(10)}|{name.center(15)}|{desc.center(30)}|{value.center(8)}|\n"
        lenRow = len(table)
        
        for i, value in enumerate(array_referenced):
            for i in range(1, lenRow):
                table += "-"
            table += f"\n|{str(i).center(10)}|{value['name'].center(15)}|{value['desc'].center(30)}|{value['value'].center(8)}|"
        
        return table
    except Exception:
        return False
    
def update(data, name, desc, value, idRow):
    return "update"

def delete(data):
    return "delete"

def showOptions():
    print("-------------------------------")
    print("|----Despesa---|----Receita---|")
    print("|--------------|--------------|")
    print("|---1-Criar----|---5-Criar----|")
    print("|---2-Ler------|---6-Ler------|")
    print("|---3-Editar---|---7-Editar---|")
    print("|---4-Excluir--|---8-Excluir--|")
    print("-------------------------------")

def controller(option):
    match option:
        case 1: 
            name = input("Digite o nome da Despesa: ")
            desc = input("Digite uma descrição para a Despesa: ")
            value = input("Digite o valor da Despesa: ")

            if create("expenses", name, desc, value):
                return "Nova despesa criada com sucesso!"
            else:
                return "Erro ao registrar nova despesa."
        case 2:
            return read("expenses")
        case 3:
            print(read("expenses"))
            idRow = int(input("Digite o id da despesa que deseja editar: "))
            name = input("Digite o novo nome: ")
            desc = input("Digite a nova descrição: ")
            value = input("Digite o novo valor: ")

            if update("expenses", name, desc, value, idRow):
                return "Despesa editada com sucesso!"
            else:
                return "Erro ao editar despesa."
        case 4:
            print(read("expenses"))
            idRow = int(input("Digite o id da despesa que deseja excluir: "))
            confirmation = input("Deseja mesmo excluir esta despesa? Essa ação não pode ser desfeita. (s/n) ")
            if confirmation != 's' and confirmation != 'n': return "Resposta não aceita. Ação interrompida."
            if confirmation == 'n': return "Ação interrompida."
            if delete("expenses", idRow):
                return "Despesa excluída com sucesso!"
            else:
                return "Erro ao exluir despesa."
        case 5:
            name = input("Digite o nome da Receita: ")
            desc = input("Digite uma descrição para a Receita: ")
            value = input("Digite o valor da Receita: ")

            if create("profits", name, desc, value):
                return "Nova receita criada com sucesso!"
            else:
                return "Erro ao registrar nova receita."
        case 6:
            return read("profits")
        case 7:
            print(read("profits"))
            idRow = int(input("Digite o id da receita que deseja editar: "))
            name = input("Digite o novo nome: ")
            desc = input("Digite a nova descrição: ")
            value = input("Digite o novo valor: ")

            if update("profits", name, desc, value, idRow):
                return "Receita editada com sucesso!"
            else:
                return "Erro ao editar receita."
        case 8:
            print(read("profits"))
            idRow = int(input("Digite o id da receita que deseja excluir: "))
            confirmation = input("Deseja mesmo excluir esta receita? Essa ação não pode ser desfeita. (s/n) ")
            if confirmation != 's' and confirmation != 'n': return "Resposta não aceita. Ação interrompida."
            if confirmation == 'n': return "Ação interrompida."
            if delete("profits", idRow):
                return "Receita excluída com sucesso!"
            else:
                return "Erro ao exluir receita."

def main():
    lucros, gastos, saldo = valuesDashBoard()
    print(f"Lucros: {lucros}, Gastos: {gastos}, Saldo: {saldo}")
    showOptions()
    option = int(input("Digite o número da opção desejada: "))
    if option <= 0 or option > 8: 
        print("Opção inválida")
        main()
    print("Processando...")
    print(controller(option))
    repeat = input("Digite 'exit' caso deseje sair, caso não, presseione enter: ")
    if repeat != 'exit': main()
    exit()

main()