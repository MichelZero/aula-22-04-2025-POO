# Escreva um programa que solicite uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e 
# continue pedindo até que o usuário informe um valor válido.

# entrada de dados

# iniciar um loop infinito
while True:
  # nota = int(input("digite uma nota entre 0 e 10: "))
  nota_str = input("digite uma nota entre 0 e 10: ")
  if nota_str.isdigit(): # verifica se o valor é um número inteiro positivo
    # nota_str.isdigit() verifica se o valor é um número inteiro positivo
    # pass
    nota = int(nota_str)
    if 0 <= nota <= 10:
      # pass
      print(f"Nota válida: {nota}")
      break
    else:
      print("Entrada inválida. Digite um valor entre 0 e 10.")
  else:
    print("Entrada inválida. Digite um número inteiro.")

# processamento


# saída de dados