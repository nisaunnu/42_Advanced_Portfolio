import sys
import string


def count_characters(text):
    """Counts the character categories in `text`.

    Returns a tuple containing the counts of uppercase letters,
    lowercase letters, punctuation marks, spaces, and digits
    in that order."""

    up_letter = 0
    low_letter = 0
    punc = 0
    spaces = 0
    digits = 0

    for char in text:
        if char.isupper():
            up_letter += 1
        elif char.islower():
            low_letter += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        elif char in string.punctuation:
            punc += 1
    return up_letter, low_letter, punc, spaces, digits


def display_counts(text):
    """Print: text length and number of characters in each category"""

    up_letter, low_letter, punc, spaces, digits = count_characters(text)

    print(f"The text contains {len(text)} characters:")
    print(f"{up_letter} upper letters")
    print(f"{low_letter} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def get_text():
    """Return: text from command line or stdin

    Uses the single command-line argument if one was given, otherwise
    prompts the user and reads a line from standard input.
    Raises AssertionError if more than one argument was given.
    """

    assert len(sys.argv) <= 2, "there is more than one argument"

    if len(sys.argv) == 2:
        return sys.argv[1]

    print("What is the text to count?")
    return sys.stdin.readline()


def main():
    """Entry point: gets the text, validates it, and displays the counts."""

    try:
        text = get_text()
        display_counts(text)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
