import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.Booking_Page import BookingPage
from pageObjects.Login_Page import LoginPage
from test_data.Login_Data import LoginData
from utilities.BaseClass import BaseClass


class Test_Login(BaseClass):

    def test_login(self, setup, getData):
        login = LoginPage(self.driver)
        login.getAppointment().click()
        login.getUsername().send_keys(getData["username"])
        login.getPassword().send_keys(getData["password"])
        login.getLogin().click()

        book = BookingPage(self.driver)

        #Facility
        facility = Select(book.getFacility())
        facility.select_by_index(1)

        #Readmission
        book.getReadmission().click()

        #HealthCare_Program
        healthCareProgram = book.getProgram()
        healthCareProgram[1].click()

        #Visit_Date
        visit_date = book.getDate()
        visit_date.click()
        wait = WebDriverWait(self.driver, 10)
        picker = wait.until(EC.visibility_of_element_located((By.ID, "txt_visit_date")))
        visit_date = picker.find_element(By.XPATH, "//td[normalize-space()='30']")
        visit_date.click()

        #Comments
        book.getComments().click()
        book.getComments().send_keys("im having headache for past two days")

        #Book-Appointment
        clicking = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((book.getBooking()))
        )
        clicking.click()

        print("Health Care Appointment Booked Successfully")


    @pytest.fixture(params=LoginData.loginData)
    def getData(self, request):
        return request.param
