from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "Wrong url"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_LOGIN_INPUT), "Login-form login is not presented"
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_PASSWORD_INPUT), "Login-form password is not " \
                                                                                   "presented "

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_EMAIL_INPUT), "Register-form email is not presented"
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_PASSWORD_INPUT), "Register-form password is not " \
                                                                                   "presented "
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_PASSWORD_REPEAT_INPUT), "Register-form " \
                                                                                          "password-repeat is not " \
                                                                                          "presented "
