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

    # def change_currency(self, currency=None):
    #     currency_converter_element = self.find_element(
    #         By.CSS_SELECTOR,
    #         'button[data-testid="header-currency-picker-trigger"]'
    #     )
    #     currency_converter_element.click()

    def search_city(self, visiting_city):
        search_input_element = self.find_element(
            By.ID,
            ":Ra9:"
        )
        search_input_element.clear()
        search_input_element.send_keys(visiting_city)
        selection_list_item = self.find_element(
            By.CLASS_NAME,
            "a40619bfbe"
        )
        if selection_list_item.text == visiting_city:
            selection_list_item.click()
        else:
            try:
                WebDriverWait(self, 10).until(
                    EC.text_to_be_present_in_element(
                        (By.CLASS_NAME, "a40619bfbe"),
                        visiting_city
                    )
                )
            except:
                print(f"{visiting_city} not found on booking.com")
            finally:
                selection_list_item.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_date_element = self.find_element(
            By.CSS_SELECTOR,
            f'span[data-date="{check_in_date}"]'
        )
        check_in_date_element.click()

        check_out_date_element = self.find_element(
            By.CSS_SELECTOR,
            f'span[data-date="{check_out_date}"]'
        )
        check_out_date_element.click()
