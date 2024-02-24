from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from infra.basepage import BasePage
import time


class Cookies(BasePage):
    COOKIES_BUTTON = '//button[@id="didomi-notice-agree-button"]'

    def __init__(self, driver):
        super().__init__(driver)

    def press_cookies_button(self):
        print("click cookies")

        cookies_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COOKIES_BUTTON))
        )
        cookies_button.click()
        time.sleep(3)
