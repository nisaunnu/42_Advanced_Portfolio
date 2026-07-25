import sys


def get_morse_table():
    """Return the character -> Morse code lookup table.

    Defined and returned by a function (instead of a module-level
    assignment) so that no global variable exists in this module.
    """
    return {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }


def encode(text):
    """Return the Morse code translation of `text`.

    Each character of `text` is looked up (case-insensitively) in
    the Morse table and its code is appended. Raises AssertionError
    if `text` contains a character that is not supported (i.e. not
    a letter, a digit or a space).
    """
    morse_table = get_morse_table()
    try:
        morse = "".join(morse_table[char.upper()] for char in text)
    except KeyError:
        raise AssertionError("the arguments are bad")
    return morse.rstrip()


def get_argument():
    """Validate and return the single command-line argument.

    Raises AssertionError if the number of arguments is not 1.
    """
    assert len(sys.argv) == 2, "the arguments are bad"
    return sys.argv[1]


def main():
    """Entry point: read the argument and print its Morse code."""
    try:
        text = get_argument()
        print(encode(text))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
