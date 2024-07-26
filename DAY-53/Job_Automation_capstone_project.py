#capstone project
import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
import lxml

EDGE_DRIVER_PATH=webdriver.EdgeService(executable_path="C:\\Users\\naolm\\Downloads\\Compressed\\edgedriver_win64\\msedgedriver.exe")
form_link= "https://docs.google.com/forms/d/e/1FAIpQLSd--yT14Dzg6w69ip4WkV36Flh_9h562uEj1pdB7Pvy_nAKjA/viewform?usp=sf_link"
zillow_link= "https://www.zillow.com/new-york-ny/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A40.988741695224775%2C%22south%22%3A40.405685665239744%2C%22east%22%3A-73.4399776308594%2C%22west%22%3A-74.51938436914065%7D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%7D"
header= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8"
}
response= requests.get(zillow_link, headers=header)
soup= BeautifulSoup(response.content, "lxml")

prices= soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine-srp-8-102-0__sc-16e8gqd-1 vjmXt")
p_list= []
for price in prices:
    txt=price.get_text()
    price=txt.split("+")[0]
    p_list.append(price)
# print(p_list)
price_list=[]
for price in p_list:
    price= price.split("/")[0]
    price_list.append(price)
# print(price_list)

addresses = soup.find_all(name="a"  , class_="StyledPropertyCardDataArea-c11n-8-102-0__sc-10i1r6-0 klMkvj property-card-link")

address_list=[]


for address in addresses:
    txt= address.get_text()
    address_list.append(txt)
# print(address_list)
# print(len(address_list))

property_links= soup.find_all(href= True , class_="StyledPropertyCardDataArea-c11n-8-102-0__sc-10i1r6-0 klMkvj property-card-link")
links_list=[]
for link in property_links:
    lin= link["href"]
    if "http" not in lin:
        links_list.append(f"https://www.zillow.com{lin}")
    else:
        links_list.append(lin)
# print(links_list)
# print(len(links_list))

driver= webdriver.Edge(service= EDGE_DRIVER_PATH)

sleep(8)





for i in range(len(address_list)):
    driver.get(form_link)
    sleep(2)
    submit_button= driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    add_input= driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input= driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input= driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_input.send_keys(address_list[i])
    
    price_input.send_keys(price_list[i])
    
    link_input.send_keys(links_list[i])
    
    submit_button.click()
    





