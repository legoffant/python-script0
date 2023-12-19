import random

nombre_a_deviner = random.randint(1, 100)

while True:
    devine = int(input("Devinez le nombre entre 1 et 100 : "))
    if devine == nombre_a_deviner:
        print("Bravo, vous avez deviné le nombre !")
        break
    elif devine < nombre_a_deviner:
        print("Le nombre est plus grand. Essayez à nouveau.")
    else:
        print("Le nombre est plus petit. Essayez à nouveau.")