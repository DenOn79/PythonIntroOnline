import random

for _ in range(15):
    print(round(random.random(), 3), end='  ')
print()

for _ in range(15):
    print(random.randint(10, 50), end='  ')
print()

for _ in range(15):
    print(random.randrange(10, 50, 2), end='  ')
print()

for _ in range(15):
    print(round(random.uniform(10, 50), 2), end='  ')
print()
