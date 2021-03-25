from abc import abstractmethod

class BasePage:
    """All page objects inherit from this"""
    def __init__(self, driver):
        self._validate_page(driver)
        self.driver = driver

    ## blueprint method, one of the methods to be implemented in other pages
    @abstractmethod
    def _validate_page(self, driver):
        return

    """Regions define functionality available through all page objects"""
    @property
    def search(self):
        from region_search import SearchRegion
        return SearchRegion(self.driver)

class InvalidPageException(Exception):
    """Throw this exception when you don't find the correct page"""
    pass