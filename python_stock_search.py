from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
import time


with Chrome() as driver:
    #your code inside this indent

    #gets the tsla webpage on CNBC
    stock=["ba","tsla"]
    for i in range(len(stock)):
        driver.get("https://www.cnbc.com/quotes/"+stock[i])

        stock_name=driver.find_element_by_class_name('QuoteStrip-name').text
        close_price=driver.find_element_by_class_name('QuoteStrip-lastPrice').text



        close="Close:"+close_price
        dict={
        stock[i]:[stock_name,close]
        }
        # print(stock_name+":")
        # print(close+":")
        # print(close_price)
        print(dict)
    #assert "TSLA" in driver.title

    #elements=driver.find_element_by_class_name('QuoteStrip-lastPriceStripContainer')

    #return Close_price
    #print(driver.title)
    #print(dict)


    time.sleep(5)
    #quits the driver, ends browser session
    driver.quit()
