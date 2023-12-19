def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Exemple d'utilisation :
nombre = int(input("Entrez un nombre : "))
if est_premier(nombre):
    print(f"{nombre} est un nombre premier.")
else:
    print(f"{nombre} n'est pas un nombre premier.")