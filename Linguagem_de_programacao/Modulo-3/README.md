# Análise de Dados de Vendas

Este projeto realiza uma análise completa dos dados de vendas de uma empresa de varejo, utilizando Python, SQLite, Pandas, Matplotlib e Seaborn.

## 📋 Funcionalidades

- **Conexão com Banco SQLite**: Cria e gerencia banco de dados local
- **Análise Exploratória**: Explora e prepara dados para análise
- **Análises Estatísticas**: Calcula métricas e insights dos dados
- **Visualizações**: Cria gráficos e heatmaps informativos
- **Relatório Final**: Gera insights e sugestões estratégicas

## 🚀 Como Executar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Executar o Programa

```bash
python analise_vendas.py
```

## 📊 Saídas do Programa

O programa gera os seguintes arquivos:

- `dados_vendas.db` - Banco de dados SQLite com os dados de vendas
- `analise_vendas_graficos.png` - Gráficos principais da análise
- `heatmap_vendas.png` - Heatmap de vendas por categoria e mês

## 📈 Análises Realizadas

1. **Análise por Categoria**: Vendas totais, ticket médio e quantidade por categoria
2. **Análise Temporal**: Vendas mensais e trimestrais
3. **Análise de Produtos**: Top produtos por valor de venda
4. **Visualizações**: Gráficos de pizza, barras, linhas e heatmap
5. **Insights Estratégicos**: Sugestões baseadas nos dados analisados

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **SQLite3** - Banco de dados
- **Pandas** - Manipulação de dados
- **Matplotlib** - Visualizações básicas
- **Seaborn** - Visualizações avançadas
- **NumPy** - Operações numéricas

## 📝 Estrutura do Código

- `conectar_banco_dados()` - Gerencia conexão e criação da tabela
- `explorar_dados()` - Carrega e prepara dados
- `analisar_dados()` - Realiza análises estatísticas
- `criar_visualizacoes()` - Gera gráficos e visualizações
- `gerar_relatorio_final()` - Cria relatório com insights
- `main()` - Função principal que orquestra todo o processo

## 🎯 Insights Principais

O programa identifica:
- Categoria líder em vendas
- Sazonalidade das vendas
- Produtos de maior performance
- Oportunidades de melhoria
- Sugestões estratégicas para a empresa

