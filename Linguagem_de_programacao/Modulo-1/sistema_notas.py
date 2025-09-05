def cadastrar_notas():
    """
    Função para cadastrar notas dos alunos
    Retorna uma lista com as notas inseridas
    """
    notas = []
    print("\n=== CADASTRO DE NOTAS ===")
    print("Digite as notas do aluno (digite -1 para finalizar):")
    
    while True:
        try:
            nota = float(input("Digite uma nota (0 a 10): "))
            
            if nota == -1:
                break
            elif nota < 0 or nota > 10:
                print("Erro: A nota deve estar entre 0 e 10!")
                continue
            
            notas.append(nota)
            print(f"Nota {nota} adicionada com sucesso!")
            
        except ValueError:
            print("Erro: Digite um número válido!")
    
    return notas

def calcular_media(notas):
    """
    Função para calcular a média das notas
    Retorna a média calculada
    """
    if not notas:
        return 0
    
    soma = sum(notas)
    media = soma / len(notas)
    return media

def determinar_situacao(media):
    """
    Função para determinar a situação do aluno
    Retorna 'Aprovado' ou 'Reprovado'
    """
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_relatorio(notas, media, situacao):
    """
    Função para exibir o relatório final
    """
    print("\n" + "="*50)
    print("           RELATÓRIO FINAL")
    print("="*50)
    
    print(f"Notas inseridas: {notas}")
    print(f"Quantidade de notas: {len(notas)}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    
    if situacao == "Aprovado":
        print("🎉 Parabéns! Você foi aprovado!")
    else:
        print("📚 Estude mais para a próxima vez!")
    
    print("="*50)

def menu_principal():
    """
    Função principal que controla o fluxo do programa
    """
    print("="*50)
    print("    SISTEMA DE GESTÃO DE NOTAS DE ALUNOS")
    print("="*50)
    
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Cadastrar notas")
        print("2. Sair do sistema")
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 1:
                # Cadastrar notas
                notas = cadastrar_notas()
                
                if not notas:
                    print("Nenhuma nota foi cadastrada!")
                    continue
                
                # Calcular média
                media = calcular_media(notas)
                
                # Determinar situação
                situacao = determinar_situacao(media)
                
                # Exibir relatório
                exibir_relatorio(notas, media, situacao)
                
            elif opcao == 2:
                print("\nObrigado por usar o sistema!")
                break
            else:
                print("Opção inválida! Escolha 1 ou 2.")
                
        except ValueError:
            print("Erro: Digite um número válido!")

if __name__ == "__main__":
    menu_principal()
