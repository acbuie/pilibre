from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from rich.text import Text


def format_datetime_title(timezone: str) -> Text:
    """Format the simple clock title.

    If `timezone` is not found in the IANA database
    (see: https://docs.python.org/3/library/zoneinfo.html and
    https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), the
    function returns 'Invalid timezone' as `Text`.

    Args:
        timezone (str): Local timezone.

    Returns:
        Text: Formatted date and local time.
    """
    try:
        tz = ZoneInfo(timezone)
    except ZoneInfoNotFoundError:
        clock = Text()
        clock.append("Invalid timezone.", style="red")
        return clock

    dt = datetime.now(tz)

    time = dt.strftime("%H:%M")
    date = dt.strftime("%A, %B %d | ")

    clock = Text()
    clock.append(date, style="white")
    clock.append(time, style="white")

    return clock
