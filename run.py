import time

from bookings.booking import Booking
from bookings.constant import SortChoice

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

with Booking() as bot:
    bot.search_city(
        visiting_city=input("Enter the City you want to visit: ").strip()
    )
    bot.select_dates(
        check_in_date=input("Enter Check-in date(YYYY-MM-DD): ").strip(),
        check_out_date=input("Enter Check-out date(YYYY-MM-DD): ").strip()
    )
    bot.select_accomodations(
        number_of_adult_travellers=int(input("Enter number of travellers: ")),
        number_of_rooms=int(input("Enter number of rooms required: "))
    )
    bot.sort_results_by(
        sort_by=SortChoice[int(input(sort_by_input_string))]
    )
    bot.filter_by_hotel_star(
        star_values=list(map(int, input(filter_star_input_string).split()))
    )
    bot.get_bookings()
