from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
EMAIL_X= ""
PASSWORD_X= ""
PROMISED_UP= 100
PROMISED_DOWN= 50
EDGE_DRIVER_PATH=webdriver.ChromeService(executable_path="C:\\Users\\naolm\\Downloads\\Compressed\\edgedriver_win64\\msedgedriver.exe")



# driver= webdriver.Edge(service=EDGE_DRIVER_PATH)
# driver.get("https://www.twitter.com")

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver= webdriver.Edge(service= driver_path)
        self.up= 0
        self.down= 0
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(8)
        Go_button=self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        Go_button.click()
        
        sleep(80)
        self.down= self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.up=self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(f"download: {self.down.text}")
        print(f"upload: {self.up.text}")
        
    
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(EMAIL_X)
        password.send_keys(PASSWORD_X)
        sleep(2)
        password.send_keys(Keys.ENTER)
        sleep(5)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(EDGE_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()

        
        


