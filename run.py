from bookings.booking import Booking
import time
with Booking() as bot:
    bot.landing_page()
    time.sleep(5)
