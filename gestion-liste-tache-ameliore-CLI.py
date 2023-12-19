import argparse
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

def main():
    parser = argparse.ArgumentParser(description="Gestionnaire de tâches")
    parser.add_argument("--ajouter", help="Ajouter une nouvelle tâche", metavar="DESCRIPTION")
    parser.add_argument("--afficher", help="Afficher la liste des tâches", action="store_true")
    parser.add_argument("--terminer", help="Marquer une tâche comme terminée", type=int, metavar="NUMERO_TACHE")
    parser.add_argument("--afficher-termines", help="Afficher les tâches terminées", action="store_true")
    parser.add_argument("--trier-par-date", help="Trier les tâches par date d'échéance", action="store_true")

    args = parser.parse_args()

    gestionnaire = GestionnaireTaches()

    if args.ajouter:
        nouvelle_tache = Tache(args.ajouter)
        gestionnaire.ajouter_tache(nouvelle_tache)

    if args.afficher:
        print("### Liste des tâches ###")
        gestionnaire.afficher_taches()

    if args.terminer:
        if 1 <= args.terminer <= len(gestionnaire.taches):
            gestionnaire.taches[args.terminer - 1].marquer_terminee()
            print(f"Tâche {args.terminer} marquée comme terminée.")
        else:
            print("Numéro de tâche invalide.")

    if args.afficher_termines:
        print("### Liste des tâches terminées ###")
        gestionnaire.afficher_taches_terminees()

    if args.trier_par_date:
        gestionnaire.trier_taches_par_date()
        print("### Liste des tâches triées par date d'échéance ###")
        gestionnaire.afficher_taches()

if __name__ == "__main__":
    main()