def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

# Exemple d'utilisation :
nombre = int(input("Entrez un nombre : "))
resultat = factorielle(nombre)
print(f"La factorielle de {nombre} est {resultat}.")