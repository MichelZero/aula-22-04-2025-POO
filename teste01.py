

valor_str = input("informe um número: ")
if valor_str.isdigit():
  print(f"número positivo -> {valor_str}")
elif valor_str.startswith('-'):
  print(f"número negativo -> {valor_str}")