import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) == 3:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        valid_extensions = (".jpg", ".jpeg", ".png")

        # Extract and normalize extensions
        input_extension = os.path.splitext(input_filename)[1].lower()
        output_extension = os.path.splitext(output_filename)[1].lower()

        # Validate extensions
        if input_extension not in valid_extensions:
            sys.exit("Invalid input")
        if output_extension not in valid_extensions:
            sys.exit("Invalid output")
        if input_extension != output_extension:
            sys.exit("Input and Output have different extension")

        # Process image after validation
        process_image(input_filename, output_filename)

    elif len(sys.argv) < 3:
        sys.exit("Too few command line argument")
    else:
        sys.exit("Too many command line argument")

def process_image(input_file, output_file):
    try:
        shirt = Image.open("shirt.png")
        input_image = Image.open(input_file)

        # Resize and crop input to match shirt size
        size = shirt.size
        input_cropped = ImageOps.fit(input_image, size)

        # Paste shirt on input image using shirt's alpha channel as mask
        input_cropped.paste(shirt, (0, 0), shirt)

        # Save the result
        input_cropped.save(output_file)

    except FileNotFoundError:
        sys.exit("File not found.")

if __name__ == "__main__":
    main()
