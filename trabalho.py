receitas = []
despesas = []


def ler_valor():
    while True:
        try:
            valor = float(input("Valor (R$): ").replace(",", "."))
            if valor > 0:
                return valor
            print("O valor deve ser maior que zero.")
        except ValueError:
            print("Digite um número válido.")


def adicionar_receita():
    descricao = input("Descrição da receita: ").strip()
    valor = ler_valor()
    receitas.append({"descricao": descricao, "valor": valor})
    print(f"Receita de R$ {valor:.2f} adicionada!\n")


def adicionar_despesa():
    descricao = input("Descrição da despesa: ").strip()
    valor = ler_valor()
    despesas.append({"descricao": descricao, "valor": valor})
    print(f"Despesa de R$ {valor:.2f} adicionada!\n")


def ver_saldo():
    total_receitas = sum(r["valor"] for r in receitas)
    total_despesas = sum(d["valor"] for d in despesas)
    saldo = total_receitas - total_despesas

    print("\n--- SALDO ---")
    print(f"Receitas: R$ {total_receitas:.2f}")
    print(f"Despesas: R$ {total_despesas:.2f}")
    print(f"Saldo:    R$ {saldo:.2f}\n")


def menu():
    while True:
        print("=== CONTROLE FINANCEIRO ===")
        print("1) Adicionar receita")
        print("2) Adicionar despesa")
        print("3) Ver saldo")
        print("4) Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_receita()
        elif opcao == "2":
            adicionar_despesa()
        elif opcao == "3":
            ver_saldo()
        elif opcao == "4":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Escolha de 1 a 4.\n")


if __name__ == "__main__":
    menu()