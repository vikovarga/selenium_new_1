from POM_demo.Locators.locators import Locators

class LoginPage():
    def __init__(self, driver):  # called every time a class object is created
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_partial_text = Locators.login_button_tag_name

    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)
        # self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)
        #find_element_by_class_name

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_login(self):
        # self.driver.find_element_by_link_text(self.login_button_partial_text).click()
        self.driver.find_element_by_tag_name(self.login_button_partial_text).click()
        # self.driver.find_element_by_partial_link_text(self.login_button_partial_text).click()
        # self.driver.find_element_by_class_name('oxd-button oxd-button--medium oxd-button--main orangehrm-login-button').click()
