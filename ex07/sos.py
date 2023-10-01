import sys


def main():
    try:
        argc = len(sys.argv)
        if argc != 2:
            raise AssertionError("the arguments are bad")
        argv = sys.argv
        text = argv[1].upper()
        morse_text = ''
        NESTED_MORSE = {
            ' ': '\\ ',
            'A': '.- ',
            'B': '-... ',
            'C': '-.-. ',
            'D': '-.. ',
            'E': '. ',
            'F': '..-. ',
            'G': '--. ',
            'H': '.... ',
            'I': '.. ',
            'J': '.--- ',
            'K': '-.- ',
            'L': '.-.. ',
            'M': '-- ',
            'N': '-. ',
            'O': '--- ',
            'P': '.--. ',
            'Q': '--.- ',
            'R': '.-. ',
            'S': '... ',
            'T': '- ',
            'U': '..- ',
            'V': '...- ',
            'W': '.-- ',
            'X': '-..- ',
            'Y': '-.-- ',
            'Z': '--.. ',
            '1': '.---- ',
            '2': '..--- ',
            '3': '...-- ',
            '4': '....- ',
            '5': '..... ',
            '6': '-.... ',
            '7': '--... ',
            '8': '---.. ',
            '9': '----. ',
            '0': '----- ',
        }
        for char in text:
            if char not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
            morse_text += NESTED_MORSE[char]
        print(morse_text)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
