import sys
import string
from ft_filter import ft_filter


def word_filter(text: str, n_char: int):
    for i in text:
        if i in string.punctuation or not i.isprintable():
            raise AssertionError("the arguments are bad")
    split_text = text.split(" ")
    return (list(ft_filter(lambda x: len(x) > n_char, split_text)))


def main():
    argc = len(sys.argv)
    argv = sys.argv
    try:
        if argc != 3:
            raise AssertionError("the arguments are bad")
        try:
            char_counts = int(argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        print(word_filter(argv[1], char_counts))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
