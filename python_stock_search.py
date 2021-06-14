from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
import time


def stock_scraper(stock):
    with Chrome() as driver:
        #your code inside this indent

        #gets the tsla webpage on CNBC
        #stock=["ba","tsla"]
        for i in range(len(stock)):
            driver.get("https://www.cnbc.com/quotes/"+stock[i])

            stock_name=driver.find_element_by_class_name('QuoteStrip-name').text

            #relative xpath selector because the class name was used in multiple places
            open_price=driver.find_element_by_xpath('//*[@id="MainContentContainer"]/div/div[2]/div[1]/div[5]/div[2]/section/div[1]/ul/li[1]/span[2]').text

            high_price=driver.find_element_by_xpath('//*[@id="MainContentContainer"]/div/div[2]/div[1]/div[5]/div[2]/section/div[1]/ul/li[2]/span[2]').text

            low_price=driver.find_element_by_xpath('//*[@id="MainContentContainer"]/div/div[2]/div[1]/div[5]/div[2]/section/div[1]/ul/li[3]/span[2]').text
            #relative xpath selector because class name was used in the whole table
            close_price=driver.find_element_by_xpath('//*[@id="MainContentContainer"]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div[2]/span[1]').text


            open="Open: "+open_price
            high="High: "+high_price
            low="Low: "+low_price
            close="Close: "+close_price

            dict={
            stock[i]:[stock_name,open,high,low,close]
            }
            # print(stock_name+":")
            # print(close+":")
            # print(close_price)
            return dict
        #assert "TSLA" in driver.title

        #return Close_price
        #print(driver.title)
        #print(dict)


        #time.sleep(5)
        #quits the driver, ends browser session
        driver.quit()
