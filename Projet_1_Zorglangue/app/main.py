import logging

from components import encode_text
from components import decode_text


logging.basicConfig(
    filename='app.log',      # fichier pour l'enregistrement
    filemode='w',             # w = écraser le fichier, a = ajouter
    level=logging.INFO,       # niveau minimum de journalisation
    format='%(asctime)s - %(levelname)s - %(message)s'  # format
)

logging.info("Programme démarré")
logging.warning("Un avertissement est survenu")
logging.error("Une erreur est survenue")

def main():
    """
    Main function to run the text encoding.
    """

    print("Choisissez l'action : encoder (u) / décoder (d)")
    act = input().lower()

    print("Saissez le text")
    text = input()

    # Appel de la fonction d'encodage ou de decodage
    match act:
        case "u":
            new_text = encode_text(text)
        case"d":
            new_text = decode_text(text)
        case _:
            raise ValueError("Action inconnue : choisissez 'u' ou 'd'.")



    # Affichage du résultat
    print("Original:", text)
    print("Result :", new_text)


if __name__ == "__main__":
    main()