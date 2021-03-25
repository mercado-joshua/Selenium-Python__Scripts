import unittest
import csv
from ddt import ddt, data, unpack
from selenium import webdriver

def get_data(file_name):
    # create an empty list to store rows
    rows = []

    # open the CSV file
    data_file = open(file_name, "rb")

    # create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader, None)

    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(executable_path=r'C:\\Selenium\\WebDriver\\Chrome\\chromedriver89_win32.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://demo.magentocommerce.com/")

    # specify test data using @data decorator
    @data(*get_data("testdata.csv"))
    @unpack
    def test_search(self, search_value, expected_count):

        # get the search textbox
        self.search_field = self.driver.find_element_by_class_name("search-icon")
        self.search_field.click()

        # enter search keyword and submit
        self.search_field = self.driver.find_element_by_class_name("search-query")
        self.search_field.clear()
        self.search_field.click()

        self.search_field.send_keys(search_value)
        self.search_field.submit()

        products = self.driver.find_elements_by_css_selector(".result-title > a")

        expected_count = int(expected_count)
        if expected_count > 0:
            # check count of products shown in results
            self.assertEqual(expected_count, len(products))

        else:
            msg = self.driver.find_element_by_class_name("note-msg")
            self.assertEqual("Your search returns no results.", msg.text)

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)