from selenium import webdriver
import unittest

class ExecuteJavaScriptTest (unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome(executable_path=r'C:\\Selenium\\WebDriver\\Chrome\\chromedriver89_win32.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://demo.magentocommerce.com/")

    def test_search_by_category(self):
        # get the search textbox
        search_field = self.driver.find_element_by_class_name("search-icon")
        search_field.click()

        # enter search keyword and submit
        search_field = self.driver.find_element_by_class_name("search-query")
        search_field.click()
        self.highlightElement(search_field)
        search_field.clear()

        self.highlightElement(search_field)
        search_field.send_keys("phones")
        self.highlightElement(search_field)
        search_field.submit()

        # get all the anchor elements which have product names displayed currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_css_selector(".result-title > a")

        self.assertEqual(10, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

    def highlightElement(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, "color: blue;outline: 2px solid blue;background:red")
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element , "")

if __name__ == "__main__":
    unittest.main(verbosity=2)