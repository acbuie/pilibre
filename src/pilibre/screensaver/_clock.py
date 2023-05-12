from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from rich.text import Text

from pilibre.screensaver.text.clock import construct_time
from pilibre.screensaver.text.colorize import construct_text


class Clock:
    def __init__(self, timezone: str) -> None:
        try:
            self.timezone = ZoneInfo(timezone)
        except ZoneInfoNotFoundError:
            # TODO: Log
            self.timezone = ZoneInfo("Ect/UTC")

        # Instantiate current local time
        self.update()

    def update(self) -> None:
        dt = datetime.now(self.timezone)

        self.date = dt.strftime("%A, %B %d")
        self.time = dt.strftime("%H:%M")

    @property
    def clock_title(self) -> Text:
        """Return the current date and time as `Text`.

        If `timezone` is not found in the IANA database
        (see: https://docs.python.org/3/library/zoneinfo.html and
        https://en.wikipedia.org/wiki/List_of_tz_database_time_zones),
        then UTM is used.

        Returns:
            Text: Formatted date and time.
        """
        clock_title = Text()

        clock_title.append(self.date, style="white")
        clock_title.append(" | ", style="white")
        clock_title.append(self.time, style="white")

        if not self.timezone:
            clock_title.append(" UTC", style="red")
            return clock_title

        return clock_title

    @property
    def date_title(self) -> Text:
        """Return the current date as `Text`.

        Returns:
            Text: Formatted date.
        """
        date_title = Text()
        date_title.append(self.date, style="white")

        return date_title

    def as_text(self) -> Text:
        """Return the clock as `Text`.

        Returns:
            Text: Formatted clock.
        """
        clock_chars = list(self.time)
        clock = construct_time(clock_chars)
        colored_clock = construct_text(clock)

        return colored_clock
