import os


def ft_tqdm(lst):
    """Yield the elements of `lst` one by one.

    While the caller iterates, a tqdm-like progress bar (percentage,
    ASCII bar and n/total counter) is printed to stdout and updated
    in place after every element.
    """
    total = len(lst)
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80
    for index, item in enumerate(lst, start=1):
        percent = index * 100 // total
        prefix = f"{percent}%|["
        suffix = f"]| {index}/{total}"
        bar_width = max(columns - len(prefix) - len(suffix) - 1, 2)
        filled = (bar_width - 1) * index // total
        bar = "=" * filled + ">" + " " * (bar_width - 1 - filled)
        print(f"\r{prefix}{bar}{suffix}", end="", flush=True)
        yield item
    print()


def main():
    """Entry point. Running this module alone does nothing."""


if __name__ == "__main__":
    main()
