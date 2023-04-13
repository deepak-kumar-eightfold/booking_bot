from prettytable import PrettyTable

from bookings import Booking
from bookings import SortChoice


sort_by_input_string = """
    Sorting choices:

    1. POPULARITY
    2. HOME_AND_APARTMENT_FIRST
    3. LOWEST_PRICE
    4. BEST_REVIEW_AND_LOWEST_PRICE
    5. RATING_HIGH_TO_LOW
    6. RATING_LOW_TO_HIGH
    7. RATING_AND_PRICE
    8. DISTANCE_FROM_CITY_CENTRE
    9. TOP_REVIEWED

    Select your sort choice: """

filter_star_input_string = """
    Filter by Hotel stars:

    Examples:
        3 --> This will show three star hotels 
        3 4 5 --> This will show 3, 4 and 5 star hotels 
    Leave empty if you don't want to apply this filter.

    Enter Hotel stars: """

visiting_city = input("Enter the City you want to visit: ")
check_in_date = input("Enter Check-in date(YYYY-MM-DD): ")
check_out_date = input("Enter Check-out date(YYYY-MM-DD): ")
number_of_adult_travellers = int(input("Enter number of travellers: "))
number_of_rooms = int(input("Enter number of rooms required: "))
sort_by = SortChoice[int(input(sort_by_input_string))]
star_values = input(filter_star_input_string).split()

with Booking() as bot:
    hotel_deals = bot.fetch_hotel_deals(
        visiting_city,
        check_in_date,
        check_out_date,
        number_of_adult_travellers,
        number_of_rooms,
        sort_by,
        star_values
    )

    table = PrettyTable(
        field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
    )
    table.add_rows(hotel_deals)
    print(table)
