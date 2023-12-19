mot = input("Entrez un mot : ")
if mot == mot[::-1]:
    print(f"{mot} est un palindrome.")
else:
    print(f"{mot} n'est pas un palindrome.")