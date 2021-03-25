import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):
    chromedriver = r'C:\\Selenium\\WebDriver\\Chrome\\chromedriver89_win32.exe'

    @classmethod
    def setUp(cls):
        # create a new Firefox session """
        cls.driver = webdriver.Chrome(executable_path=cls.chromedriver)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page """
        cls.driver.get("http://demo.magentocommerce.com/")

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()

    def test_search_field(self):
        # check search field exists on Home page
        self.assertTrue(self.is_element_present(By.CLASS_NAME, "search-icon"))

    def test_language_option(self):
        # check language options dropdown on Home page
        self.assertTrue(self.is_element_present(By.CLASS_NAME, "current-lan"))

    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False

        return True

if __name__ == '__main__':
    unittest.main(verbosity=2)


