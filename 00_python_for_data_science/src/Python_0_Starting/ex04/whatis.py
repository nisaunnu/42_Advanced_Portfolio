import sys


def main():
    argv_len = len(sys.argv)

    if argv_len == 1:
        return

    try:
        if argv_len > 2:
            raise AssertionError("more than one argument is provided")

        try:
            num = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
