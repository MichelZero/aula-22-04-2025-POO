# 3. Média dos valores ímpares
# Em linguagem Python, Escreva um programa leia vários valores inteiros (positivos ou negativos), 
# até que seja informado o valor 0 ( ZERO) , calcule média dos valores impares informados.


# entrada de dados
# soma dos valores ímpares
soma_impares = 0
contagem_impares = 0

# processamento
# inicializa o loop infinito
while True:
    valor_str = input("Digite um valor inteiro (0 para sair): ")
     # o isdigit() verifica se a string é um número inteiro (positivo ou negativo)
     # o startwith() verifica se a string começa com o que está entre aspas, ou seja, se a string começa com o sinal de menos.
    if valor_str.isdigit() or valor_str.startswith('-'): 
      # pass # o pass é um comando que não faz nada, ou seja, ele é um comando vazio.
        valor = int(valor_str)
        if valor == 0:
            break
        if valor % 2 != 0:  # Verifica se o valor é ímpar
            soma_impares += valor
            contagem_impares += 1
    else:
        print("Entrada inválida. Digite um número inteiro.")

if contagem_impares == 0:
    print("Nenhum valor ímpar foi digitado.")
else:
    media = soma_impares / contagem_impares
    print("Média dos valores ímpares:", media)
    
def faz_algo():
    pass  # Aqui você pode adicionar o que quiser fazer com a função faz_algo()