from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    TXT_USERNAME = (By.ID, "txtUsername")
    TXT_PASSWORD = (By.ID, "txtPassword")
    BTN_LOGIN = (By.ID, "btnLogin")
    MSG_INVALIDCREDS = (By.ID,"spanMessage")

    """Constructor of CarrersPage class"""

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login_credentials(self, user, pwd):
        self.input_element(self.TXT_USERNAME, user)
        self.input_element(self.TXT_PASSWORD, pwd)

    def enter_username(self,user):
        self.input_element(self.TXT_USERNAME, user)

    def enter_password(self, pwd):
        self.input_element(self.TXT_PASSWORD, pwd)


    def enter_login(self):
        self.click_element(self.BTN_LOGIN)

    def validateTitle(self):
        assert self.get_title() == "OrangeHRM"

    def validateInvalidCreds(self):
        assert self.get_element_text(self.MSG_INVALIDCREDS) == "Invalid credentials"

    def validateEmptyUsername(self):
        assert self.get_element_text(self.MSG_INVALIDCREDS) == "Username cannot be empty"

    def validateEmptyPassword(self):
        assert self.get_element_text(self.MSG_INVALIDCREDS) == "Password cannot be empty"