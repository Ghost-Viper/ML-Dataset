from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Webapp_HomePage:

    name = (By.NAME, 'name')
    email = (By.NAME,'email')
    password = (By.CSS_SELECTOR,"[placeholder='Password']")
    checkbox = (By.ID,"exampleCheck1")
    dropdown = (By.ID,"exampleFormControlSelect1")
    status = (By.CSS_SELECTOR,"[value='option2']")
    date = (By.NAME,"bday")
    submit = (By.CSS_SELECTOR,"[value='Submit']")
    text = (By.XPATH,"//div/strong")
    def __init__(self,driver):
        self.driver = driver

    def webapp_name(self):
        return self.driver.find_element(*Webapp_HomePage.name)
    def webapp_email(self):
        return self.driver.find_element(*Webapp_HomePage.email)
    def webapp_password(self):
        return self.driver.find_element(*Webapp_HomePage.password)
    def webapp_checkbox(self):
        return self.driver.find_element(*Webapp_HomePage.checkbox)
    def webapp_dropdown(self):
        return Select(self.driver.find_element(*Webapp_HomePage.dropdown))
    def webapp_status(self):
        return self.driver.find_element(*Webapp_HomePage.status)
    def webapp_date(self):
        return self.driver.find_element(*Webapp_HomePage.date)
    def webapp_submit(self):
        return self.driver.find_element(*Webapp_HomePage.submit)
    def webapp_text(self):
        return self.driver.find_element(*Webapp_HomePage.text)

