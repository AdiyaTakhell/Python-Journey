import re
import sys

def convert(time_range: str) -> str:
    pattern = r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)"
    match = re.search(pattern, time_range)
    if not match or match.group(0) != time_range:
        raise ValueError("Invalid format. Use 'hh[:mm] AM/PM to hh[:mm] AM/PM'.")
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()
    start_hour, end_hour = int(start_hour), int(end_hour)
    start_minute = int(start_minute) if start_minute else 0
    end_minute = int(end_minute) if end_minute else 0
    if not (0 <= start_minute < 60 and 0 <= end_minute < 60):
        raise ValueError("Minutes must be between 0 and 59.")
    start_hour_24 = (start_hour % 12) + (12 if start_period == "PM" else 0)
    end_hour_24 = (end_hour % 12) + (12 if end_period == "PM" else 0)
    return f"{start_hour_24:02}:{start_minute:02} to {end_hour_24:02}:{end_minute:02}"

def main():
    try:
        user_input = input("Enter time range (e.g., '9 AM to 5 PM'): ")
        print(convert(user_input))
    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()