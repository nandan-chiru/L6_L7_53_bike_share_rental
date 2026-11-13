def parse_ride_duration(text):
    """
    Converts a ride duration written as HH:MM into minutes.
    Returns 0 for invalid input.
    """
    try:
        if not isinstance(text, str):
            return 0

        parts = text.strip().split(':')

        if len(parts) != 2:
            return 0

        hours, minutes = parts

        if not hours.isdigit() or not minutes.isdigit():
            return 0

        return int(hours) * 60 + int(minutes)

    except (ValueError, TypeError, AttributeError):
        return 0


def format_station_code(code):
    """
    Formats a station code as ZONE-NUMBER, e.g. 'a12' -> 'A-12'.
    Returns an empty string for invalid input.
    """
    try:
        if not isinstance(code, str):
            return ""

        code = code.strip().upper()

        if not code:
            return ""

        return code[0] + '-' + code[1:]

    except (ValueError, TypeError, AttributeError, IndexError):
        return ""


def parse_ride_log(line):
    """
    Parses 'bike_type,minutes,subscriber' into a tuple.
    Returns a safe default tuple for invalid input.
    """
    try:
        if not isinstance(line, str):
            return "", 0, False

        parts = line.split(',')

        if len(parts) != 3:
            return "", 0, False

        bike_type = parts[0].strip()

        try:
            minutes = int(parts[1].strip())
        except (ValueError, TypeError):
            minutes = 0

        subscriber = parts[2].strip().lower() == 'yes'

        return bike_type, minutes, subscriber

    except (ValueError, TypeError, AttributeError, IndexError):
        return "", 0, False


def main():
    print("==== Running parse_ride_duration ====")
    value = input("Enter a ride duration as HH:MM (e.g. 01:15): ")
    print("Duration in minutes:", parse_ride_duration(value))

    print("\n==== Running format_station_code ====")
    value = input("Enter a station code (e.g. a12): ")
    print("Formatted station code:", format_station_code(value))

    print("\n==== Running parse_ride_log ====")
    value = input("Enter a ride log line as type,minutes,subscriber (e.g. electric,45,yes): ")
    print("Parsed ride log:", parse_ride_log(value))


if __name__ == "__main__":
    main()