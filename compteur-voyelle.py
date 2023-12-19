def compter_voyelles(chaine):
    voyelles = "aeiouAEIOU"
    return sum(1 for char in chaine if char in voyelles)

# Exemple d'utilisation :
mot = input("Entrez un mot : ")
nombre_voyelles = compter_voyelles(mot)
print(f"Le mot {mot} contient {nombre_voyelles} voyelles.")