from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    appointment = (By.ID, "btn-make-appointment")
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    button = (By.ID, "btn-login")

    def getAppointment(self):
        return self.driver.find_element(*LoginPage.appointment)

    def getUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getLogin(self):
        return self.driver.find_element(*LoginPage.button)


