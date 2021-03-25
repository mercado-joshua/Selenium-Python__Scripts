from base_page import BasePage
from base_page import InvalidPageException

class ProductPage(BasePage):
    _product_view_locator = '#block-magento-content'
    _product_name_locator = '.content h1 span'
    _product_description_locator = '.blog-content h3'
    _product_date_locator = '.blog-date'

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def name(self):
        return self.driver.find_element_by_css_selector(self._product_name_locator).text.strip()

    @property
    def description(self):
        return self.driver.find_element_by_css_selector(self._product_description_locator).text.strip()

    # @property
    # def stock_status(self):
    #     return self.driver.find_element_by_css_selector(self._product_stock_status_locator).text.strip()

    @property
    def date(self):
        return self.driver.find_element_by_css_selector(self._product_date_locator).text.strip()

    def _validate_page(self, driver):
        try:
            driver.find_element_by_css_selector(self._product_view_locator)
        except:
            raise InvalidPageException('Product page not loaded')