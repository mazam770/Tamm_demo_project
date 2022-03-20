from selenium.webdriver.common.by import By

from Config.Config import TestData
from Pages.BasePage import BasePage

ENGLISH_BUTTON = (By.XPATH, "//a[@href='/en']")
PAGE_TITLE = (By.XPATH, "//h1[contains(@class,'TPN-intro__titles-title mb-2')]")
SEARCH_FIELD = (By.XPATH, "(//input[@name='q'])[2]")
SECOND_SEARCH_FIELD = (By.XPATH, "//input[@class='search-box-input tt-input']")
SECOND_SEARCH_LIST = (By.XPATH, "//div[@class='tt-menu tt-open']/div/div")
SECOND_SEARCH_RESULT = (By.XPATH, "//div[contains(text(),'Abu Dhabi Police')]")
SECOND_SEARCH_RESULT_LIST = (By.XPATH, "//div[contains(@class,'col-lg-9 col-md-12')]")
SEARCH_RESULT = (By.XPATH, "//div[@class='TPN-autocomplete__result']//a[1]")
SEARCH_COUNT = (By.XPATH, "//div[@class='ui-lib-margin-b_md ui-lib-margin-t_md totalResultsText']/p")
SEARCH_RESULT_LIST = (By.XPATH, "//div[@class='ui-lib-category-list-item']")
BURGER_MENU = (By.XPATH, "(//a[@href='#'])[3]")
MENU_ITEM = (By.XPATH, "(//a[@data-variantfieldname='Link'])[2]")


class Tamm_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def access_website_url(self):
        self.driver.get(TestData.BASE_URL)

    def change_language(self):
        self.wait_for_element(ENGLISH_BUTTON)
        self.do_click(ENGLISH_BUTTON)

    def is_language_changed(self) -> str:
        self.wait_for_element(PAGE_TITLE)
        return self.get_element_text(PAGE_TITLE)

    def search_for_abu_dhabi_police(self, search):
        self.wait_for_element(SEARCH_FIELD)
        self.do_click(SEARCH_FIELD)
        self.send_keys(SEARCH_FIELD, search)
        self.wait_for_element(SEARCH_RESULT)
        self.do_click(SEARCH_RESULT)

    def count_total_result(self) -> str:
        self.wait_for_element(SEARCH_COUNT)
        return self.get_element_text(SEARCH_COUNT)

    def get_first_five_results(self):
        self.wait_for_element(SEARCH_RESULT_LIST)
        elements = self.get_element_list(SEARCH_RESULT_LIST)
        data = []
        for element in elements:
            data.append(element.text)
        return data

    def refresh(self):
        self.driver.refresh()

    def access_url(self):
        self.driver.get(TestData.BASE_URL_FOR_SECOND_CASE)

    def click_burger_menu(self):
        self.wait_for_element(BURGER_MENU)
        self.do_click(BURGER_MENU)

    def click_abu_dhabi_govt_services(self):
        self.wait_for_element(MENU_ITEM)
        self.do_click(MENU_ITEM)

    def search_adp(self, search):
        self.wait_for_element(SECOND_SEARCH_FIELD)
        self.do_click(SECOND_SEARCH_FIELD)
        self.send_keys(SECOND_SEARCH_FIELD, search)

    def confirm_adp_in_suggestion_list(self):
        self.wait_for_element(SECOND_SEARCH_LIST)
        self.get_element_list(SECOND_SEARCH_LIST)

        elements = self.get_element_list(SECOND_SEARCH_LIST)
        data = []
        for element in elements:
            data.append(element.text)
        return data

    def select_adp_from_suggestion_list(self):
        self.do_click(SECOND_SEARCH_RESULT)

    def verify_adp_results_on_page(self):
        self.wait_for_element(SECOND_SEARCH_RESULT_LIST)

        elements = self.get_element_list(SECOND_SEARCH_RESULT_LIST)
        data = []
        for element in elements:
            data.append(element.text)
        return data
