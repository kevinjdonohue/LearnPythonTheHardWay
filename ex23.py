"""Exercise 23."""

import sys

# pylint: disable=unbalanced-tuple-unpacking
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    """Main."""
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

    raise Exception()


def print_line(line, encoding, errors):
    """Print Line."""
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(f"{raw_bytes} <==> {cooked_string}")


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
