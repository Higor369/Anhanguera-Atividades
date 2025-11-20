#include <stdio.h>

// Função para calcular o salário bruto
float calcular_salario_bruto(float valor_hora, float horas_trabalhadas) {
    return valor_hora * horas_trabalhadas;
}

// Função para calcular o desconto (9% sobre o salário bruto)
float calcular_desconto(float salario_bruto) {
    return salario_bruto * 0.09;
}

// Função para calcular o salário líquido
float calcular_salario_liquido(float salario_bruto, float desconto) {
    return salario_bruto - desconto;
}

int main(void) {
    float valor_hora, horas_trabalhadas;
    float salario_bruto, desconto, salario_liquido;
    
    printf("=== Sistema de Calculo de Salario ===\n");
    printf("Este programa calcula o salario bruto, descontos e salario liquido.\n\n");
    
    // Solicita o valor da hora de trabalho
    printf("Digite o valor da sua hora de trabalho: R$ ");
    
    if (scanf("%f", &valor_hora) != 1) {
        printf("Entrada invalida. Por favor, digite um numero valido.\n");
        return 1;
    }
    
    // Solicita a quantidade de horas trabalhadas
    printf("Digite a quantidade de horas trabalhadas no mes: ");
    
    if (scanf("%f", &horas_trabalhadas) != 1) {
        printf("Entrada invalida. Por favor, digite um numero valido.\n");
        return 1;
    }
    
    // Calcula o salário bruto utilizando a função
    salario_bruto = calcular_salario_bruto(valor_hora, horas_trabalhadas);
    
    // Calcula o desconto utilizando a função
    desconto = calcular_desconto(salario_bruto);
    
    // Calcula o salário líquido utilizando a função
    salario_liquido = calcular_salario_liquido(salario_bruto, desconto);
    
    // Exibe os resultados
    printf("\n=== Relatorio de Salario ===\n");
    printf("Salario Bruto: R$ %.2f\n", salario_bruto);
    printf("Desconto (9%%): R$ %.2f\n", desconto);
    printf("Salario Liquido: R$ %.2f\n", salario_liquido);
    
    return 0;
}

