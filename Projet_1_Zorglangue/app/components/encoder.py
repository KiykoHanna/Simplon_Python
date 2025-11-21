def encode_text(text:str)->str:
    """
    Encode a text by reversing the letters in each word while preserving 
    the position of non-letter characters. Supports accented French letters.

    Args:
        text (str): The input string to be encoded. Must be of type str.

    Returns:
        str: The encoded string with letters in each word reversed 
             and non-letter characters in their original positions.

    Raises:
        TypeError: If `text` is not a string.
        RuntimeError: If an unexpected error occurs during encoding.
    
    Example:
        >>> encode_text("Bonjour, ça va très bien !")
        "ruojnoB, aç av sért neib !"
    """

    if not isinstance(text, str):
        raise TypeError("text must be str")
    
    try:
        result = []
        mot = []

        for lett in text:
            if lett.isalpha():
                mot.append(lett)
            else:
                result.append("".join(mot[::-1]))
                result.append(lett)
                mot = []
        result.append("".join(mot[::-1]))    

        return "".join(result)

    except Exception as e:
        raise RuntimeError(f"Erreur inattendue lors de l'encodage: {e}") from e