# numbers.py

# fisrt.py não faz nada além de gerar números aleatórios
# Arquivo que será infectado
import random

random.seed()

for _ in range(10):
    print(random.randint(0, 100))
