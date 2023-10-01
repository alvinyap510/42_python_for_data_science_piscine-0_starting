import sys
import string


def count_characters(s):
    upper_letters = sum(1 for c in s if c.isupper())
    lower_letters = sum(1 for c in s if c.islower())
    punctuation_marks = sum(1 for c in s if c in string.punctuation)
    spaces = sum(1 for c in s if c.isspace())
    digits = sum(1 for c in s if c.isdigit())

    return {
        "upper_letters": upper_letters,
        "lower_letters": lower_letters,
        "punctuation_marks": punctuation_marks,
        "spaces": spaces,
        "digits": digits
    }


def main():
    if len(sys.argv) == 1:
        s = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        s = sys.argv[1]
    else:
        raise AssertionError("Expected only one argument")

    result = count_characters(s)
    print(f"The text contains {len(s)} characters:")
    print(f"{result['upper_letters']} upper letters")
    print(f"{result['lower_letters']} lower letters")
    print(f"{result['punctuation_marks']} punctuation marks")
    print(f"{result['spaces']} spaces")
    print(f"{result['digits']} digits")


if __name__ == "__main__":
    main()
