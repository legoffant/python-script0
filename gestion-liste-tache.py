taches = []

def ajouter_tache(tache):
    taches.append({"tache": tache, "terminee": False})

def marquer_terminee(index):
    if 0 <= index < len(taches):
        taches[index]["terminee"] = True
    else:
        print("Index invalide.")

def afficher_taches():
    for i, tache in enumerate(taches):
        etat = "Terminée" if tache["terminee"] else "En cours"
        print(f"{i + 1}. {tache['tache']} ({etat})")

# Exemple d'utilisation :
ajouter_tache("Faire les courses")
ajouter_tache("Réviser pour l'examen")
afficher_taches()
marquer_terminee(0)
afficher_taches()