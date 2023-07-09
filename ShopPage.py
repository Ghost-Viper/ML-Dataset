from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class ShopPage:

    cards = (By.XPATH, "//app-card/div")
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout_process = (By.XPATH, "//tr[3]/td[5]/button")

    def __init__(self,driver):
        self.driver = driver

    def get_cards(self):
        return self.driver.find_elements(*ShopPage.cards)

    def get_checkout(self):
        return self.driver.find_element(*ShopPage.checkout)

    def get_checkout_process(self):
        self.driver.find_element(*ShopPage.checkout_process).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage

