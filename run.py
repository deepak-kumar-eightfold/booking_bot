from bookings.booking import Booking
import time
with Booking() as bot:
    bot.landing_page()
    bot.search_city(visiting_city="Bangalore")
    time.sleep(5)
