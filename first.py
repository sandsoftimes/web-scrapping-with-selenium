import os
import sys
from selenium import webdriver # used to create driver to help us scrape website
website='https://www.adamchoi.co.uk/overs/detailed' # Define which site to scrape
path='/home/spoofy/Downloads/chromedriver_linux64' #path of chrome driver
driver=webdriver.Chrome(path) #define driver variable # webdriver.Firefox(path) for firefox e.t.c 
driver.get(website)