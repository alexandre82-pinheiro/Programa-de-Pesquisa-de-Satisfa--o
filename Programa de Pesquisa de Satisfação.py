# Programa de Pesquisa de Satisfação

print("     PESQUISA DE SATISFAÇÃO DE ATENDIMENTO ")


# Laço principal para permitir repetir a pesquisa inteira
while True:
    # Solicita a quantidade de entrevistados para esta nova pesquisa
    while True:
        try:
            total_entrevistados = int(input("\nQuantas pessoas serão entrevistadas nesta pesquisa? "))
            if total_entrevistados > 0:
                break
            print("Erro: A quantidade deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

    # Contadores para as respostas
    qtd_excelente = 0
    qtd_bom = 0
    qtd_ruim = 0

    print(f"Iniciando pesquisa com {total_entrevistados} clientes.\n")

    # Estrutura de repetição para coletar os dados dos entrevistados
    for i in range(1, total_entrevistados + 1):
        print(f"--- Entrevistado {i} de {total_entrevistados} ---")
        
        # Solicitação do Nome
        nome = input("Digite o nome do cliente: ").strip()
        while nome == "":
            print("Erro: O nome não pode estar vazio.")
            nome = input("Digite o nome do cliente: ").strip()
            
        # Solicitação e validação da Idade
        while True:
            try:
                idade = int(input("Digite a idade do cliente: "))
                if idade > 0:
                    break
                print("Erro: A idade deve ser maior que zero.")
            except ValueError:
                print("Erro: Digite um número inteiro válido para a idade.")
                
        # Solicitação e validação da Opinião
        while True:
            try:
                print("Opinião sobre o atendimento:")
                print(" [1] EXCELENTE")
                print(" [2] BOM")
                print(" [3] RUIM")
                opiniao = int(input("Digite o número correspondente (1, 2 ou 3): "))
                
                if opiniao in [1, 2, 3]:
                    break
                print("Erro: Opção inválida! Escolha 1, 2 ou 3.")
            except ValueError:
                print("Erro: Digite um número válido (1, 2 ou 3).")
                
        # Contabilização das respostas
        if opiniao == 1:
            qtd_excelente += 1
        elif opiniao == 2:
            qtd_bom += 1
        elif opiniao == 3:
            qtd_ruim += 1
            

    # Cálculo das porcentagens
    perc_excelente = (qtd_excelente / total_entrevistados) * 100
    perc_bom = (qtd_bom / total_entrevistados) * 100
    perc_ruim = (qtd_ruim / total_entrevistados) * 100

    # Exibição dos resultados finais com as porcentagens

    print("      RESULTADO FINAL DA PESQUISA    ")
    print(f"Total de entrevistados nesta sessão: {total_entrevistados}")
    print(f"a) Quantidade de respostas “EXCELENTE”: {qtd_excelente} ({perc_excelente:.1f}%)")
    print(f"   Quantidade de respostas “BOM”: {qtd_bom} ({perc_bom:.1f}%)")
    print(f"b) Quantidade de respostas “RUIM”: {qtd_ruim} ({perc_ruim:.1f}%)")
    
    # Pergunta se deseja realizar uma nova pesquisa

    continuar = input("\nDeseja realizar uma nova pesquisa? (s/n): ").strip().lower()
    if continuar != 's':
        print("\nEncerrando o programa de pesquisas. Obrigado!")
        break

    print("             INICIANDO NOVA PESQUISA")
    