#!/usr/bin/env python
# coding: utf-8

# # Importing Required Modules

# This program scrapes the web to create pdf files of a desired web search.

# In[2]:


from selenium import webdriver
import pdfkit
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import search


# # The Scraper Function

# In[3]:


browser = webdriver.Chrome('/Users/arslanmac/Downloads/chromedriver')

###  results_array(number_search_pages, name_of_the_engine): creates an an array of the 'not-google' links on the
###  on the number of 'number_search_pages' search pages.

def results_array(name_of_the_engine, number_search_pages=1):
    results = []
    for loop in range(1, number_search_pages):
        for elm in browser.find_elements_by_xpath('//*[@id="rso"]//a'):
            href = elm.get_attribute('href')
            if search(name_of_the_engine, href):
                pass
            else:
                results.append(href)
        press_next = browser.find_element_by_id('pnnext')
        press_next.click()

        

###  pdf_from_result(): prints pdf of the result from results array

def pdf_from_result():
    for result in results:
        try:
            browser.get(result)
            pdfkit.from_url(result, '%s .pdf' %browser.title)
            sleep(2)
        except:
            pass
    return results

### scraper(search_term): scrapes the search_engine based on te

def scraper(search_term, url = "https://www.google.com/"):
    browser.get(url)
    search_box = browser.find_element_by_name('q')
    search_box.send_keys(search_term)
    search_box.submit()
    sleep(1)
    results_array('google', 19)
    pdf_from_result()
    


# In[ ]:


scraper("Search input")           

