from selenium import webdriver
import unittest
from time import gmtime, strftime

class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\\Selenium\\WebDriver\\Chrome\\chromedriver89_win32.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://demo.magentocommerce.com/")

    def test_register_new_user1(self):
        driver = self.driver

        account_icon_button = driver.find_element_by_class_name("account-icon")
        self.assertTrue(account_icon_button.is_displayed() and account_icon_button.is_enabled())
        account_icon_button.click()

        # check title
        self.assertEqual("Sign in", driver.title)

        # get the Create Account button
        create_account_button = driver.find_element_by_link_text("Create an account")

        # check Create Account button is displayed and enabled
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())

        # click on Create Account button. This will display new account
        create_account_button.click()

        # check title
        self.assertEqual("Create New Customer Account", driver.title)

        # get all the fields from Create an Account form
        first_name = driver.find_element_by_id("firstname")
        last_name = driver.find_element_by_id("lastname")
        email_address = driver.find_element_by_id("email_address")
        company_name = driver.find_element_by_id("self_defined_company")
        password = driver.find_element_by_id("password")
        confirm_password = driver.find_element_by_id("password-confirmation")

        company_type = driver.find_element_by_id("company_type")
        individual_role = driver.find_element_by_id("individual_role")
        country = driver.find_element_by_id("country")
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div/div/div/div/button')

        self.assertTrue(first_name.is_enabled() and last_name.is_enabled() and email_address.is_enabled() and company_name.is_enabled() and company_type.is_enabled() and individual_role.is_enabled() and country.is_enabled() and password.is_enabled() and confirm_password.is_enabled() and submit_button.is_enabled())

        user_name = "user_" + strftime("%Y%m%d%H%M%S", gmtime())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
