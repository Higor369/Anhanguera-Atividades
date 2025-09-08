import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

# Configuração para exibir gráficos em português
plt.rcParams['font.family'] = 'DejaVu Sans'
sns.set_style("whitegrid")

def conectar_banco_dados():
    """Conecta ao banco de dados SQLite e cria a tabela de vendas"""
    print("=== PASSO 1: CONECTANDO AO BANCO DE DADOS ===")
    
    # Conectar ao banco de dados (ou criar, se não existir)
    conexao = sqlite3.connect('dados_vendas.db')
    cursor = conexao.cursor()
    
    # Criar uma tabela (se não existir)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
    )
    ''')
    
    # Inserir dados de vendas
    dados_vendas = [
        ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
        ('2023-01-05', 'Produto B', 'Roupas', 350.00),
        ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
        ('2023-03-15', 'Produto D', 'Livros', 200.00),
        ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
        ('2023-04-02', 'Produto F', 'Roupas', 400.00),
        ('2023-05-05', 'Produto G', 'Livros', 150.00),
        ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
        ('2023-07-20', 'Produto I', 'Roupas', 600.00),
        ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
        ('2023-09-30', 'Produto K', 'Livros', 300.00),
        ('2023-10-05', 'Produto L', 'Roupas', 450.00),
        ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
        ('2023-12-20', 'Produto N', 'Livros', 250.00)
    ]
    
    # Limpar dados existentes e inserir novos
    cursor.execute('DELETE FROM vendas1')
    cursor.executemany('''
    INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) 
    VALUES (?, ?, ?, ?)
    ''', dados_vendas)
    
    # Confirmar as mudanças
    conexao.commit()
    print("✓ Banco de dados criado e dados inseridos com sucesso!")
    
    return conexao

def explorar_dados(conexao):
    """Explora e prepara os dados para análise"""
    print("\n=== PASSO 2: EXPLORANDO E PREPARANDO OS DADOS ===")
    
    # Carregar dados do banco para DataFrame
    df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)
    
    # Converter data_venda para datetime
    df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
    
    # Adicionar colunas derivadas
    df_vendas['mes'] = df_vendas['data_venda'].dt.month
    df_vendas['trimestre'] = df_vendas['data_venda'].dt.quarter
    df_vendas['ano'] = df_vendas['data_venda'].dt.year
    
    print("✓ Dados carregados e preparados:")
    print(f"  - Total de registros: {len(df_vendas)}")
    print(f"  - Período: {df_vendas['data_venda'].min().strftime('%d/%m/%Y')} a {df_vendas['data_venda'].max().strftime('%d/%m/%Y')}")
    print(f"  - Categorias: {', '.join(df_vendas['categoria'].unique())}")
    print(f"  - Valor total das vendas: R$ {df_vendas['valor_venda'].sum():,.2f}")
    
    print("\nPrimeiras 5 linhas dos dados:")
    print(df_vendas.head())
    
    print("\nInformações gerais do dataset:")
    print(df_vendas.info())
    
    return df_vendas

def analisar_dados(df_vendas):
    """Realiza análises específicas dos dados"""
    print("\n=== PASSO 3: ANÁLISE DOS DADOS ===")
    
    # Análise por categoria
    print("\n1. ANÁLISE POR CATEGORIA:")
    vendas_por_categoria = df_vendas.groupby('categoria').agg({
        'valor_venda': ['sum', 'mean', 'count']
    }).round(2)
    vendas_por_categoria.columns = ['Total_Vendas', 'Ticket_Medio', 'Quantidade_Vendas']
    print(vendas_por_categoria)
    
    # Análise mensal
    print("\n2. ANÁLISE MENSAL:")
    vendas_mensais = df_vendas.groupby('mes').agg({
        'valor_venda': ['sum', 'count']
    }).round(2)
    vendas_mensais.columns = ['Total_Vendas', 'Quantidade_Vendas']
    print(vendas_mensais)
    
    # Análise por trimestre
    print("\n3. ANÁLISE POR TRIMESTRE:")
    vendas_trimestrais = df_vendas.groupby('trimestre').agg({
        'valor_venda': ['sum', 'mean', 'count']
    }).round(2)
    vendas_trimestrais.columns = ['Total_Vendas', 'Ticket_Medio', 'Quantidade_Vendas']
    print(vendas_trimestrais)
    
    # Estatísticas descritivas
    print("\n4. ESTATÍSTICAS DESCRITIVAS:")
    print(df_vendas['valor_venda'].describe())
    
    # Produtos mais vendidos
    print("\n5. PRODUTOS MAIS VENDIDOS (por valor):")
    produtos_top = df_vendas.nlargest(5, 'valor_venda')[['produto', 'categoria', 'valor_venda']]
    print(produtos_top)
    
    return {
        'vendas_por_categoria': vendas_por_categoria,
        'vendas_mensais': vendas_mensais,
        'vendas_trimestrais': vendas_trimestrais,
        'produtos_top': produtos_top
    }

def criar_visualizacoes(df_vendas, analises):
    """Cria visualizações dos dados"""
    print("\n=== PASSO 4: CRIANDO VISUALIZAÇÕES ===")
    
    # Configurar o estilo dos gráficos
    plt.style.use('seaborn-v0_8')
    fig = plt.figure(figsize=(20, 15))
    
    # Gráfico 1: Vendas por categoria
    plt.subplot(2, 3, 1)
    vendas_cat = analises['vendas_por_categoria']['Total_Vendas']
    plt.pie(vendas_cat.values, labels=vendas_cat.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribuição de Vendas por Categoria', fontsize=14, fontweight='bold')
    
    # Gráfico 2: Vendas mensais
    plt.subplot(2, 3, 2)
    meses = analises['vendas_mensais'].index
    vendas_mes = analises['vendas_mensais']['Total_Vendas']
    plt.bar(meses, vendas_mes, color='skyblue', edgecolor='navy')
    plt.title('Vendas Mensais', fontsize=14, fontweight='bold')
    plt.xlabel('Mês')
    plt.ylabel('Valor das Vendas (R$)')
    plt.xticks(meses)
    
    # Gráfico 3: Vendas por trimestre
    plt.subplot(2, 3, 3)
    trimestres = analises['vendas_trimestrais'].index
    vendas_trim = analises['vendas_trimestrais']['Total_Vendas']
    plt.bar(trimestres, vendas_trim, color='lightgreen', edgecolor='darkgreen')
    plt.title('Vendas por Trimestre', fontsize=14, fontweight='bold')
    plt.xlabel('Trimestre')
    plt.ylabel('Valor das Vendas (R$)')
    plt.xticks(trimestres)
    
    # Gráfico 4: Ticket médio por categoria
    plt.subplot(2, 3, 4)
    ticket_medio = analises['vendas_por_categoria']['Ticket_Medio']
    plt.bar(ticket_medio.index, ticket_medio.values, color='orange', edgecolor='darkorange')
    plt.title('Ticket Médio por Categoria', fontsize=14, fontweight='bold')
    plt.xlabel('Categoria')
    plt.ylabel('Ticket Médio (R$)')
    plt.xticks(rotation=45)
    
    # Gráfico 5: Evolução temporal das vendas
    plt.subplot(2, 3, 5)
    df_vendas_ordenado = df_vendas.sort_values('data_venda')
    plt.plot(df_vendas_ordenado['data_venda'], df_vendas_ordenado['valor_venda'], 
             marker='o', linewidth=2, markersize=6)
    plt.title('Evolução Temporal das Vendas', fontsize=14, fontweight='bold')
    plt.xlabel('Data')
    plt.ylabel('Valor da Venda (R$)')
    plt.xticks(rotation=45)
    
    # Gráfico 6: Top 5 produtos
    plt.subplot(2, 3, 6)
    produtos_top = analises['produtos_top']
    plt.barh(produtos_top['produto'], produtos_top['valor_venda'], color='purple', alpha=0.7)
    plt.title('Top 5 Produtos por Valor', fontsize=14, fontweight='bold')
    plt.xlabel('Valor da Venda (R$)')
    
    plt.tight_layout()
    plt.savefig('analise_vendas_graficos.png', dpi=300, bbox_inches='tight')
    print("✓ Gráficos salvos em 'analise_vendas_graficos.png'")
    
    # Gráfico adicional: Heatmap de vendas por categoria e mês
    plt.figure(figsize=(12, 8))
    pivot_table = df_vendas.pivot_table(values='valor_venda', index='categoria', columns='mes', aggfunc='sum', fill_value=0)
    sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='YlOrRd', cbar_kws={'label': 'Valor das Vendas (R$)'})
    plt.title('Heatmap: Vendas por Categoria e Mês', fontsize=16, fontweight='bold')
    plt.xlabel('Mês')
    plt.ylabel('Categoria')
    plt.tight_layout()
    plt.savefig('heatmap_vendas.png', dpi=300, bbox_inches='tight')
    print("✓ Heatmap salvo em 'heatmap_vendas.png'")
    
    plt.show()

def gerar_relatorio_final(df_vendas, analises):
    """Gera relatório final com insights e sugestões"""
    print("\n=== PASSO 5: RELATÓRIO FINAL E INSIGHTS ===")
    
    # Calcular métricas principais
    total_vendas = df_vendas['valor_venda'].sum()
    ticket_medio_geral = df_vendas['valor_venda'].mean()
    categoria_top = analises['vendas_por_categoria']['Total_Vendas'].idxmax()
    mes_melhor = analises['vendas_mensais']['Total_Vendas'].idxmax()
    trimestre_melhor = analises['vendas_trimestrais']['Total_Vendas'].idxmax()
    
    print("=" * 60)
    print("           RELATÓRIO DE ANÁLISE DE VENDAS 2023")
    print("=" * 60)
    
    print(f"\n📊 MÉTRICAS PRINCIPAIS:")
    print(f"   • Total de vendas: R$ {total_vendas:,.2f}")
    print(f"   • Ticket médio: R$ {ticket_medio_geral:,.2f}")
    print(f"   • Total de transações: {len(df_vendas)}")
    print(f"   • Categorias ativas: {len(df_vendas['categoria'].unique())}")
    
    print(f"\n🏆 DESTAQUES:")
    print(f"   • Categoria líder: {categoria_top} (R$ {analises['vendas_por_categoria'].loc[categoria_top, 'Total_Vendas']:,.2f})")
    print(f"   • Melhor mês: {mes_melhor} (R$ {analises['vendas_mensais'].loc[mes_melhor, 'Total_Vendas']:,.2f})")
    print(f"   • Melhor trimestre: {trimestre_melhor}º (R$ {analises['vendas_trimestrais'].loc[trimestre_melhor, 'Total_Vendas']:,.2f})")
    
    print(f"\n💡 INSIGHTS E ANÁLISES:")
    
    # Análise de sazonalidade
    vendas_por_mes = analises['vendas_mensais']['Total_Vendas']
    variacao_max = ((vendas_por_mes.max() - vendas_por_mes.min()) / vendas_por_mes.min()) * 100
    print(f"   • Sazonalidade: Variação de {variacao_max:.1f}% entre melhor e pior mês")
    
    # Análise de concentração por categoria
    concentracao_eletronicos = (analises['vendas_por_categoria'].loc['Eletrônicos', 'Total_Vendas'] / total_vendas) * 100
    print(f"   • Concentração: Eletrônicos representam {concentracao_eletronicos:.1f}% do faturamento")
    
    # Análise de ticket médio por categoria
    ticket_eletronicos = analises['vendas_por_categoria'].loc['Eletrônicos', 'Ticket_Medio']
    ticket_roupas = analises['vendas_por_categoria'].loc['Roupas', 'Ticket_Medio']
    print(f"   • Ticket médio Eletrônicos: R$ {ticket_eletronicos:,.2f} vs Roupas: R$ {ticket_roupas:,.2f}")
    
    print(f"\n🎯 SUGESTÕES ESTRATÉGICAS:")
    print(f"   1. FOCO EM ELETRÔNICOS:")
    print(f"      - Categoria com maior faturamento e ticket médio")
    print(f"      - Investir em marketing e estoque para esta categoria")
    
    print(f"   2. OTIMIZAÇÃO SAZONAL:")
    print(f"      - Mês {mes_melhor} é o mais forte - preparar campanhas especiais")
    print(f"      - Identificar causas da baixa em outros meses")
    
    print(f"   3. DIVERSIFICAÇÃO:")
    print(f"      - Reduzir dependência excessiva de Eletrônicos")
    print(f"      - Desenvolver estratégias para aumentar vendas de Livros e Roupas")
    
    print(f"   4. ANÁLISE DE PRODUTOS:")
    print(f"      - Investigar por que alguns produtos têm performance superior")
    print(f"      - Replicar estratégias de sucesso para outros produtos")
    
    print(f"\n📈 PRÓXIMOS PASSOS RECOMENDADOS:")
    print(f"   • Implementar análise de tendências mais detalhada")
    print(f"   • Criar dashboard em tempo real para monitoramento")
    print(f"   • Desenvolver previsões de demanda por categoria")
    print(f"   • Estabelecer metas mensais baseadas em dados históricos")
    
    print("=" * 60)
    print("Relatório gerado com sucesso! 📊")

def main():
    """Função principal que executa todo o processo de análise"""
    try:
        print("🚀 INICIANDO ANÁLISE DE DADOS DE VENDAS")
        print("=" * 50)
        
        # Passo 1: Conectar ao banco de dados
        conexao = conectar_banco_dados()
        
        # Passo 2: Explorar dados
        df_vendas = explorar_dados(conexao)
        
        # Passo 3: Analisar dados
        analises = analisar_dados(df_vendas)
        
        # Passo 4: Criar visualizações
        criar_visualizacoes(df_vendas, analises)
        
        # Passo 5: Gerar relatório final
        gerar_relatorio_final(df_vendas, analises)
        
        # Fechar conexão
        conexao.close()
        print(f"\n✅ Análise concluída com sucesso!")
        print(f"📁 Arquivos gerados:")
        print(f"   • dados_vendas.db (banco de dados)")
        print(f"   • analise_vendas_graficos.png (gráficos principais)")
        print(f"   • heatmap_vendas.png (heatmap de vendas)")
        
    except Exception as e:
        print(f"❌ Erro durante a execução: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    main()

