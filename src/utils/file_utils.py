
import os
def get_filename():
    return input("Donnez le nom du fichier à chercher: ").strip()


def get_boolean_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in {"oui", "non"}:
            return response == "oui"
        else:
            print("Réponse non valide. Veuillez répondre par 'oui' ou 'non'.")


def get_directories():
    directories = []
    while True:
        path_to_discover = input("Donnez le chemin d'accès où chercher: ")
        if os.path.isdir(path_to_discover):
            directories.append(path_to_discover)
        else:
            print(f"Le chemin {path_to_discover} n'est pas valide.")

        end = input("Avez-vous terminé ? (oui/non): ").strip().lower()
        if end == "oui":
            break
    return directories
