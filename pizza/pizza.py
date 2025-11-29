import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if filename.endswith(".csv"):
            data = check()
            header = data[0]
            rows = data[1:]
            print(tabulate(rows, headers=header, tablefmt="grid"))

        else:
            sys.exit("Not a CSV File")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    else:
        sys.exit("Too few command line arguments")

def check():
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == '__main__':
    main()
