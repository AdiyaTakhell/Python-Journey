from fpdf import FPDF


def create_shirtificate(name):
    # Initialize PDF: A4, Portrait, millimeters
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # --- CS50 Shirtificate Header ---
    pdf.set_font('helvetica', 'B', 50)
    pdf.set_text_color(0, 0, 0)  # Black
    # Center header text horizontally at Y=20mm
    pdf.set_xy((pdf.w - pdf.get_string_width("CS50 Shirtificate")) / 2, 20)
    pdf.cell(0, 0, "CS50 Shirtificate")

    # --- Shirt Image Placement ---
    shirt_image_path = "shirtificate.png"
    shirt_width = 170  # Desired width of shirt on PDF (mm)
    shirt_height = 170  # Desired height of shirt on PDF (mm)
    shirt_x = (pdf.w - shirt_width) / 2  # Center shirt horizontally
    shirt_y = 65  # Y-position for the top of the shirt

    try:
        # Place the shirt image
        pdf.image(shirt_image_path, x=shirt_x, y=shirt_y, w=shirt_width, h=shirt_height)
    except RuntimeError:
        print(f"Error: Could not load '{shirt_image_path}'. Make sure it's in the same directory.")
        # If the image isn't found, we can't create the shirtificate correctly, so we stop here.
        return

        # --- Name on Shirt ---
    pdf.set_font('helvetica', 'B', 32)
    pdf.set_text_color(255, 255, 255)  # White text

    # Calculate name position to be centered on the shirt
    name_x_on_shirt = shirt_x + (shirt_width - pdf.get_string_width(name)) / 2
    name_y_on_shirt = shirt_y + (shirt_height / 2) - 10  # Adjust Y for vertical placement on shirt

    pdf.set_xy(name_x_on_shirt, name_y_on_shirt)
    pdf.cell(0, 0, name)

    # --- Output PDF ---
    pdf.output("shirtificate.pdf")
    print("PDF 'shirtificate.pdf' generated successfully!")


# --- Main execution block ---
if __name__ == "__main__":
    # Get the user's name using input()
    user_name = input("Enter your name: ")

    # Call the function with the provided name
    create_shirtificate(user_name)