import logging

from components import encode_text
from components import decode_text

logging.basicConfig(
    filename='app.log',      # fichier pour l'enregistrement
    filemode='w',
    level=logging.INFO
    format='%(asctime)s - %(levelname)s - %(message)s'  # format
)

logging.info("Programme démarré")
logging.warning("Un avertissement est survenu")
logging.error("Une erreur est survenue")

def main():
    """
    Main function to run the text encoding.
    """

    

if __name__ == "__main__":
    main()