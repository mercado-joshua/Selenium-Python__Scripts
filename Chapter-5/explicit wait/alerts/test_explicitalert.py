from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import unittest

class ExplicitWaitTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\\Selenium\\WebDriver\\Chrome\\chromedriver89_win32.exe')
        self.driver.get("file:///C:\\Users\\joshua\\Desktop\\Selenium-Test\\Chapter-5\\explicit wait\\alerts\\index.html")

    def test_alert(self):
        # wait for button to be visible
        button = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "js-btn")))

        # click on Clear All link this will display an alert to the user
        button.click()

        # wait for the alert to present
        alert = WebDriverWait(self.driver, 10).until(ec.alert_is_present())

        # get the text from alert
        alert_text = alert.text

        # check alert text
        self.assertEqual("Hello! I am an alert box!", alert_text)

        # click on Ok button
        alert.accept()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)