from selenium import webdriver
import time
import unittest
from POM_demo.Pages.loginPage import LoginPage
# from POM_demo.Pages.homePage import HomePage

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Viktor/PycharmProjects/selenium_new/driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)


    def test_login_valid(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        # driver.find_element_by_link_text()

        time.sleep(5)
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        driver.find_element_by_tag_name('button').click()
        login.click_login()  # does not work

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")