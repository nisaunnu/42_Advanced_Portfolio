import time


def main():
    """Prints the time since January 1, 1970 in seconds
    and the date in the format "Mon dd yyyy"""

    my_time = time.time()
    my_date = time.strftime("%b %d %Y", time.localtime())

    print(
            f"Seconds since January 1, 1970: {my_time:,.4f} or "
            f"{my_time:.2e} in scientific notation"
        )
    print(my_date)


if __name__ == "__main__":
    main()
