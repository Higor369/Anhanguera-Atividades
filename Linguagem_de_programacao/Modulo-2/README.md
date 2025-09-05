# Sistema de Gerenciamento de Biblioteca

Sistema simples desenvolvido em Python para gerenciar livros em uma biblioteca, permitindo cadastrar, listar, buscar livros e gerar gráficos de análise.

## Funcionalidades

- ✅ Cadastrar novos livros
- ✅ Listar todos os livros disponíveis
- ✅ Buscar livros por título
- ✅ Gerar gráfico com quantidade de livros por gênero
- ✅ Exibir estatísticas da biblioteca
- ✅ Interface de menu interativo

## Instalação

1. Certifique-se de ter Python 3.7+ instalado
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como usar

Execute o sistema:
```bash
python sistema_biblioteca.py
```

O sistema oferece um menu interativo com as seguintes opções:

1. **Cadastrar novo livro** - Adiciona um novo livro à biblioteca
2. **Listar todos os livros** - Mostra todos os livros cadastrados
3. **Buscar livro por título** - Encontra livros pelo título
4. **Gerar gráfico de livros por gênero** - Cria um gráfico de barras
5. **Exibir estatísticas** - Mostra estatísticas gerais da biblioteca
6. **Sair do sistema** - Encerra o programa

## Estrutura do Projeto

- `sistema_biblioteca.py` - Arquivo principal com todo o código
- `requirements.txt` - Dependências do projeto
- `README.md` - Este arquivo de documentação

## Classe Livro

Cada livro possui os seguintes atributos:
- **título**: Nome do livro
- **autor**: Nome do autor
- **gênero**: Gênero literário
- **quantidade**: Número de exemplares disponíveis

## Exemplo de Uso

Ao iniciar o sistema, você pode optar por adicionar livros de exemplo para demonstração. O sistema inclui 15 livros clássicos da literatura brasileira para teste.

## Tecnologias Utilizadas

- Python 3.7+
- Matplotlib (para geração de gráficos)
- Collections (para contagem de elementos)
