from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ElementFinderAndProcessor:
    def __init__(
        self,
        chromedriver: webdriver.Chrome
    ) -> None:
        self.driver = chromedriver

    def search_element(
        self,
        element_locator: tuple[By, str]
    ) -> WebElement:
        return self.driver.find_element(
            element_locator[0],
            element_locator[1]
        )

    def search_elements(
        self,
        element_locator: tuple[By, str]
    ) -> list[WebElement]:
        return self.driver.find_elements(
            element_locator[0],
            element_locator[1]
        )

    def click_element(
        self,
        element: WebElement
    ) -> None:
        element.click()

    def get_value_from_element(
        self,
        element: WebElement
    ) -> str:
        return element.text.strip()

    def set_value_to_element(
        self,
        element: WebElement,
        value: str
    ) -> None:
        element.send_keys(value)

    def search_and_click_element(
        self,
        element_locator: tuple[By, str]
    ) -> None:
        element = self.search_element(element_locator)
        self.click_element(element)
