#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int primeiroNumero, segundoNumero, terceiroNumero;

    printf("Digite o primeiro numero inteiro: ");
    if (scanf("%d", &primeiroNumero) != 1) {
        printf("Entrada invalida.\n");
        return 1;
    }

    printf("Digite o segundo numero inteiro: ");
    if (scanf("%d", &segundoNumero) != 1) {
        printf("Entrada invalida.\n");
        return 1;
    }

    printf("Digite o terceiro numero inteiro: ");
    if (scanf("%d", &terceiroNumero) != 1) {
        printf("Entrada invalida.\n");
        return 1;
    }

    // Operacoes aritmeticas
    long soma = (long)primeiroNumero + (long)segundoNumero + (long)terceiroNumero;
    long subtracao = (long)primeiroNumero - (long)segundoNumero - (long)terceiroNumero;
    long long multiplicacao = (long long)primeiroNumero * (long long)segundoNumero * (long long)terceiroNumero;

    printf("\n=== Resultados Aritmeticos ===\n");
    printf("Soma: %ld\n", soma);
    printf("Subtracao (a - b - c): %ld\n", subtracao);
    printf("Multiplicacao: %lld\n", multiplicacao);

    printf("Divisao (a / b / c): ");
    if (segundoNumero == 0 || terceiroNumero == 0) {
        printf("indefinida (divisao por zero).\n");
    } else {
        // Divisao real para evitar truncamento da divisao inteira
        double divisao = ((double)primeiroNumero / (double)segundoNumero) / (double)terceiroNumero;
        printf("%.6f\n", divisao);
    }

    // Operadores relacionais
    bool primeiroMaiorQueSegundo = primeiroNumero > segundoNumero;
    bool segundoMenorQueTerceiro = segundoNumero < terceiroNumero;

    printf("\n=== Comparacoes Relacionais ===\n");
    printf("Primeiro (> Segundo)? %s\n", primeiroMaiorQueSegundo ? "Verdadeiro" : "Falso");
    printf("Segundo (< Terceiro)? %s\n", segundoMenorQueTerceiro ? "Verdadeiro" : "Falso");

    // Operadores logicos
    bool primeiroPositivo = primeiroNumero > 0;
    bool segundoPar = (segundoNumero % 2 == 0);

    printf("\n=== Validacoes Logicas ===\n");
    printf("Primeiro numero positivo? %s\n", primeiroPositivo ? "Sim" : "Nao");
    printf("Segundo numero par? %s\n", segundoPar ? "Sim" : "Nao");

    if (primeiroPositivo && segundoPar) {
        printf("Condicao especial: o primeiro numero e positivo E o segundo e par.\n");
    } else {
        printf("Condicao especial NAO atendida.\n");
    }

    printf("\nTeste o programa com diferentes conjuntos de numeros para verificar todas as funcionalidades.\n");

    return 0;
}


