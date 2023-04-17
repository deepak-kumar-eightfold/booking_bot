from datetime import datetime, timedelta


class DateValidator:
    def __init__(self) -> None:
        pass

    def is_valid_date_format(self, date: str) -> bool:
        """Checks if the date is in "YYYY-MM-DD" format. Returns True if it follows the format."""

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except Exception:
            return False

        return True

    def is_date_not_in_past(self, date: str) -> bool:
        """Checks if date is not in the past. Return False if date is in the past."""

        date = datetime.strptime(date, "%Y-%m-%d")

        return date >= datetime.today()

    def is_date_before_next_month_last_date(self, date: str) -> bool:
        """Checks if the date is less than or equal to the last date of next month counting from today's date (Not from the date itself). Returns False if date is after the next month's last date."""

        date = datetime.strptime(date, "%Y-%m-%d")

        today = datetime.now()
        next_month = today.replace(
            month=today.month + 2,
            day=1
        )
        last_date_of_next_month = next_month - timedelta(days=1)

        return date <= last_date_of_next_month

    def are_dates_equal(self, date1: str, date2: str) -> bool:
        """Checks if two dates are equal or not. Returns True if dates are equal."""

        date1 = datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.strptime(date2, "%Y-%m-%d")

        return date1 == date2
