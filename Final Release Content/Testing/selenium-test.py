import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the chrome driver
driver = webdriver.Chrome('/Users/lachlanwatson/IFB299/Testing/chromedriver')

# go to music school homepage
driver.get("http://127.0.0.1:8000/music_school/signup")

print(driver.title)

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("id")

# # type in the search
# inputElement.send_keys("cheese!")

# # submit the form (although google automatically searches now without submitting)
# inputElement.submit()

# try:
# 	# we have to wait for the page to refresh, the last thing that seems to be updated is the title
# 	WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

# 	# You should see "cheese! - Google Search"
# 	print(driver.title)

# finally:
driver.quit()