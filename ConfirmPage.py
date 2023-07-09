from selenium.webdriver.common.by import By

class ConfirmPage:

    dropdown = (By.ID, "country")
    select_dropdown = (By.LINK_TEXT, "United Arab Emirates")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    button = (By.CSS_SELECTOR, "input[class*='btn-lg']")
    expected_text = (By.CSS_SELECTOR, "div[class*='alert'] strong")

    def __init__(self,driver):
        self.driver = driver

    def get_dropdown(self):
        return self.driver.find_element(*ConfirmPage.dropdown)

    def get_dropdown_value(self):
        return self.driver.find_element(*ConfirmPage.select_dropdown)

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def get_button(self):
        return self.driver.find_element(*ConfirmPage.button)

    def get_text(self):
        return self.driver.find_element(*ConfirmPage.expected_text)


