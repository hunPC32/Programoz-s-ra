import random

health = 2000
enemy_health = 2000
strenght = int(input("Erő, 1-25: "))
enemy_strenght = random.randint(1, 25)

for i in range(20):
    dmg = random.randint(1, 20) * strenght
    enemy_health -= dmg
    print(f"A sebzés: {dmg}, Az ellenfél életereje: {enemy_health}")
    enemy_dmg = random.randint(1, 20) * enemy_strenght
    health -= enemy_dmg
    print(f"Az ellenfél sebzése: {enemy_dmg}, Az életerőd: {health}")
    
    if health <= 0:
        print("Vesztettél")
        break
    if enemy_health <= 0:
        print("Nyertél")

print(f"Az ellenfél életereje: {enemy_health}")
print(f"Az életerőd: {health}")