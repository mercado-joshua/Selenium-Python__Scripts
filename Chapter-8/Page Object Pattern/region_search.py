from base_page import BasePage
from base_page import InvalidPageException
from page_productpage import ProductPage

class SearchRegion(BasePage):
    ## separate the locator strings
    _search_box_locator1 = "search-icon"
    _search_box_locator2 = "search-query"

    def __init__(self, driver):
        super().__init__(driver)

    def searchFor(self, term):
        # get the search textbox
        self.search_field = self.driver.find_element_by_class_name("search-icon")
        self.search_field.click()

        # enter search keyword and submit
        self.search_field = self.driver.find_element_by_class_name("search-query")
        self.search_field.clear()
        self.search_field.click()

        self.search_field.send_keys(term)
        self.search_field.submit()

        return SearchResults(self.driver)

class SearchResults(BasePage):
    ## separate the locator strings
    _product_list_locator = 'ol > li'
    _product_name_locator = 'result-title > a'
    _product_result_link = 'result-url > a'

    _page_title_locator = 'title'
    _products_count = 0
    _products = {}

    def __init__(self, driver):
        super().__init__(driver)

        results = self.driver.find_elements_by_css_selector(self._product_list_locator)

        for product in results:
            name = product.find_element_by_css_selector(self._product_name_locator).text
            self._products[name] = product.find_element_by_css_selector(self._product_result_link)

    def _validate_page(self, driver):
        if 'Search | Magento' not in driver.title:
            raise InvalidPageException('Search results not loaded')

    @property
    def product_count(self):
        return len(self._products)

    def get_products(self):
        return self._products

    def open_product_page(self, product_name):
        self._products[product_name].click()
        return ProductPage(self.driver)