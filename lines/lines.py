import sys

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if filename.endswith(".py"):
            result = check()
            print(result)
        else:
            sys.exit("Not a Python File")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    else:
        sys.exit("Too few command line arguments")

def check():
    try:
        with open(sys.argv[1], "r") as file:
            count = 0
            for line in file:
                stripped = line.lstrip()

                if stripped and not stripped.startswith('#'):
                    count += 1
            return f"Total non-empty, non-comment lines: {count}"
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == '__main__':
    main()
