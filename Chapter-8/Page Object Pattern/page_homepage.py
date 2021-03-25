from base_page import BasePage
from base_page import InvalidPageException

class HomePage(BasePage):
    ## separate the locator strings
    _home_page_slideshow_locator = 'row-id-300922'

    def __init__(self, driver):
        super().__init__(driver) # to use __init__ of the BasePage (Parent Class)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_id(self._home_page_slideshow_locator)
        except:
            raise InvalidPageException("Home Page not loaded")