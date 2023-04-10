from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import bookings.constant as const


class Booking(webdriver.Chrome):
    def __init__(self) -> None:
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def landing_page(self):
        self.get(const.BASE_URL)
        sign_in_prompt = self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Dismiss sign in information."]'
        )
        sign_in_prompt.click()
