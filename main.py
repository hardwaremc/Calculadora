def add(x,y):
  return x + y

def sub(x,y):
  return x - y

def mult(x,y):
  return x * y
  
def div(x,y):
  return x / y


print("Selecione uma operação.")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Escolha uma operação (1/2/3/4)")

if escolha in ('1','2','3','4'):
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))

    if escolha == '1':
      print(n1,"+",n2,"=",add(n1,n2))
      print(add(n1,n2))

    if escolha == '2':
      print(sub(n1,n2))

    if escolha == '3':
      print(mult(n1,n2))

    if escolha == '4':
      print(div(n1,n2))

