import re  # Import the 're' module for regular expression handling
import sys  # Import the 'sys' module (not used in this code)


def convert(time_range: str) -> str:
    # Define a regex pattern to match a time range in the format 'hh[:mm] AM/PM to hh[:mm] AM/PM'
    pattern = r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)"

    # Search for a match in the provided string
    match = re.search(pattern, time_range)

    # If no match is found or if the input does not exactly match the pattern, raise an error
    if not match or match.group(0) != time_range:
        raise ValueError("Invalid format. Use 'hh[:mm] AM/PM to hh[:mm] AM/PM'.")

    # Extract the matched groups: start time and end time components
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # Convert hour values to integers
    start_hour, end_hour = int(start_hour), int(end_hour)

    # Convert minute values to integers, defaulting to 0 if not provided
    start_minute = int(start_minute) if start_minute else 0
    end_minute = int(end_minute) if end_minute else 0

    # Validate that minute values are within the valid range (0 to 59)
    if not (0 <= start_minute < 60 and 0 <= end_minute < 60):
        raise ValueError("Minutes must be between 0 and 59.")

    # Convert 12-hour format to 24-hour format
    start_hour_24 = (start_hour % 12) + (12 if start_period == "PM" else 0)
    end_hour_24 = (end_hour % 12) + (12 if end_period == "PM" else 0)

    # Return the formatted 24-hour time range
    return f"{start_hour_24:02}:{start_minute:02} to {end_hour_24:02}:{end_minute:02}"


def main():

    user_input = input("Enter time range (e.g., '9 AM to 5 PM'): ")
    print(convert(user_input))


# Ensure that the script runs only when executed directly, not imported as a module
if __name__ == "__main__":
    main()