
from selenium.webdriver.common.by import By


class ElementLocators:
    replacement_text = "REPLACE_THIS"

    close_sign_in_prompt_button = (
        By.CSS_SELECTOR,
        'button[aria-label="Dismiss sign in information."]'
    )

    city_search_input_field = (
        By.ID,
        ":Ra9:"
    )
    city_selection_list_item = (
        By.CLASS_NAME,
        "a40619bfbe"
    )

    date_picker = (
        By.CSS_SELECTOR,
        'span[data-date="REPLACE_THIS"]'
    )

    accomodation_selector_element = (
        By.CSS_SELECTOR,
        'button[data-testid="occupancy-config"]'
    )
    room_counter_id = "no_rooms"
    traveller_counter_id = "group_adults"
    decrement_counter_button = (
        By.XPATH,
        '//div[contains(@class, "b2b5147b20")]//input[@id="REPLACE_THIS"]/following-sibling::div[contains(@class, "e98c626f34")]//button[1]'
    )
    increment_counter_button = (
        By.XPATH,
        '//div[contains(@class, "b2b5147b20")]//input[@id="REPLACE_THIS"]/following-sibling::div[contains(@class, "e98c626f34")]//button[2]'
    )
    counter_value_span = (
        By.XPATH,
        '//div[contains(@class, "b2b5147b20")]//input[@id="REPLACE_THIS"]/following-sibling::div[contains(@class, "e98c626f34")]/span'
    )

    search_button = (
        By.CSS_SELECTOR,
        'button[type="submit"]'
    )

    sort_option_menu_button = (
        By.CSS_SELECTOR,
        'button[data-testid="sorters-dropdown-trigger"]'
    )
    sort_option_item_button = (
        By.CSS_SELECTOR,
        "button[data-id='REPLACE_THIS']"
    )

    star_filter_checkbox = (
        By.XPATH,
        "//input[contains(@aria-label, 'REPLACE_THIS stars')]"
    )

    hotel_deal_list_div = (
        By.CSS_SELECTOR,
        'div[data-testid="property-card"]'
    )
    hotel_name_div = (
        By.CSS_SELECTOR,
        'div[data-testid="title"]'
    )
    hotel_rating_div = (
        By.XPATH,
        '//div[contains(@aria-label, "Scored")]'
    )
    hotel_price_span = (
        By.CSS_SELECTOR,
        'span[data-testid="price-and-discounted-price"]'
    )
