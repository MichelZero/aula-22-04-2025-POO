# 	Em linguagem Python, elabore um programa que leia 4 números 
# inteiros e armazene-os em uma lista L1. O programa deve ler 
# outros 6 números inteiros e armazená-los em uma lista L2. 
# A partir destas duas listas, crie uma terceira lista, L3,
# que deve armazenar os elementos da lista L2 e L1, mas na 
# ordem inversa. A lista L3 deve ser exibida em tela. 
# Observe o exemplo abaixo, considerando que os valores 
# que preenchem as listas L1 e L2 foram informados pelo usuário:

# L1 = [4,3,2,1]            L2 = [5,6,7,8,9,10]          L3 = [10,9,8,7,6,5,1,2,3,4]

# entrada de dados
L1 = [] # lista L1 vazia
L2 = [] # lista L2 vazia
L3 = [] # lista L3 vazia

for i in range(4):  
  L1.append(int(input("Insira um número inteiro")))
  
for i in range(6):
  L2.append(int(input("Insira um número inteiro")))
  
L3.extend(reversed(L2)) # adiciona os elementos de L2 na ordem inversa
# extend() adiciona os elementos de L2 na lista L3
L3.extend(reversed(L1))

print(f"Lista L1: {L1}") # imprime a lista L1
print(f"Lista L2: {L2}")
print(f"Lista L3: {L3}") # imprime a lista L3