import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

# Fonction pour afficher la question actuelle et les choix
def afficher_question():
    # Obtenir la question actuelle à partir de la liste quiz_data
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Afficher les choix sur les boutons
    choix = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choix[i], state="normal")  # Réinitialiser l'état du bouton

    # Effacer l'étiquette de retour d'information et désactiver le bouton suivant
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Fonction pour vérifier la réponse sélectionnée et fournir un retour d'information
def verifier_reponse(choix):
    # Obtenir la question actuelle à partir de la liste quiz_data
    question = quiz_data[current_question]
    choix_selectionne = choice_btns[choix].cget("text")

    # Vérifier si le choix sélectionné correspond à la réponse correcte
    if choix_selectionne == question["answer"]:
        # Mettre à jour le score et l'afficher
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct !", foreground="green")
    else:
        feedback_label.config(text="Incorrect !", foreground="red")

    # Désactiver tous les boutons de choix et activer le bouton suivant
    for bouton in choice_btns:
        bouton.config(state="disabled")
    next_btn.config(state="normal")

# Fonction pour passer à la question suivante
def question_suivante():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        # S'il y a plus de questions, afficher la question suivante
        afficher_question()
    else:
        # Si toutes les questions ont été répondues, afficher le score final et terminer le quiz
        messagebox.showinfo("Quiz Terminé",
                            "Quiz Terminé ! Score final : {}/{}".format(score, len(quiz_data)))
        root.destroy()

# Créer la fenêtre principale
root = tk.Tk()
root.title("Application de Quiz")
root.geometry("600x500")
style = Style(theme="flatly")

# Configurer la taille de la police pour la question et les boutons de choix
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Créer l'étiquette de question
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

# Créer les boutons de choix
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: verifier_reponse(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Créer l'étiquette de retour d'information
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialiser le score
score = 0

# Créer l'étiquette de score
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Créer le bouton suivant
next_btn = ttk.Button(
    root,
    text="Suivant",
    command=question_suivante,
    state="disabled"
)
next_btn.pack(pady=10)

# Initialiser l'index de la question actuelle
current_question = 0

# Afficher la première question
afficher_question()

# Démarrer la boucle principale des événements
root.mainloop()





