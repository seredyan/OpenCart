import time

from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
from model.users import User

class LoginPage(BasePage):




    def sign_up(self, user):
        self.ensure_logout()
        self.go_to_register()
        self.fill_sign_up_forms(user)
        self.browser.find_element(*LoginPageLocators.CHECK_BOX_PRIVACY_POLICY_AGREE).click()
        self.browser.find_element(*LoginPageLocators.CONTINUE_TO_REGISTER).click()
        self.browser.find_element(*LoginPageLocators.CONTINUE_TO_FINISH_REGISTRATION).click()










    def edit_account(self, user, edited_user):
        self.login(user)
        self.browser.find_element(*LoginPageLocators.EDIT_ACCOUNT).click()
        self.fill_sign_up_forms(edited_user)
        self.browser.find_element(*LoginPageLocators.CONTINUE_TO_REGISTER).click()

        # self.logout()





    ### auxiliary parts of the code***



    def can_login(self, user):
        self.ensure_logout()
        self.browser.implicitly_wait(0.5)
        self.login(user)
        return self.is_logged_in()



    def change_field_value(self, selector, field_name, text):
        if text is not None:
            self.browser.find_element(selector, field_name).click()
            self.browser.find_element(selector, field_name).clear()
            self.browser.find_element(selector, field_name).send_keys(text)


    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()
        else:
            return



    def go_to_account(self):
        self.browser.implicitly_wait(0.2)
        if self.is_element_present(*LoginPageLocators.GO_TO_LOGIN) or self.is_element_present(*LoginPageLocators.LOGOUT):
            self.browser.find_element(*LoginPageLocators.MY_ACCOUNT).click()
        self.browser.find_element(*LoginPageLocators.MY_ACCOUNT).click()


    def go_to_login(self):
        self.go_to_account()
        self.browser.find_element(*LoginPageLocators.GO_TO_LOGIN).click()

    def go_to_register(self):
        self.go_to_account()
        self.browser.find_element(*LoginPageLocators.GO_TO_REGISTER).click()


    def is_logged_in(self):
        self.go_to_account()
        self.browser.implicitly_wait(0.2)
        return len(self.browser.find_elements(*LoginPageLocators.LOGOUT)) > 0


    def fill_sign_up_forms(self, user):
        self.change_field_value(*LoginPageLocators.REGISTER_FIRST_NAME, user.firstname)
        self.change_field_value(*LoginPageLocators.REGISTER_LAST_NAME, user.lastname)
        self.change_field_value(*LoginPageLocators.REGISTER_EMAIL, user.username)
        self.change_field_value(*LoginPageLocators.REGISTER_PHONE, user.phone)
        self.change_field_value(*LoginPageLocators.REGISTER_PASSWORD, user.password)
        self.change_field_value(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD, user.password)


    def login(self, user):
        self.go_to_login()
        self.change_field_value(*LoginPageLocators.REGISTER_EMAIL, user.username)
        self.change_field_value(*LoginPageLocators.REGISTER_PASSWORD, user.password)
        self.browser.find_element(*LoginPageLocators.LOGIN).click()

    def logout(self):
        self.go_to_account()
        self.browser.find_element(*LoginPageLocators.LOGOUT).click()

    def should_be_success_message(self):
        return self.is_element_present(*BasePageLocators.SUCCESS_MESSAGE)











