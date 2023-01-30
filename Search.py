import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:/Users/PC/Desktop/python/Selenium_Series/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com")

search = driver.find_element(By.NAME,"q")
search.send_keys("marshmello")
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()  #search button
#search.send_keys(Keys.RETURN)
time.sleep(3)

driver.find_element(By.LINK_TEXT,"Images").click()
time.sleep(5)

driver.find_element(By.LINK_TEXT,"Videos").click()
time.sleep(5)

driver.find_element(By.LINK_TEXT,"News").click()
time.sleep(5)
driver.back()
time.sleep(3)
 #Scroll to bottom
driver.execute_script("window.scrollTo(0,1000);")
time.sleep(2)
driver.execute_script("window.scrollTo(1000,1500);")
time.sleep(2)
driver.execute_script("window.scrollTo(1500,2000);")
time.sleep(3)


 # go to 2nd page
driver.find_element(By.XPATH,"//*[@id='botstuff']/div/div[2]/table/tbody/tr/td[3]/a").click()
time.sleep(3)






