import unittest
from page_homepage import HomePage
from base_testcase import BaseTestCase

class SearchProductTest(BaseTestCase):
    def testSearchForProduct(self):
        homepage = HomePage(self.driver)
        search_results = homepage.search.searchFor('phone')
        self.assertEqual(10, search_results.product_count)

        product = search_results.open_product_page('One Year Later: How the Pandemic has Changed Digital Commerce')
        self.assertEqual('One Year Later: How the Pandemic has Changed Digital Commerce', product.name)
        self.assertEqual('If you haven’t acted on these seven digital commerce learnings from 2020, they should be at the top of your to-do list for 2021.', product.description)
        self.assertEqual('March 16, 2021', product.date)

if __name__ == '__main__':
    unittest.main(verbosity=2)
