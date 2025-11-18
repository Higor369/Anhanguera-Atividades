#include <stdio.h>

int main(void) {
    int numero;
    int soma = 0;

    printf("=== Calculadora de Soma ===\n");
    printf("Digite numeros inteiros para somar.\n");
    printf("Digite 0 (zero) para encerrar e ver o resultado.\n\n");

    // Solicita o primeiro número
    printf("Digite um numero inteiro: ");
    
    // Lê o primeiro número antes de entrar no loop
    if (scanf("%d", &numero) != 1) {
        printf("Entrada invalida.\n");
        return 1;
    }

    // Estrutura de repetição while com teste da condição no início
    while (numero != 0) {
        // Adiciona o número à soma
        soma += numero;
        
        // Solicita o próximo número
        printf("Digite outro numero inteiro (ou 0 para encerrar): ");
        
        // Lê o próximo número
        if (scanf("%d", &numero) != 1) {
            printf("Entrada invalida. Encerrando o programa.\n");
            break;
        }
    }

    // Exibe o resultado final da soma
    printf("\n=== Resultado Final ===\n");
    printf("A soma de todos os numeros inseridos e: %d\n", soma);
    printf("\nPrograma encerrado. Obrigado!\n");

    return 0;
}

