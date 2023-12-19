from datetime import datetime, timedelta

class Tache:
    def __init__(self, description, date_echeance=None):
        self.description = description
        self.date_echeance = date_echeance
        self.terminee = False

    def marquer_terminee(self):
        self.terminee = True

    def __str__(self):
        statut = "Terminée" if self.terminee else "En cours"
        date_str = f" (échéance le {self.date_echeance.strftime('%Y-%m-%d')})" if self.date_echeance else ""
        return f"{self.description} ({statut}{date_str})"

class GestionnaireTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def afficher_taches(self):
        if not self.taches:
            print("Aucune tâche à afficher.")
        else:
            for i, tache in enumerate(self.taches, start=1):
                print(f"{i}. {tache}")

    def afficher_taches_terminees(self):
        taches_terminees = [tache for tache in self.taches if tache.terminee]
        if not taches_terminees:
            print("Aucune tâche terminée à afficher.")
        else:
            for i, tache in enumerate(taches_terminees, start=1):
                print(f"{i}. {tache}")

    def trier_taches_par_date(self):
        self.taches.sort(key=lambda tache: tache.date_echeance)

# Exemple d'utilisation :
gestionnaire = GestionnaireTaches()

tache1 = Tache("Faire les courses", datetime.now() + timedelta(days=2))
tache2 = Tache("Réviser pour l'examen", datetime.now() + timedelta(days=5))
tache3 = Tache("Apprendre Python")

gestionnaire.ajouter_tache(tache1)
gestionnaire.ajouter_tache(tache2)
gestionnaire.ajouter_tache(tache3)

print("### Liste initiale de tâches ###")
gestionnaire.afficher_taches()

print("\n### Liste de tâches triée par date d'échéance ###")
gestionnaire.trier_taches_par_date()
gestionnaire.afficher_taches()

print("\n### Marquer la première tâche comme terminée ###")
tache1.marquer_terminee()
gestionnaire.afficher_taches_terminees()