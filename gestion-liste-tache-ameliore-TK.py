import tkinter as tk
from tkinter import messagebox
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
        return self.taches

    def afficher_taches_terminees(self):
        return [tache for tache in self.taches if tache.terminee]

    def trier_taches_par_date(self):
        self.taches.sort(key=lambda tache: tache.date_echeance)

class GestionnaireTachesApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestionnaire de Tâches")

        self.gestionnaire = GestionnaireTaches()

        self.label_taches = tk.Label(master, text="Liste des Tâches")
        self.label_taches.pack()

        self.listbox_taches = tk.Listbox(master, selectmode=tk.SINGLE)
        self.listbox_taches.pack()

        self.button_ajouter = tk.Button(master, text="Ajouter une Tâche", command=self.ajouter_tache)
        self.button_ajouter.pack()

        self.button_marquer_terminee = tk.Button(master, text="Marquer comme Terminée", command=self.marquer_terminee)
        self.button_marquer_terminee.pack()

        self.button_afficher_termines = tk.Button(master, text="Afficher les Tâches Terminées", command=self.afficher_termines)
        self.button_afficher_termines.pack()

        self.button_trier_par_date = tk.Button(master, text="Trier par Date d'Échéance", command=self.trier_par_date)
        self.button_trier_par_date.pack()

        self.afficher_taches()

    def afficher_taches(self):
        self.listbox_taches.delete(0, tk.END)
        for tache in self.gestionnaire.afficher_taches():
            self.listbox_taches.insert(tk.END, str(tache))

    def ajouter_tache(self):
        dialogue = AjouterTacheDialog(self.master)
        self.master.wait_window(dialogue.top)
        nouvelle_tache = dialogue.result
        if nouvelle_tache:
            self.gestionnaire.ajouter_tache(nouvelle_tache)
            self.afficher_taches()

    def marquer_terminee(self):
        selection = self.listbox_taches.curselection()
        if selection:
            index = selection[0]
            self.gestionnaire.afficher_taches()[index].marquer_terminee()
            self.afficher_taches()

    def afficher_termines(self):
        taches_terminees = self.gestionnaire.afficher_taches_terminees()
        if taches_terminees:
            messagebox.showinfo("Tâches Terminées", "\n".join(map(str, taches_terminees)))
        else:
            messagebox.showinfo("Tâches Terminées", "Aucune tâche terminée.")

    def trier_par_date(self):
        self.gestionnaire.trier_taches_par_date()
        self.afficher_taches()

class AjouterTacheDialog:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Ajouter une Tâche")

        self.label_description = tk.Label(self.top, text="Description de la Tâche:")
        self.label_description.pack()

        self.entry_description = tk.Entry(self.top)
        self.entry_description.pack()

        self.label_date = tk.Label(self.top, text="Date d'Échéance (YYYY-MM-DD):")
        self.label_date.pack()

        self.entry_date = tk.Entry(self.top)
        self.entry_date.pack()

        self.button_ok = tk.Button(self.top, text="OK", command=self.ok)
        self.button_ok.pack()

        self.result = None

    def ok(self):
        description = self.entry_description.get()
        date_str = self.entry_date.get()
        date_echeance = datetime.strptime(date_str, '%Y-%m-%d') if date_str else None
        self.result = Tache(description, date_echeance)
        self.top.destroy()

def main():
    root = tk.Tk()
    app = GestionnaireTachesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()