def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date_str = input("Enter a date (MM/DD/YYYY or Month Day, Year): ")
        try:
            if "/" in date_str:
                month, day, year = map(int, date_str.split("/"))
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break
            else:
                parts = date_str.split()
                if len(parts) == 3:
                    month_str, day_str, year_str = parts
                    if month_str in months and day_str.endswith(','):
                        month = months.index(month_str) + 1
                        day_str_cleaned = day_str.rstrip(',')
                        if day_str_cleaned.isdigit():
                            day = int(day_str_cleaned)
                            year = int(year_str)
                            if 1 <= day <= 31:
                                print(f"{year:04}-{month:02}-{day:02}")
                                break
        except ValueError:
            pass
        except IndexError:
            pass


if __name__ == "__main__":
    main()
