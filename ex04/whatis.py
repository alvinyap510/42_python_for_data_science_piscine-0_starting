import sys


def main():
    try:
        argc = len(sys.argv)
        if (argc != 2):
            if argc < 2:
                return
            else:
                raise AssertionError("more than one argument is provided")
        arg = sys.argv[1]
        try:
            num = int(arg)
            if num % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            raise AssertionError("argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Don't interupt me !!")


if __name__ == "__main__":
    main()
