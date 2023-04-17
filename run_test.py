

from bookings import Booking
from utils import JsonParser
from validators import DateValidator, CountValidator


def perform_date_validations(date: str) -> None:
    date_validator = DateValidator()
    if not date_validator.is_valid_date_format(date):
        raise Exception("Invalid format! ")

    if not date_validator.is_date_not_in_past(date):
        raise Exception("Date can not be in past!")

    if not date_validator.is_date_before_next_month_last_date(date):
        raise Exception("Date can't be beyond next month!")


def are_dates_equal(date1: str, date2: str) -> None:
    date_validator = DateValidator()
    if date_validator.are_dates_equal(date1, date2):
        raise Exception("Check-in and Check-out dates cannot be the same.")


def verify_count(start: int, end: int, value: int) -> None:
    count_validator = CountValidator(start, end)
    if not count_validator.is_count_valid(value):
        raise Exception(f'value must be between {start} and {end}')


def perform_validations(test_obj: dict) -> None:
    perform_date_validations(test_obj["checkInDate"])
    perform_date_validations(test_obj["checkOutDate"])
    are_dates_equal(test_obj["checkInDate"], test_obj["checkOutDate"])
    verify_count(1, 30, test_obj["numberOfTravellers"])
    verify_count(1, 30, test_obj["numberOfRooms"])


def run_test(test: dict) -> dict:
    test_result = {
        'testId': test['testId'],
        'deals': [],
        'error': None
    }
    try:
        perform_validations(test)
        with Booking() as bot:
            test_result["deals"] = bot.fetch_hotel_deals(test)
    except Exception as e:
        test_result['error'] = str(e)

    return test_result


json_parser = JsonParser()
test_data = json_parser.read_json_from_file(
    input_file_path="./test_input/booking.com.json"
)['testInputs']

test_results = []

for test_obj in test_data:
    test_results.append(run_test(test_obj))


json_parser.write_json_to_file(
    output_file_path='./test_result/booking.com.json',
    output_data={"testResults": test_results}
)
