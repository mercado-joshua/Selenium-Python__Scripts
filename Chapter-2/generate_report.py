import unittest
from HtmlTestRunner import HTMLTestRunner

from test_classSearchTests import SearchTests
from test_homepageTest import HomePageTest

# get all tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

#1
# run the suite (default, individual reports)
# runner = HTMLTestRunner(output='example_suite')
# runner.run(smoke_tests)

#2
# combine into single report
runner = HTMLTestRunner(combine_reports=True, report_name='MyReport', add_timestamp=False)
runner.run(smoke_tests)