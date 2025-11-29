def main():
    result = indicator()
    print(result)

def indicator():
    while True:
        try:
            fraction = input("Fraction : ").strip()


            if "/" not in fraction:
                continue

            numerator, denominator = fraction.split("/")


            if not numerator.isdigit() or not denominator.isdigit():
                continue

            num = int(numerator)
            den = int(denominator)


            if den == 0 or num > den:
                continue


            percentage = round((num / den) * 100)

            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{percentage}%"

        except (ValueError, ZeroDivisionError):
            continue

if __name__ == '__main__':
    main()
