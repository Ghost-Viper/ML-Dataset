from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage


class Homepage:
    def __init__(self,driver): # retrieved the driver from 'test_e2e' method
        self.driver=driver

    shop = (By.XPATH, "//a[text()='Shop']")

    def shop_page(self):
        self.driver.find_element(*Homepage.shop).click()
        shoppage = ShopPage(self.driver)
        return shoppage






