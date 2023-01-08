from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from rich.text import Text


def format_datetime_title(timezone: str) -> Text:
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
