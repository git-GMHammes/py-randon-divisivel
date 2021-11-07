# 
# Informar nºs aleatórios na Tela
# Informar nºs divisíveis:
# Por 5: Buzz
# Por 3: Fizz
# Por 3 e 5: FizzBuzz
# 
from random import randint


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz - Divisível por 3 e 5'
    elif n % 3 == 0:
        return 'Fizz - Divisével por 3'
    elif n % 5 == 0:
        return 'Buzz - Divisível por 5'
    else:
        return "Favor digitar um valor que seja divisível por 3 nem por 5"


for i in range(100):
    aleatorio = randint(0, 100)
    print(f"Valor: {aleatorio}, {fizzbuzz(aleatorio)}")
