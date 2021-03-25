import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    chromedriver = r'C:\\Selenium\\WebDriver\\Chrome\\chromedriver89_win32.exe'

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=cls.chromedriver)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page
        cls.driver.get("http://demo.magentocommerce.com/")
        cls.driver.title

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    ## id
    def test_search_text_field_max_length(self):
        # get the search textbox
        search_field = self.driver.find_element_by_id("edit-keys")

        # check maxlength attribute is set to 128
        self.assertEqual("128", search_field.get_attribute("maxlength"))

    ## class
    def test_search_button_enabled(self):
        # get Search button
        search_button = self.driver.find_element_by_class_name("search-icon")

        # check Search button is enabled
        self.assertTrue(search_button.is_enabled())

def main():
    unittest.main()

if __name__ == '__main__':
    main()