import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

def carregar_dados():
    """Carrega o conjunto de dados Iris do scikit-learn"""
    print("Carregando conjunto de dados Iris...")
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    print(f"Forma dos dados: {X.shape}")
    print(f"Classes disponíveis: {iris.target_names}")
    print(f"Características: {iris.feature_names}")
    
    return X, y, iris

def preprocessar_dados(X, y, test_size=0.2, random_state=42):
    """Divide os dados em treino/teste e normaliza"""
    print("\nPreprocessando dados...")
    
    # Dividir dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    print(f"Dados de treino: {X_train.shape}")
    print(f"Dados de teste: {X_test.shape}")
    
    # Normalizar os dados
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("Dados normalizados com sucesso!")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

def construir_modelo(input_shape, num_classes):
    """Constrói modelo de rede neural usando TensorFlow"""
    print(f"\nConstruindo modelo de rede neural...")
    print(f"Forma de entrada: {input_shape}")
    print(f"Número de classes: {num_classes}")
    
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(input_shape,)),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("Modelo construído com sucesso!")
    model.summary()
    
    return model

def treinar_modelo(model, X_train, y_train, X_test, y_test, epochs=100, batch_size=16):
    """Treina o modelo com os dados de treinamento"""
    print(f"\nIniciando treinamento do modelo...")
    print(f"Épocas: {epochs}, Batch size: {batch_size}")
    
    # Callback para parar o treinamento se não houver melhoria
    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=10,
        restore_best_weights=True
    )
    
    # Treinar o modelo
    history = model.fit(
        X_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(X_test, y_test),
        callbacks=[early_stopping],
        verbose=1
    )
    
    print("Treinamento concluído!")
    
    return history

def avaliar_modelo(model, X_test, y_test, iris):
    """Avalia a precisão do modelo usando os dados de teste"""
    print("\nAvaliando modelo...")
    
    # Avaliar perda e precisão
    test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
    
    print(f"Precisão no conjunto de teste: {test_accuracy:.4f}")
    print(f"Perda no conjunto de teste: {test_loss:.4f}")
    
    # Fazer previsões
    y_pred = model.predict(X_test)
    y_pred_classes = np.argmax(y_pred, axis=1)
    
    # Relatório de classificação
    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred_classes, target_names=iris.target_names))
    
    # Matriz de confusão
    print("\nMatriz de Confusão:")
    cm = confusion_matrix(y_test, y_pred_classes)
    print(cm)
    
    return test_accuracy, y_pred_classes

def fazer_previsoes(model, X_new, scaler, iris):
    """Faz previsões com o modelo treinado"""
    print("\nFazendo previsões...")
    
    # Normalizar novos dados
    X_new_scaled = scaler.transform(X_new)
    
    # Fazer previsões
    predictions = model.predict(X_new_scaled)
    predicted_classes = np.argmax(predictions, axis=1)
    
    # Mostrar resultados
    for i, (pred_class, confidence) in enumerate(zip(predicted_classes, np.max(predictions, axis=1))):
        print(f"Amostra {i+1}: {iris.target_names[pred_class]} (confiança: {confidence:.4f})")
    
    return predicted_classes, predictions

def plotar_historico_treinamento(history):
    """Plota gráficos do histórico de treinamento"""
    print("\nGerando gráficos do histórico de treinamento...")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Gráfico de precisão
    ax1.plot(history.history['accuracy'], label='Treino')
    ax1.plot(history.history['val_accuracy'], label='Validação')
    ax1.set_title('Precisão do Modelo')
    ax1.set_xlabel('Época')
    ax1.set_ylabel('Precisão')
    ax1.legend()
    ax1.grid(True)
    
    # Gráfico de perda
    ax2.plot(history.history['loss'], label='Treino')
    ax2.plot(history.history['val_loss'], label='Validação')
    ax2.set_title('Perda do Modelo')
    ax2.set_xlabel('Época')
    ax2.set_ylabel('Perda')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('historico_treinamento.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Gráficos salvos como 'historico_treinamento.png'")

def main():
    """Função principal que executa todo o pipeline"""
    print("=== CLASSIFICAÇÃO DE ESPÉCIES DE FLORES IRIS ===")
    print("Modelo de Machine Learning usando TensorFlow\n")
    
    # Passo 1: Carregar dados
    X, y, iris = carregar_dados()
    
    # Passo 2: Pré-processamento
    X_train, X_test, y_train, y_test, scaler = preprocessar_dados(X, y)
    
    # Passo 3: Construir modelo
    model = construir_modelo(X_train.shape[1], len(iris.target_names))
    
    # Passo 4: Treinar modelo
    history = treinar_modelo(model, X_train, y_train, X_test, y_test)
    
    # Passo 5: Avaliar modelo
    accuracy, y_pred = avaliar_modelo(model, X_test, y_test, iris)
    
    # Passo 6: Fazer previsões com dados de exemplo
    print("\n=== TESTANDO PREVISÕES ===")
    
    # Exemplos de dados para teste (valores típicos de cada espécie)
    exemplos = np.array([
        [5.1, 3.5, 1.4, 0.2],  # Setosa
        [6.2, 2.9, 4.3, 1.3],  # Versicolor
        [7.2, 3.0, 5.8, 1.6]   # Virginica
    ])
    
    print("Testando com exemplos típicos de cada espécie:")
    for i, exemplo in enumerate(exemplos):
        print(f"Exemplo {i+1}: {exemplo}")
    
    predicted_classes, predictions = fazer_previsoes(model, exemplos, scaler, iris)
    
    # Plotar histórico de treinamento
    plotar_historico_treinamento(history)
    
    print(f"\n=== RESUMO FINAL ===")
    print(f"Precisão final do modelo: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print("Modelo treinado e testado com sucesso!")
    
    return model, scaler, iris

if __name__ == "__main__":
    # Executar o pipeline completo
    model, scaler, iris = main()
