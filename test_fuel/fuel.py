def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    if "/" not in fraction:
        raise ValueError("Invalid format: missing '/'")

    numerator, denominator = fraction.split("/")

    if not numerator.isdigit() or not denominator.isdigit():
        raise ValueError("Invalid numbers")

    num = int(numerator)
    den = int(denominator)

    if den == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if num > den:
        raise ValueError("Numerator cannot be greater than denominator")

    percentage = round((num / den) * 100)
    return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
