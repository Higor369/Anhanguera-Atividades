import sqlite3
import pandas as pd

def teste_basico():
    """Teste básico para verificar se as bibliotecas estão funcionando"""
    print("=== TESTE BÁSICO ===")
    
    # Teste SQLite
    conexao = sqlite3.connect('teste.db')
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS teste (id INTEGER, nome TEXT)')
    cursor.execute('INSERT INTO teste VALUES (1, "teste")')
    conexao.commit()
    print("✓ SQLite funcionando")
    
    # Teste Pandas
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print("✓ Pandas funcionando")
    print(df.head())
    
    # Teste Matplotlib
    try:
        import matplotlib.pyplot as plt
        plt.figure(figsize=(6, 4))
        plt.plot([1, 2, 3], [1, 4, 2])
        plt.title('Teste Matplotlib')
        plt.savefig('teste_matplotlib.png')
        plt.close()
        print("✓ Matplotlib funcionando")
    except Exception as e:
        print(f"❌ Erro no Matplotlib: {e}")
    
    # Teste Seaborn
    try:
        import seaborn as sns
        print("✓ Seaborn funcionando")
    except Exception as e:
        print(f"❌ Erro no Seaborn: {e}")
    
    conexao.close()
    print("Teste concluído!")

if __name__ == "__main__":
    teste_basico()

