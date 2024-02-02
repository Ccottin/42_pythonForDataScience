
# this part is about filling the terminal as tsdm does but uses
# forbidden functions
# import os

# def better_fit():
#    columns,rows = os.get_terminal_size(0)
#    return (columns - 41)


def ft_tqdm(lst: range) -> None:
    """this function reproduces tqdm(). It displays a loading bar.
    from Stackoverflow = Range objects carry no iteration state.
    There's a common misconception that range returns a generator,
    but range objects are lazy, immutable sequences, not generators.
    You can't determine the state of an iteration over a range by
    looking at the range."""

    upper_range = max(lst) + 1
    # max_pgr_bar = better_fit()
    max_pgr_bar = 100
    for count in lst:
        ratio = int(count * 100 / upper_range)
        progress_bar = ""
        bar_ratio = ratio / 100 * max_pgr_bar
        i = 0
        while (i <= bar_ratio + 1):
            progress_bar = progress_bar + "█"
            i = i + 1
        while (i > bar_ratio and i < max_pgr_bar):
            progress_bar = progress_bar + " "
            i = i + 1
        print(str(ratio + 1) + "%|" + progress_bar + "|", str(count + 1)
              + "/" + str(upper_range), end="\r")
        yield (count)

    print(str(ratio + 1) + "%|" + progress_bar + "|", str(count + 1)
          + "/" + str(upper_range), end="\r")
