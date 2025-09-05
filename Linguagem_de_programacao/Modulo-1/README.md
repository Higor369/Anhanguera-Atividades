# Sistema de Gestão de Notas de Alunos

## Descrição
Sistema simples desenvolvido em Python para gerenciar notas de alunos, calcular médias e determinar a situação acadêmica (aprovado/reprovado).

## Funcionalidades
- ✅ Cadastro de notas dos alunos
- ✅ Cálculo automático da média
- ✅ Determinação da situação (aprovado/reprovado)
- ✅ Relatório final completo
- ✅ Interface amigável via console
- ✅ Validação de entrada de dados

## Como Executar

### Executar o Sistema Principal
```bash
python sistema_notas.py
```

### Executar os Testes
```bash
python teste_sistema.py
```

## Como Usar

1. Execute o programa principal
2. Escolha a opção "1" para cadastrar notas
3. Digite as notas do aluno (valores entre 0 e 10)
4. Digite "-1" para finalizar o cadastro
5. O sistema exibirá automaticamente:
   - Lista de notas inseridas
   - Média calculada
   - Situação do aluno (Aprovado/Reprovado)

## Critérios de Aprovação
- **Aprovado**: Média ≥ 7.0
- **Reprovado**: Média < 7.0

## Estrutura do Código

### Funções Principais
- `cadastrar_notas()`: Permite inserir notas do aluno
- `calcular_media(notas)`: Calcula a média das notas
- `determinar_situacao(media)`: Determina se o aluno foi aprovado ou reprovado
- `exibir_relatorio(notas, media, situacao)`: Exibe o relatório final
- `menu_principal()`: Controla o fluxo principal do programa

### Características Técnicas
- Utiliza estruturas condicionais (if/else)
- Implementa estruturas de repetição (while)
- Organizado em funções modulares
- Tratamento de erros e validação de entrada
- Interface interativa via console

## Exemplo de Uso

```
=== MENU PRINCIPAL ===
1. Cadastrar notas
2. Sair do sistema

Escolha uma opção: 1

=== CADASTRO DE NOTAS ===
Digite as notas do aluno (digite -1 para finalizar):
Digite uma nota (0 a 10): 8.5
Nota 8.5 adicionada com sucesso!
Digite uma nota (0 a 10): 7.0
Nota 7.0 adicionada com sucesso!
Digite uma nota (0 a 10): 9.2
Nota 9.2 adicionada com sucesso!
Digite uma nota (0 a 10): -1

==================================================
           RELATÓRIO FINAL
==================================================
Notas inseridas: [8.5, 7.0, 9.2]
Quantidade de notas: 3
Média: 8.23
Situação: Aprovado
🎉 Parabéns! Você foi aprovado!
==================================================
```

## Requisitos
- Python 3.6 ou superior
- Nenhuma dependência externa necessária
