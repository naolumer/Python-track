import time
from selenium import webdriver

chrome_path= "C:\development\chromedriver"
driver= webdriver.Chrome(chrome_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
#cookies icon clickable
cookie= driver.find_element_by_id("cookie")

#upgradable_items
items= driver.find_elements_by_css_selector("#store div")
items_id= [item.get_attribute("id") for item in items]

timeout= time.time() + 5
five_min= time.time() + 60*5

while True:
    cookie.click()
    
    if time.time()> timeout:
        
        all_prices= driver.find_elements_by_css_selector("#store b")
        item_prices=[]
        
        for prices in all_prices:
            element_text= prices.text
            
            if element_text!="":
                cost=int(element_text.split("-")[1].strip().replace(",",""))
                item_prices.append(cost)
            
        # create a dic of store items with prices
        cookie_upgrades={}
        for n in range(len(item_prices)):
                cookie_upgrades[item_prices[n]]= items_id[n]
                
        #get the current count of cookies
        money_element= driver.find_element_by_id("money").text
        if "," in money_element:
                money_element=money_element.replace(",","")
                cookie_count= int(money_element)
                
        # dic of affordabel prices
        affordable_id={}
        
        for cost,id in cookie_upgrades.items():
            if cost<cookie_count:
                affordable_id[cost]= id
            
        #highest affordable
            
        high_affordable_upgrade= max(affordable_id)
        to_purchase_upgrade= affordable_id[high_affordable_upgrade]
            
        driver.find_element_by_id("to_purchars_id").click()
            
        timeout= time.time() + 5
    if time.time()> five_min:
        cookie_per_sec= driver.find_element_by_id("cps").text
        print(cookie_per_sec)
        break
        
        
            
            
                
            
            
            
            
        




