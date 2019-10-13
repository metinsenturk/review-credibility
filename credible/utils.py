import sys
import json


def check_json(filepath):
    """
    Validates if the file is json or not.
    """
    with open(filepath, 'rb') as stream:
        try:
            json.load(stream)
            return True
        except json.JSONDecodeError:
            return False


def convert_file_to_json(read_filepath, write_filepath):
    """
    Converts yelp raw data files into full valid json files.
    """
    # params
    lines = []

    # read file
    with open(read_filepath, 'r', encoding="utf8") as stream:
        for line in stream:
            lines.append(json.loads(line))

    # write file
    with open(write_filepath, 'w+', encoding="utf8") as stream:
        json.dump(lines, stream)

    print('success! length : {}.'.format(len(lines)))


def progressbar(it, prefix="", size=60, file=sys.stdout):
    """
    Progress bar function for long processes.

    it      : iterator
    prefix  : custom string to add on progress bar.
    size    : size of the progress bar
    file    : where the progress bar runs.

    For more information, check the original answer from
    stackoverflow, https://stackoverflow.com/a/34482761.
    """
    count = len(it)

    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" %
                   (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()


def progressbar2(total, progress, prefix=""):
    """
    Displays or updates a console progress bar.

    Original source: https://stackoverflow.com/a/15860757/1391441
    """
    barLength, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r{} [{}] {:.0f}% {}".format(
        prefix, "#" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()
