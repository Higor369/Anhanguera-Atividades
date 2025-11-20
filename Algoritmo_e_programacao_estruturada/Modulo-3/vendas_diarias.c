#include <stdio.h>

int main(void) {
    // Declaração do vetor de tamanho 5 para armazenar números inteiros
    int vendas[5];
    int soma = 0;
    int i;
    
    printf("=== Sistema de Analise de Vendas Diarias ===\n");
    printf("Digite a quantidade de vendas realizadas em cada um dos 5 dias.\n\n");
    
    // Solicita ao usuário que insira 5 valores inteiros
    for (i = 0; i < 5; i++) {
        printf("Digite a quantidade de vendas do dia %d: ", i + 1);
        fflush(stdout); // Garante que a mensagem seja exibida antes da leitura
        
        // Lê o valor e armazena no vetor
        int resultado = scanf("%d", &vendas[i]);
        
        // Limpa o buffer de entrada (remove caracteres extras, incluindo o \n)
        int c;
        while ((c = getchar()) != '\n' && c != EOF);
        
        if (resultado != 1) {
            printf("Entrada invalida. Por favor, digite um numero inteiro.\n");
            return 1;
        }
    }
    
    // Calcula a soma de todos os valores do vetor
    for (i = 0; i < 5; i++) {
        soma += vendas[i];
    }
    
    // Exibe todos os elementos do vetor, um por linha
    printf("\n=== Relatorio de Vendas ===\n");
    printf("Quantidade de vendas por dia:\n");
    for (i = 0; i < 5; i++) {
        printf("Dia %d: %d vendas\n", i + 1, vendas[i]);
    }
    
    // Exibe a soma total dos valores
    printf("\n=== Total Geral ===\n");
    printf("Quantidade total de vendas no periodo: %d\n", soma);
    
    return 0;
}

