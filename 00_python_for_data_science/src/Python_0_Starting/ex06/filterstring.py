import sys


def get_arguments():
    """Validate and return the (string, integer) command-line pair.

    Raises AssertionError if the number of arguments is not 2, if
    the second argument is not a valid integer, or if any argument
    has an unexpected type.
    """
    assert len(sys.argv) == 3, "the arguments are bad"
    text = sys.argv[1]
    try:
        limit = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    return text, limit


def filter_words(text, limit):
    """Return the words of `text` longer than `limit` characters.

    Uses a list comprehension combined with a lambda predicate.
    """
    return [word for word in text.split(" ")
            if (lambda w: len(w) > limit)(word)]


def main():
    """Entry point: parse arguments and print the filtered words."""
    try:
        text, limit = get_arguments()
        print(filter_words(text, limit))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
