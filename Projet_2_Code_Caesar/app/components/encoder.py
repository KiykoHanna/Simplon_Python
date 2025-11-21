def encode_text(text:str, cle:int)->str:
    """
    Encode un texte en utilisant le code de César.

    Le code de César est un des plus simples algorithmes de cryptage :
    chaque lettre est décalée dans l'alphabet d'un nombre fixe de positions. 
    Les lettres majuscules et minuscules sont traitées séparément.
    Les caractères non alphabétiques restent inchangés.

    Args:
        text (str): Le texte à encoder.
        cle (int): La clé de décalage (nombre entier de positions à décaler).

    Returns:
        str: Le texte encodé avec le décalage appliqué.


     Raises:
        TypeError: Si `text` n'est pas une chaîne de caractères.
        TypeError: Si `cle` n'est pas une nombre entier.
        RuntimeError: Si une erreur inattendue se produit pendant l'encodage.

    Exemple:
        >>> encoder("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3)
        'DEFGHIJKLMNOPQRSTUVWXYZABC'
        >>> encoder("abcdefghijklmnopqrstuvwxyz", 3)
        'defghijklmnopqrstuvwxyzabc'
        >>> encoder("Bonjour!", 2)
        'Dqplrwqt!'
    """

    if isinstance(text, str):
        raise TypeError("Text must be str")

    if isinstance(cle, int):
        raise TypeError("Cle must be int")
    
    try:
        result = ""
        for lett in text:
            if 65 <= ord(lett) <= 90:
                new_lett = chr(ord(lett) + cle) if (ord(lett) + cle) <=90 else chr(ord(lett) + cle - 26) 
                result += new_lett
            elif 97 <= ord(lett) <= 122:
                new_lett = chr(ord(lett) + cle) if (ord(lett) + cle) <=122 else chr(ord(lett) + cle - 26)
                result += new_lett
            else:
                result += lett
        return result 
    
    except Exception as e:
        raise RuntimeError(f"Erreur inattendue lors de l'encodage: {e}") from e