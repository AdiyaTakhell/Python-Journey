from datetime import date
import inflect
import sys

def main():
    dob_input = input("Date of Birth: ").strip()
    try:
        dob = date.fromisoformat(dob_input)
    except ValueError:
        sys.exit("Invalid date")

    minutes = calculate_minutes(dob)
    print(convert_to_words(minutes))

def calculate_minutes(birth_date):
    today = date.today()
    delta = today - birth_date
    return delta.days * 24 * 60

def convert_to_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()
    return f"{words} minutes"

if __name__ == "__main__":
    main()
