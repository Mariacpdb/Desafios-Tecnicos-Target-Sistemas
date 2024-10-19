def verificacao_a(string):
  
    string_lower = string.lower()
    
    contagem = string_lower.count('a')
    
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")

texto = input("Digite uma string: ")


verificacao_a(texto)
