"""
Script de teste para demonstrar o funcionamento do sistema de notas
"""

from sistema_notas import calcular_media, determinar_situacao, exibir_relatorio

def testar_sistema():
    """
    Função para testar diferentes cenários do sistema
    """
    print("=== TESTE DO SISTEMA DE NOTAS ===\n")
    
    # Teste 1: Aluno aprovado
    print("TESTE 1: Aluno Aprovado")
    notas_aprovado = [8.5, 7.0, 9.2, 6.8]
    media_aprovado = calcular_media(notas_aprovado)
    situacao_aprovado = determinar_situacao(media_aprovado)
    exibir_relatorio(notas_aprovado, media_aprovado, situacao_aprovado)
    
    print("\n" + "-"*50 + "\n")
    
    # Teste 2: Aluno reprovado
    print("TESTE 2: Aluno Reprovado")
    notas_reprovado = [5.0, 4.5, 6.0, 3.8]
    media_reprovado = calcular_media(notas_reprovado)
    situacao_reprovado = determinar_situacao(media_reprovado)
    exibir_relatorio(notas_reprovado, media_reprovado, situacao_reprovado)
    
    print("\n" + "-"*50 + "\n")
    
    # Teste 3: Aluno com média exata 7.0
    print("TESTE 3: Aluno com Média Exata 7.0")
    notas_exato = [7.0, 7.0, 7.0, 7.0]
    media_exato = calcular_media(notas_exato)
    situacao_exato = determinar_situacao(media_exato)
    exibir_relatorio(notas_exato, media_exato, situacao_exato)
    
    print("\n" + "-"*50 + "\n")
    
    # Teste 4: Aluno com apenas uma nota
    print("TESTE 4: Aluno com Uma Nota")
    notas_uma = [8.0]
    media_uma = calcular_media(notas_uma)
    situacao_uma = determinar_situacao(media_uma)
    exibir_relatorio(notas_uma, media_uma, situacao_uma)

if __name__ == "__main__":
    testar_sistema()
