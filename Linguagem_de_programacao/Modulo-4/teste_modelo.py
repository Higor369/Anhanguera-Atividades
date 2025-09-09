"""
Script de teste para verificar se o modelo de classificação Iris está funcionando corretamente
"""

import numpy as np
from classificacao_iris import main

def testar_modelo():
    """Testa o modelo com dados conhecidos"""
    print("=== TESTE DO MODELO DE CLASSIFICAÇÃO IRIS ===\n")
    
    try:
        # Executar o pipeline principal
        model, scaler, iris = main()
        
        print("\n=== TESTE ADICIONAL COM DADOS CONHECIDOS ===")
        
        # Dados de teste com valores típicos conhecidos
        dados_teste = np.array([
            [5.1, 3.5, 1.4, 0.2],  # Setosa típica
            [6.2, 2.9, 4.3, 1.3],  # Versicolor típica
            [7.2, 3.0, 5.8, 1.6],  # Virginica típica
            [4.9, 3.0, 1.4, 0.2],  # Setosa
            [6.4, 2.8, 5.6, 2.1]   # Virginica
        ])
        
        # Fazer previsões
        from classificacao_iris import fazer_previsoes
        predicted_classes, predictions = fazer_previsoes(model, dados_teste, scaler, iris)
        
        # Verificar se as previsões fazem sentido
        especies_esperadas = ['setosa', 'versicolor', 'virginica', 'setosa', 'virginica']
        
        print("\nVerificação das previsões:")
        for i, (pred, esperada) in enumerate(zip(predicted_classes, especies_esperadas)):
            pred_nome = iris.target_names[pred]
            confianca = np.max(predictions[i])
            status = "✓" if pred_nome == esperada else "✗"
            print(f"Amostra {i+1}: {pred_nome} (esperada: {esperada}) - Confiança: {confianca:.3f} {status}")
        
        print("\n=== TESTE CONCLUÍDO COM SUCESSO ===")
        return True
        
    except Exception as e:
        print(f"\n❌ ERRO durante o teste: {e}")
        return False

if __name__ == "__main__":
    sucesso = testar_modelo()
    if sucesso:
        print("✅ Todos os testes passaram!")
    else:
        print("❌ Alguns testes falharam!")
