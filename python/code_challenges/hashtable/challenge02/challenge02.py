def first_repeated_word(s):
    """
    Find the first repeated word in a string.

    Args:
        s (str): The input string.

    Returns:
        str: The first repeated word, or 'No Repetition' if no word is repeated.

    Example Usage:
        >>> first_repeated_word("ASAC is a department at LTUC. ASAC teaches programming in LTUC.")
        'ASAC'
        >>> first_repeated_word("I am learning programming at ASAC.")
        'No Repetition'
    """
    words = s.split()
    seen = set()

    for word in words:
        word = word.strip('.,!?').lower()
        if word in seen:
            return word
        seen.add(word)

    return "No Repetition"
