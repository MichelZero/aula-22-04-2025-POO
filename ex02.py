# 2
# Escreva um programa em Python que leia vários valores 
# inteiros (positivos ou negativos), até que seja informado 
# o valor 0 ( ZERO) , encontra o maior e o menor deles 
# e mostra o resultado.

# Entrada de dados
maior = float('-inf') # inicializa maior com o menor valor possível 
#maior = -1000
menor = float('inf') # inicializa menor com o maior valor possível 
#menor = 1000

# loop infinito
# processamento
while True:
  valor_str = input("informe um valor inteiro (ZERO para sair):") 
  if valor_str.isdigit() or valor_str.startswith('-'): 
    # verifica se o valor é um número inteiro positivo ou negativo
    # valor_str.isdigit() verifica se o valor é um número inteiro positivo
    # valor_str.startswith('-') verifica se o valor é um número inteiro negativo
    # atenção, estamos usando o método startswith() para verificar se o valor começa com '-'
    # e não o método isdigit(), pois o método isdigit() não aceita números negativos
    #pass
    valor = int(valor_str)
    if valor == 0:
      break
    if valor > maior:
      maior = valor
    if valor < menor:
      menor = valor
  else:
    print("Entrada inválida. Digite um número inteiro.")
    

# saída de dados
if maior == float("-inf"): # verifica se o maior valor foi atualizado
  # se o maior valor não foi atualizado, significa que nenhum valor foi informado
  print("Nenhum valor foi informado.")
else:
  print(f"Maior valor: {maior}") 
  print(f"Menor valor: {menor}")
  
