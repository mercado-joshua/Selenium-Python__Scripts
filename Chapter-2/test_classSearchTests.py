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

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_class_name("search-icon")
        self.search_field.click()

        # enter search keyword and submit
        self.search_field = self.driver.find_element_by_class_name("search-query")
        self.search_field.click()
        self.search_field.send_keys("phones")
        self.search_field.submit()

        # get all the anchor elements which have product names displayed currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_css_selector(".result-title > a")

        self.assertEqual(10, len(products))

    ## adding another tests
    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_class_name("search-icon")
        self.search_field.click()

        # enter search keyword and submit
        self.search_field = self.driver.find_element_by_class_name("search-query")
        self.search_field.click()
        self.search_field.send_keys("talk")
        self.search_field.submit()

        # get all the anchor elements which have product names displayed currently on result page
        products = self.driver.find_elements_by_css_selector(".result-title > a")

        self.assertEqual(10, len(products))

def main():
    unittest.main()

if __name__ == '__main__':
    main()