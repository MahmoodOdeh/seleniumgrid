from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from infra.basepage import BasePage
import time


class ScoresPage(BasePage):
    SEARCH_INPUT = "//input[@class='main-header-module-desktop-search-input']"
    COOKIES_BUTTON = '//button[@id="didomi-notice-agree-button"]'
    SEARCH_BUTTON = "//div[@class='main-header-module-search-widget-dropdown-container']"
    SETTING_BUTTON = "//button[@class='main-header-module-settings-button']"
    SWITCH_TO_DARK_MODE = "(//div[@class='switch-button_container__xSCbF'])[3]"
    DARK_MODE = "(//html)[1]"

    def __init__(self, driver):
        super().__init__(driver)
        self.dark_mode = self._driver.find_element(By.XPATH, self.DARK_MODE)
        self.setting_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SETTING_BUTTON))
        )

    def press_cookies_button(self):
        print("click cookies")
        cookies_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COOKIES_BUTTON))
        )
        cookies_button.click()
        time.sleep(3)

    def change_to_dark_mode(self):
        self.setting_button.click()
        time.sleep(2)
        dark_mode = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SWITCH_TO_DARK_MODE))
        )
        dark_mode.click()
        time.sleep(5)
        if self.dark_mode.get_attribute("data-theme") == "dark":
            return True
        return False

    def search_for_query(self, query):
        search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search_input.send_keys(query)
        time.sleep(2)
        search_input.send_keys(Keys.RETURN)
        time.sleep(3)
