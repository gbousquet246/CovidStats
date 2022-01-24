# imports
from selenium import webdriver
import time

# creates a firefox webdriver profile and then disables the download popup for the file type
profile = webdriver.FirefoxProfile()

# sets the download popup preference to off
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/vnd.ms-excel")

# ADD THE profile.set_preference below for setting a doanload path here
# link to the StackOverflow article that was useful for me: https://stackoverflow.com/questions/24852709/how-do-i-automatically-download-files-from-a-pop-up-dialog-using-selenium-python

# gecko (firefox) driver location YOU MAY NEED TO DOWNLOAD THE DRIVER
geckoDriver = 'C:/Users/Garrett Bousquet/Desktop/geckodriver-v0.30.0-win64/gekodriver.exe'

# sets up the remote browser with the driver path (executable_path) and the profile options(firefox_profile)
browser = webdriver.Firefox(executable_path=geckoDriver, firefox_profile=profile)

# tells the browser where to go
browser.get("https://covid.cdc.gov/covid-data-tracker/#cases_casesper100k")

# sleeps the program to allow the page to load fully
time.sleep(1)

# targets the contaaining div and clicks to toggle it to display the download button
browser.find_element_by_css_selector('div#us-cases-table-toggle').click()

# targets the download button
element = browser.find_element_by_css_selector('button#btnUSTableExport')

# clicks the download data
element.click()

# closes the browser
browser.quit()


