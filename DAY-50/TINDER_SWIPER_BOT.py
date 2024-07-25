from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

FB_EMAIL= "naol@example.com"
FB_PASSWORD= "qwerty123"

chrome_driver_path= "C:/development/chromedriver"
driver= webdriver.Chrome(chrome_driver_path)
driver.get("https://www.tinder.com")

sleep(2)
login_button= driver.find_element_by_xpath()
login_button.click()

sleep(2)
fb_login_button= driver.find_element_by_xpath()
fb_login_button.click()

sleep(2)
base_window= driver.window_handles[0]
fb_window= driver.window_handles[1]
driver.switch_to.window(fb_window)

email= driver.find_element_by_xpath()
password= driver.find_element_by_xpath()

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)


driver.switch_to.window(base_window)

sleep(5)
allow_locations_button= driver.find_element_by_xpath()
allow_locations_button.click()

cookies_button= driver.find_element_by_xpath()
cookies_button.click()

notifications_button= driver.find_element_by_xpath()
notifications_button.click()


#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()
