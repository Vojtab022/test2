import random

def random_pole(delka):
    return [random.randint(1, 100) for _ in range(delka)]

Správně = 0
Špatně = 0

for _ in range(random.randint(1, 15)):
    delka = random.randint(1, 10)
    pole = random_pole(delka)
    print("Generované pole:", pole)
    
    delka2 = int(input("Zadej délku pole (1-10): "))

    if delka == delka2:
        print("Správně")
        Správně += 1
    else:
        print("Špatně")
        Špatně += 1

print("Počet správných odpovědí:", Správně)
print("Počet nesprávných odpovědí:", Špatně)