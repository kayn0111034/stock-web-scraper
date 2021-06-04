from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("http://www.cnbc.com/quotes")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()



#Simple assignment
from selenium.webdriver import Chrome

driver = Chrome()

#Or use the context manager
from selenium.webdriver import Chrome

with Chrome() as driver:
    #your code inside this indent

    #gets the tsla webpage on CNBC
    driver.get("https://www.cnbc.com/quotes/tsla")

    assert "TSLA" in driver.title

    elements=driver.find_elements(By.classname, 'QuoteStrip-lastPriceStripContainer')
    Close_price=elements.find_elements(By.classname, 'QuoteStrip-lastPrice')
    


    #quits the driver, ends browser session
    driver.quit()
