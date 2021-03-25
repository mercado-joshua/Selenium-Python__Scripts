from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import unittest

class ExplicitWaitTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\\Selenium\\WebDriver\\Chrome\\chromedriver89_win32.exe')
        self.driver.get("http://demo.magentocommerce.com/")

    def test_account_link(self):

        ## 1 : Implementing custom wait conditions
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id("js-headerbutton").get_attribute("href") == "https://magento.com/products/experience-magento?utm_source=m.com&utm_medium=website&utm_campaign=WW_200101_WBS_ACOM_ForgeDX_Overview_Demo")

        ## 2
        careers = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.LINK_TEXT, "Careers")))
        careers.click()

    ## Waiting for an element to be enabled
    def test_create_new_customer(self):
        # click on Log In link to open Login page
        account_icon_button = self.driver.find_element_by_class_name("account-icon")
        account_icon_button.click()

        account_button = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.LINK_TEXT, "Create an account")))
        account_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)