import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    args = sys.argv[1:]

    if not args:
        font = random.choice(fonts)
   
    elif len(args) == 2 and args[0] in ("-f", "--font"):
        font = args[1]
        if font not in fonts:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")

    text = input("Input: ")
    figlet.setFont(font=font)
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
