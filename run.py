import time

from bookings.booking import Booking
from bookings.constant import SortChoice

with Booking() as bot:
    bot.landing_page()
    bot.search_city(visiting_city="Bangalore")
    bot.select_dates('2023-04-12', '2023-04-19')
    bot.select_accomodations(3, 2)
    bot.click_search()
    bot.sort_results_by(SortChoice.RATING_AND_PRICE)
    time.sleep(5)
