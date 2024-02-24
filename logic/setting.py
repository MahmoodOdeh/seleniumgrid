from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from infra.basepage import BasePage
import time


class Setting(BasePage):
    CHOOSE_LANGUAGE_BUTTON = "(//div[@class='language-menu_header__rHHQp'])[2]"
    CHOOSE_LANGUAGE_ENGLISH = "(//div[@class='language-menu_item__n4ICI'])[1]"

    def __init__(self, driver):
        super().__init__(driver)


    def change_language_flow(self):

        time.sleep(2)

        choose_language_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CHOOSE_LANGUAGE_BUTTON))
        )
        choose_language_button.click()
        time.sleep(2)
        choose_language_english = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CHOOSE_LANGUAGE_ENGLISH))
        )
        choose_language_english.click()
        time.sleep(2)


