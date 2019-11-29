from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    SIGN_IN_LOGIN_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    SIGN_IN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")

    SIGN_UP_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    SIGN_UP_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    SIGN_UP_PASSWORD_REPEAT_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
