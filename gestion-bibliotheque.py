class Livre:
    def __init__(self, titre, auteur, date_publication):
        self.titre = titre
        self.auteur = auteur
        self.date_publication = date_publication

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def supprimer_livre(self, livre):
        self.livres.remove(livre)

    def afficher_livres(self):
        for livre in self.livres:
            print(f"{livre.titre} par {livre.auteur}, publié en {livre.date_publication}")

# Exemple d'utilisation :
biblio = Bibliotheque()
livre1 = Livre("Harry Potter", "J.K. Rowling", 1997)
livre2 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954)

biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)
biblio.afficher_livres()