import unittest
from selenium import webdriver
import subprocess
import time

class SearchProductTest(unittest.TestCase):
    def setUp(self):
        # start the recording of movie
        self.proc = subprocess.Popen(['ffmpeg', '-f', 'gdigrab', '-framerate', '15', '-offset_x', '0', '-offset_y', '0', '-video_size', '1920x1080', '-i', 'desktop', '-c:v', 'libx264', '-vprofile', 'baseline', '-g', '15', '-crf', '1', '-pix_fmt', 'yuv420p', '-threads', '4', 'output.mkv'])

        self.driver = webdriver.Chrome(executable_path=r'C:\\Selenium\\WebDriver\\Chrome\\chromedriver89_win32.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://demo.magentocommerce.com/")

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

    def tearDown(self):
        # close the browser window
        self.driver.quit()
        # Stop the recording
        time.sleep(10)
        self.proc.kill()

if __name__ == '__main__':
    unittest.main(verbosity=2)