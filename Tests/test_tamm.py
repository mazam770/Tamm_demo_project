from assertpy import assert_that

from Config.Config import TestData
from Pages.tamm_page import Tamm_Page
from Tests.Base_Class import BaseClass


class TestTammDemoClass(BaseClass):

    def test_first_test_case(self):
        self.tamm_page = Tamm_Page(self.driver)
        self.tamm_page.access_website_url()
        self.tamm_page.change_language()
        assert_that(self.tamm_page.is_language_changed(),
                    "Language change").is_equal_to("Abu Dhabi Government Services")

        self.tamm_page.search_for_abu_dhabi_police(TestData.SEARCH_TEXT)
        count_before_refresh = self.tamm_page.count_total_result()
        result_list_before_refresh = self.tamm_page.get_first_five_results()

        for element in range(5):
            self.tamm_page.refresh()
            count_after_refresh = self.tamm_page.count_total_result()
            result_list_after_refresh = self.tamm_page.get_first_five_results()

            if count_before_refresh == count_after_refresh and result_list_before_refresh == result_list_after_refresh:
                continue
            else:
                return 0

    def test_second_test_case(self):
        self.tamm_page = Tamm_Page(self.driver)
        self.tamm_page.access_url()
        self.tamm_page.click_burger_menu()
        self.tamm_page.click_abu_dhabi_govt_services()
        self.tamm_page.search_adp(TestData.SEARCH_ADP_TEXT)
        assert_that(self.tamm_page.confirm_adp_in_suggestion_list(),
                    "Suggestion list").contains("Abu Dhabi Police")

        self.tamm_page.select_adp_from_suggestion_list()
        results = self.tamm_page.verify_adp_results_on_page()
        for result in results:
            assert_that(result, "result of sdp").contains("Abu Dhabi Police")
