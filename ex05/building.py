import sys
import string


def count_text(text: str):
    letters = 0
    upper_letters = 0
    lower_letters = 0
    punctuation_marks = 0
    spaces = 0
    digits = 0
    i = 0
    while (i < len(text)):
        if (text[i] != '\n'):
            letters += 1
        if text[i].isupper():
            upper_letters += 1
        elif text[i].islower():
            lower_letters += 1
        elif text[i] in string.punctuation:
            punctuation_marks += 1
        elif text[i].isspace():
            spaces += 1
        elif text[i].isdigit():
            digits += 1
        i += 1
    print(f"""The text contain {letters} characters:
{upper_letters} upper letters
{lower_letters} lower letters
{punctuation_marks} punctuation marks
{spaces} spaces
{digits} digits""")


def main():
    try:
        argc = len(sys.argv)
        if (argc > 2):
            raise AssertionError("more than one argument is provided")
        if (argc == 1):
            # text = input("What is the text to count?\n")
            # print("What is the text to count?")
            # text = sys.stdin.read()
            try:
                print("What is the text to count?")
                text = sys.stdin.readline()
                # text = input("What is the text to count?\n")
            except KeyboardInterrupt:
                return
        else:
            text = sys.argv[1]
        count_text(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
