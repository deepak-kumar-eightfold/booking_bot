from bookings.booking import Booking
import time
with Booking() as bot:
    bot.landing_page()
    bot.search_city(visiting_city="Bangalore")
    bot.select_dates('2023-04-12', '2023-04-19')
    time.sleep(5)
