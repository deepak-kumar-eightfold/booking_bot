from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import bookings.constant as const
from .element_finder_and_processor import ElementFinderAndProcessor
from .locators import ElementLocators as EL


class Booking(webdriver.Chrome):
    def __init__(self) -> None:
        super().__init__()
        self.element_finder = ElementFinderAndProcessor(self)
        self.implicitly_wait(15)
        self.maximize_window()
        self._landing_page()

    def __exit__(self, exc_type, exc, traceback):
        self.quit()
        return super().__exit__(exc_type, exc, traceback)

    def _landing_page(self):
        self.get(const.BASE_URL)
        self.element_finder.search_and_click_element(
            EL.close_sign_in_prompt_button
        )

    def _search_city(self, visiting_city):
        search_input_element = self.element_finder.search_element(
            EL.city_search_input_field
        )
        search_input_element.clear()
        search_input_element.send_keys(visiting_city)
        selection_list_item = self.element_finder.search_element(
            EL.city_selection_list_item
        )
        if selection_list_item.text == visiting_city:
            self.element_finder.click_element(
                selection_list_item
            )
        else:
            try:
                WebDriverWait(self, 10).until(
                    EC.text_to_be_present_in_element(
                        EL.city_selection_list_item,
                        visiting_city
                    )
                )
            except:
                print(f"{visiting_city} not found on booking.com")
            finally:
                self.element_finder.click_element(
                    selection_list_item
                )

    def _select_dates(self, check_in_date, check_out_date):

        self.element_finder.search_and_click_element(
            (
                EL.date_picker[0],
                EL.date_picker[1].replace(
                    EL.replacement_text,
                    check_in_date
                )
            )
        )
        self.element_finder.search_and_click_element(
            (
                EL.date_picker[0],
                EL.date_picker[1].replace(
                    EL.replacement_text,
                    check_out_date
                )
            )
        )

    def _accomodation_counter(
        self,
        increment_button,
        decrement_button,
        value_span,
        count
    ):

        while int(value_span.text) != count:
            if int(value_span.text) > count:
                decrement_button.click()
            else:
                increment_button.click()

    def _select_accomodations(
        self,
        number_of_adult_travellers=2,
        number_of_rooms=1
    ):
        # Must have at least one traveller and one room
        if number_of_rooms < 1:
            number_of_rooms = 1

        if number_of_adult_travellers < 1:
            number_of_adult_travellers = 1

        self.element_finder.search_and_click_element(
            EL.accomodation_selector_element
        )

        traveller_increment_button = self.element_finder.search_element(
            (
                EL.increment_counter_button[0],
                EL.increment_counter_button[1].replace(
                    EL.replacement_text,
                    EL.traveller_counter_id
                )
            )
        )
        traveller_decrement_button = self.element_finder.search_element(
            (
                EL.decrement_counter_button[0],
                EL.decrement_counter_button[1].replace(
                    EL.replacement_text,
                    EL.traveller_counter_id
                )
            )
        )
        traveller_number_span = self.element_finder.search_element(
            (
                EL.counter_value_span[0],
                EL.counter_value_span[1].replace(
                    EL.replacement_text,
                    EL.traveller_counter_id
                )
            )
        )
        self._accomodation_counter(
            traveller_increment_button,
            traveller_decrement_button,
            traveller_number_span,
            number_of_adult_travellers
        )

        room_increment_button = self.element_finder.search_element(
            (
                EL.increment_counter_button[0],
                EL.increment_counter_button[1].replace(
                    EL.replacement_text,
                    EL.room_counter_id
                )
            )
        )
        room_decrement_button = self.element_finder.search_element(
            (
                EL.decrement_counter_button[0],
                EL.decrement_counter_button[1].replace(
                    EL.replacement_text,
                    EL.room_counter_id
                )
            )
        )
        room_number_span = self.element_finder.search_element(
            (
                EL.counter_value_span[0],
                EL.counter_value_span[1].replace(
                    EL.replacement_text,
                    EL.room_counter_id
                )
            )
        )
        self._accomodation_counter(
            room_increment_button,
            room_decrement_button,
            room_number_span,
            number_of_rooms
        )

        self.element_finder.search_and_click_element(
            EL.search_button
        )

    def _sort_results_by(self, sort_by):
        if sort_by == "":
            return
        self.element_finder.search_and_click_element(
            EL.sort_option_menu_button
        )
        sort_choice_button = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((
                EL.sort_option_item_button[0],
                EL.sort_option_item_button[1].replace(
                    EL.replacement_text,
                    sort_by
                )
            ))
        )
        sort_choice_button.click()

    def _filter_by_hotel_star(self, star_values):
        for star_value in star_values:
            if star_value == '1':
                continue
            self.element_finder.search_and_click_element(
                (
                    EL.star_filter_checkbox[0],
                    EL.star_filter_checkbox[1].replace(
                        EL.replacement_text,
                        star_value
                    )
                )
            )

    def _extract_results(self):
        self.refresh()
        hotel_boxes = self.element_finder.search_elements(
            EL.hotel_deal_list_div
        )

        top_hotel_collection = []

        for hotel_box in hotel_boxes:
            hotel_name = hotel_box.find_element(
                EL.hotel_name_div[0],
                EL.hotel_name_div[1]
            ).get_attribute('innerHTML').strip()

            hotel_price = hotel_box.find_element(
                EL.hotel_price_span[0],
                EL.hotel_price_span[1]
            ).get_attribute('innerHTML').strip()
            hotel_price = hotel_price.replace("&nbsp;", " ")

            hotel_rating = hotel_box.find_element(
                EL.hotel_rating_div[0],
                EL.hotel_rating_div[1]
            ).get_attribute('innerHTML').strip()

            top_hotel_collection.append(
                [hotel_name, hotel_price, hotel_rating]
            )

        return top_hotel_collection

    def fetch_hotel_deals(
        self,
        visiting_city: str,
        check_in_date: str,
        check_out_date: str,
        number_of_travellers: int,
        number_of_rooms: int,
        sort_by: str,
        star_values: list[str]
    ) -> list:
        self._search_city(visiting_city)
        self._select_dates(check_in_date, check_out_date)
        self._select_accomodations(number_of_travellers, number_of_rooms)
        self._sort_results_by(sort_by)
        self._filter_by_hotel_star(star_values)
        return self._extract_results()
