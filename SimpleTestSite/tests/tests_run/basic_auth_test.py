from tests.page_objects.basic_auth_page import *
from tests.tests_run.base import BaseTest


class TestsAuthTab(BaseTest):
    def test_auth_content_visible(self):
        BasicAuthPage(self.driver).click_auth_tab()
        self.assertTrue(BasicAuthPage(self.driver).auth_content_visible())

    def test_auth_login_successful(self):
        BasicAuthPage(self.driver).click_auth_tab()
        self.assertTrue(BasicAuthPage(self.driver).send_correct_username())
        self.assertTrue(BasicAuthPage(self.driver).send_correct_password())

        BasicAuthPage(self.driver).click_login_button()
        self.assertTrue(BasicAuthPage(self.driver).logged_in_content_visible())
        self.assertTrue(BasicAuthPage(self.driver).logged_in_message())

    def test_auth_incorrect_username(self):
        BasicAuthPage(self.driver).click_auth_tab()
        self.assertTrue(BasicAuthPage(self.driver).send_incorrect_username())
        self.assertTrue(BasicAuthPage(self.driver).send_correct_password())

        BasicAuthPage(self.driver).click_login_button()
        self.assertTrue(BasicAuthPage(self.driver).login_error_message())

    def test_auth_incorrect_password(self):
        BasicAuthPage(self.driver).click_auth_tab()
        self.assertTrue(BasicAuthPage(self.driver).send_correct_username())
        self.assertTrue(BasicAuthPage(self.driver).send_incorrect_password())

        BasicAuthPage(self.driver).click_login_button()
        self.assertTrue(BasicAuthPage(self.driver).login_error_message())

    def test_auth_random_data(self):
        BasicAuthPage(self.driver).click_auth_tab()
        self.assertTrue(BasicAuthPage(self.driver).send_incorrect_username())
        self.assertTrue(BasicAuthPage(self.driver).send_incorrect_password())

        BasicAuthPage(self.driver).click_login_button()
        self.assertTrue(BasicAuthPage(self.driver).login_error_message())

    def test_auth_send_no_data(self):
        BasicAuthPage(self.driver).click_auth_tab()
        BasicAuthPage(self.driver).click_login_button()
        self.assertTrue(BasicAuthPage(self.driver).login_error_message())

