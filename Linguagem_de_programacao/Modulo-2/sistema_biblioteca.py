"""
Sistema de Gerenciamento de Livros para Biblioteca
Desenvolvido para gerenciar cadastro, listagem, busca e análise de livros
"""

import matplotlib.pyplot as plt
from collections import Counter


class Livro:
    """
    Classe que representa um livro na biblioteca
    Atributos: título, autor, gênero e quantidade disponível
    """
    
    def __init__(self, titulo, autor, genero, quantidade=1):
        """
        Inicializa um novo livro
        
        Args:
            titulo (str): Título do livro
            autor (str): Nome do autor
            genero (str): Gênero literário
            quantidade (int): Quantidade de exemplares disponíveis
        """
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade
    
    def __str__(self):
        """
        Retorna uma representação em string do livro
        """
        return f"Título: {self.titulo} | Autor: {self.autor} | Gênero: {self.genero} | Quantidade: {self.quantidade}"
    
    def __repr__(self):
        """
        Retorna uma representação técnica do objeto
        """
        return f"Livro('{self.titulo}', '{self.autor}', '{self.genero}', {self.quantidade})"


# Lista global para armazenar todos os livros da biblioteca
biblioteca = []


def cadastrar_livro():
    """
    Função para cadastrar um novo livro na biblioteca
    Solicita informações do usuário e adiciona o livro à lista
    """
    print("\n=== CADASTRAR NOVO LIVRO ===")
    
    try:
        titulo = input("Digite o título do livro: ").strip()
        if not titulo:
            print("Erro: Título não pode estar vazio!")
            return
        
        autor = input("Digite o nome do autor: ").strip()
        if not autor:
            print("Erro: Autor não pode estar vazio!")
            return
        
        genero = input("Digite o gênero do livro: ").strip()
        if not genero:
            print("Erro: Gênero não pode estar vazio!")
            return
        
        quantidade = int(input("Digite a quantidade de exemplares (padrão: 1): ") or "1")
        if quantidade < 0:
            print("Erro: Quantidade não pode ser negativa!")
            return
        
        # Verifica se já existe um livro com o mesmo título
        for livro in biblioteca:
            if livro.titulo.lower() == titulo.lower():
                print(f"Livro '{titulo}' já existe na biblioteca!")
                opcao = input("Deseja adicionar mais exemplares? (s/n): ").lower()
                if opcao == 's':
                    livro.quantidade += quantidade
                    print(f"Adicionados {quantidade} exemplares. Total: {livro.quantidade}")
                return
        
        # Cria e adiciona o novo livro
        novo_livro = Livro(titulo, autor, genero, quantidade)
        biblioteca.append(novo_livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!")
        
    except ValueError:
        print("Erro: Quantidade deve ser um número inteiro!")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def listar_livros():
    """
    Função para listar todos os livros cadastrados na biblioteca
    """
    print("\n=== LISTA DE LIVROS ===")
    
    if not biblioteca:
        print("Nenhum livro cadastrado na biblioteca.")
        return
    
    print(f"Total de livros cadastrados: {len(biblioteca)}")
    print("-" * 80)
    
    for i, livro in enumerate(biblioteca, 1):
        print(f"{i}. {livro}")
    
    print("-" * 80)


def buscar_livro():
    """
    Função para buscar um livro pelo título
    """
    print("\n=== BUSCAR LIVRO ===")
    
    if not biblioteca:
        print("Nenhum livro cadastrado na biblioteca.")
        return
    
    titulo_busca = input("Digite o título do livro para buscar: ").strip().lower()
    
    if not titulo_busca:
        print("Erro: Título não pode estar vazio!")
        return
    
    livros_encontrados = []
    
    # Busca livros que contenham o título pesquisado
    for livro in biblioteca:
        if titulo_busca in livro.titulo.lower():
            livros_encontrados.append(livro)
    
    if livros_encontrados:
        print(f"\nEncontrados {len(livros_encontrados)} livro(s) com o título '{titulo_busca}':")
        print("-" * 80)
        for i, livro in enumerate(livros_encontrados, 1):
            print(f"{i}. {livro}")
        print("-" * 80)
    else:
        print(f"Nenhum livro encontrado com o título '{titulo_busca}'.")


def gerar_grafico_generos():
    """
    Função para gerar um gráfico com a quantidade de livros por gênero
    """
    print("\n=== GRÁFICO DE LIVROS POR GÊNERO ===")
    
    if not biblioteca:
        print("Nenhum livro cadastrado na biblioteca.")
        return
    
    # Conta a quantidade de livros por gênero
    generos = [livro.genero for livro in biblioteca]
    contador_generos = Counter(generos)
    
    # Prepara os dados para o gráfico
    generos_nomes = list(contador_generos.keys())
    quantidades = list(contador_generos.values())
    
    # Cria o gráfico
    plt.figure(figsize=(12, 6))
    plt.bar(generos_nomes, quantidades, color='skyblue', edgecolor='navy', alpha=0.7)
    plt.title('Quantidade de Livros por Gênero', fontsize=16, fontweight='bold')
    plt.xlabel('Gêneros', fontsize=12)
    plt.ylabel('Quantidade de Livros', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    
    # Adiciona valores nas barras
    for i, v in enumerate(quantidades):
        plt.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    # Exibe estatísticas no console
    print(f"\nEstatísticas por gênero:")
    print("-" * 40)
    for genero, quantidade in contador_generos.items():
        print(f"{genero}: {quantidade} livro(s)")


def exibir_estatisticas():
    """
    Função para exibir estatísticas gerais da biblioteca
    """
    print("\n=== ESTATÍSTICAS DA BIBLIOTECA ===")
    
    if not biblioteca:
        print("Nenhum livro cadastrado na biblioteca.")
        return
    
    total_livros = len(biblioteca)
    total_exemplares = sum(livro.quantidade for livro in biblioteca)
    generos_unicos = len(set(livro.genero for livro in biblioteca))
    autores_unicos = len(set(livro.autor for livro in biblioteca))
    
    print(f"Total de títulos únicos: {total_livros}")
    print(f"Total de exemplares: {total_exemplares}")
    print(f"Gêneros diferentes: {generos_unicos}")
    print(f"Autores diferentes: {autores_unicos}")
    
    # Gênero mais comum
    generos = [livro.genero for livro in biblioteca]
    genero_mais_comum = Counter(generos).most_common(1)[0]
    print(f"Gênero mais comum: {genero_mais_comum[0]} ({genero_mais_comum[1]} livros)")


def menu_principal():
    """
    Função que exibe o menu principal e gerencia as opções do usuário
    """
    while True:
        print("\n" + "="*50)
        print("    SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
        print("="*50)
        print("1. Cadastrar novo livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro por título")
        print("4. Gerar gráfico de livros por gênero")
        print("5. Exibir estatísticas")
        print("6. Sair do sistema")
        print("="*50)
        
        try:
            opcao = input("Escolha uma opção (1-6): ").strip()
            
            if opcao == '1':
                cadastrar_livro()
            elif opcao == '2':
                listar_livros()
            elif opcao == '3':
                buscar_livro()
            elif opcao == '4':
                gerar_grafico_generos()
            elif opcao == '5':
                exibir_estatisticas()
            elif opcao == '6':
                print("\nObrigado por usar o Sistema de Gerenciamento de Biblioteca!")
                break
            else:
                print("Opção inválida! Escolha uma opção de 1 a 6.")
                
        except KeyboardInterrupt:
            print("\n\nSistema interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")


def adicionar_livros_exemplo():
    """
    Função para adicionar alguns livros de exemplo para demonstração
    """
    livros_exemplo = [
        Livro("Dom Casmurro", "Machado de Assis", "Romance", 3),
        Livro("O Cortiço", "Aluísio Azevedo", "Romance", 2),
        Livro("Capitães da Areia", "Jorge Amado", "Romance", 4),
        Livro("O Alienista", "Machado de Assis", "Ficção", 2),
        Livro("A Hora da Estrela", "Clarice Lispector", "Ficção", 3),
        Livro("Vidas Secas", "Graciliano Ramos", "Romance", 2),
        Livro("O Guarani", "José de Alencar", "Romance", 1),
        Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", "Romance", 3),
        Livro("O Quinze", "Rachel de Queiroz", "Romance", 2),
        Livro("Macunaíma", "Mário de Andrade", "Ficção", 1),
        Livro("Grande Sertão: Veredas", "João Guimarães Rosa", "Romance", 2),
        Livro("A Moreninha", "Joaquim Manuel de Macedo", "Romance", 1),
        Livro("O Tempo e o Vento", "Érico Veríssimo", "Romance", 3),
        Livro("Casa-Grande & Senzala", "Gilberto Freyre", "História", 2),
        Livro("Os Sertões", "Euclides da Cunha", "História", 1)
    ]
    
    biblioteca.extend(livros_exemplo)
    print(f"Adicionados {len(livros_exemplo)} livros de exemplo à biblioteca.")


if __name__ == "__main__":
    """
    Função principal que inicia o sistema
    """
    print("Bem-vindo ao Sistema de Gerenciamento de Biblioteca!")
    
    # Pergunta se o usuário quer adicionar livros de exemplo
    adicionar_exemplos = input("Deseja adicionar livros de exemplo para demonstração? (s/n): ").lower()
    if adicionar_exemplos == 's':
        adicionar_livros_exemplo()
    
    # Inicia o menu principal
    menu_principal()
