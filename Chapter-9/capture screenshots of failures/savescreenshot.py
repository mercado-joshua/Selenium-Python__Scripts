from selenium import webdriver
import datetime, time, unittest
from selenium.common.exceptions import NoSuchElementException

class ScreenShotTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\\Selenium\\WebDriver\\Chrome\\chromedriver89_win32.exe')
        self.driver.get("http://demo.magentocommerce.com/")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_screen_shot(self):
        driver = self.driver
        try:
            promo_banner_elem = driver.find_element_by_id("promo_banner")
            self.assertEqual("Promotions", promo_banner_elem.text)

        except NoSuchElementException:
            # pass ther path and the filename
            st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
            file_name = "main_page_missing_banner" + st + ".png"
            driver.save_screenshot(file_name)
            raise
            """
            raise without any arguments is a special use of python syntax. It means get the exception and re-raise it. If this usage it could have been called reraise.

            If no expressions are present, raise re-raises the last exception that was active in the current scope.
            """

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)