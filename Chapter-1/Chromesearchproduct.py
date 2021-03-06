from selenium import webdriver

# create a new Firefox session
driver = webdriver.Chrome(executable_path=r'C:\\Selenium\\WebDriver\\Chrome\\chromedriver89_win32.exe')
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("http://demo.magentocommerce.com/")

# get the search textbox
search_field = driver.find_element_by_class_name("search-icon")
search_field.click()

# enter search keyword and submit
search_field = driver.find_element_by_class_name("search-query")
search_field.click()
search_field.send_keys("phones")
search_field.submit()

# get all the anchor elements which have product names displayed currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_css_selector(".result-title > a")

# get the number of anchor elements found
print("Found " + str(len(products)) + " products:")

# iterate through each anchor element and print the text that is name of the product
for product in products:
    print(product.text)

# close the browser window
driver.quit()