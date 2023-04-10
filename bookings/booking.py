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

    def _accomodation_counter(self, counter_element, count):
        decrement_button = counter_element.find_element(
            By.XPATH,
            "./button[1]"
        )
        increment_button = counter_element.find_element(
            By.XPATH,
            "./button[2]"
        )
        show_travellers_span = counter_element.find_element(
            By.XPATH,
            "./span"
        )

        while int(show_travellers_span.text) != count:
            if int(show_travellers_span.text) > count:
                decrement_button.click()
            else:
                increment_button.click()

    def select_accomodations(
        self,
        number_of_adult_travellers=2,
        number_of_rooms=1
    ):
        # Must have at least one traveller and one room
        if number_of_rooms == 0:
            number_of_rooms = 1

        if number_of_adult_travellers == 0:
            number_of_adult_travellers = 1

        travel_accomodation_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="occupancy-config"]'
        )
        travel_accomodation_element.click()

        adult_selection_element = self.find_element(
            By.XPATH,
            '//div[contains(@class, "b2b5147b20")]//input[@id="group_adults"]/following-sibling::div[contains(@class, "e98c626f34")]'
        )
        self._accomodation_counter(
            adult_selection_element, number_of_adult_travellers
        )

        room_selection_element = self.find_element(
            By.XPATH,
            '//div[contains(@class, "b2b5147b20")]//input[@id="no_rooms"]/following-sibling::div[contains(@class, "e98c626f34")]'
        )
        self._accomodation_counter(
            room_selection_element, number_of_rooms
        )

    def click_search(self):
        search_button = self.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]'
        )
        search_button.click()

    def sort_results_by(self, sort_by):
        sort_selection_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="sorters-dropdown-trigger"]'
        )
        sort_selection_element.click()

        sort_choice_button = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                f"button[data-id='{sort_by}']"
            ))
        )
        sort_choice_button.click()
