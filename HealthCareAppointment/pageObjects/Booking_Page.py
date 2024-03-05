from selenium.webdriver.common.by import By


class BookingPage:
    def __init__(self, driver):
        self.driver = driver

    facility = (By.ID, "combo_facility")
    readmission = (By.NAME, "hospital_readmission")
    program = (By.CLASS_NAME, "col-sm-4")
    date = (By.ID, "txt_visit_date")
    selected_date = (By.XPATH, "//td[normalize-space()='30']")
    comments = (By.NAME, "comment")
    booking = (By.XPATH, "//button[@id='btn-book-appointment']")

    def getFacility(self):
        return self.driver.find_element(*BookingPage.facility)

    def getReadmission(self):
        return self.driver.find_element(*BookingPage.readmission)

    def getProgram(self):
        return self.driver.find_elements(*BookingPage.program)

    def getDate(self):
        return self.driver.find_element(*BookingPage.date)

    def getSelectedDate(self):
        return self.driver.find_element(*BookingPage.selected_date)

    def getComments(self):
        return self.driver.find_element(*BookingPage.comments)

    def getBooking(self):
        return self.driver.find_element(*BookingPage.booking)
