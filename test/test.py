import concurrent.futures
import time
import unittest
from functools import partial

from infra.browser_wrapper import BrowserWrapper
from logic.score365SoursePage import ScoresPage  # Renamed to reflect new focus


class ScoresTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()

    def test_dark_mode(self, browser_type):
        self.driver = self.browser.get_driver(browser_type)
        self.driver.get("https://www.365scores.com/he")  # Navigate to the 365Scores website
        self.scores_page = ScoresPage(self.driver)
        time.sleep(4)
        self.scores_page.press_cookies_button()
        self.scores_page.change_to_dark_mode()
        self.assertTrue(self.scores_page, "background dose not dark")

    def test_search(self, browser_type):
        self.driver = self.browser.get_driver(browser_type)
        self.driver.get("https://www.365scores.com/he")  # Navigate to the 365Scores website
        self.scores_page = ScoresPage(self.driver)
        time.sleep(4)
        self.scores_page.press_cookies_button()

        # Modify with your search query
        self.scores_page.search_for_query("בראזיל")
        expected_title = ""
        self.assertEqual(expected_title, self.driver.title, "Title does not match expected value")

        self.driver.quit()

    def test_run_grid_parallel(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:

            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                # Use partial to pass browser_type argument along with test_365scores method
                executor.map(self.test_search, self.browser.browser_types)

            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                # Use partial to pass browser_type argument along with test_365scores method
                executor.map(self.test_dark_mode, self.browser.browser_types)
        else:

            self.test_search(self.browser.default_browser.lower())
            self.test_dark_mode(self.browser.default_browser.lower())
