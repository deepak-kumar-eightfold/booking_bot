

from bookings import Booking
from bookings import SortChoice
from utils import JsonParser


def run_test(test: dict) -> dict:
    test_result = {
        'testId': test['testId'],
        'deals': [],
        'error': None
    }
    try:
        with Booking() as bot:
            test_result["deals"] = bot.fetch_hotel_deals(
                test["visitingCity"],
                test["checkInDate"],
                test["checkOutDate"],
                test["numberOfTravellers"],
                test["numberOfRooms"],
                SortChoice[test["sortBy"]],
                test["hotelStars"]
            )
    except Exception as e:
        test_result['error'] = str(e)

    return test_result


json_parser = JsonParser()
test_data = json_parser.read_json_from_file(
    input_file_path="./test_input/booking.com.json"
)['testInputs']

test_results = []

for test in test_data:
    test_results.append(run_test(test))


json_parser.write_json_to_file(
    output_file_path='./test_result/booking.com.json',
    output_data={"testResults": test_results}
)
