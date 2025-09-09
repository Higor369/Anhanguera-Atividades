# Classificação de Espécies de Flores Iris

Este projeto implementa um modelo de Machine Learning usando TensorFlow para classificar espécies de flores Iris baseado em características morfológicas.

## Descrição

O modelo utiliza uma rede neural artificial para classificar flores Iris em três espécies:
- **Iris Setosa**
- **Iris Versicolor** 
- **Iris Virginica**

Com base em quatro características:
- Comprimento da sépala
- Largura da sépala
- Comprimento da pétala
- Largura da pétala

## Instalação

1. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

## Como Executar

Execute o arquivo principal:
```bash
python classificacao_iris.py
```

## Funcionalidades

- ✅ Carregamento automático do dataset Iris do scikit-learn
- ✅ Pré-processamento dos dados (divisão treino/teste e normalização)
- ✅ Construção de rede neural com TensorFlow
- ✅ Treinamento do modelo com early stopping
- ✅ Avaliação completa (precisão, relatório de classificação, matriz de confusão)
- ✅ Sistema de previsões para novos dados
- ✅ Visualização do histórico de treinamento
- ✅ Código bem documentado e modular

## Estrutura do Modelo

O modelo utiliza uma arquitetura de rede neural com:
- Camada de entrada: 4 neurônios (características)
- Camada oculta 1: 64 neurônios com ativação ReLU
- Dropout: 0.3
- Camada oculta 2: 32 neurônios com ativação ReLU
- Dropout: 0.3
- Camada de saída: 3 neurônios com ativação Softmax

## Resultados Esperados

O modelo geralmente alcança precisão superior a 95% no conjunto de teste, demonstrando excelente capacidade de classificação das espécies de Iris.
