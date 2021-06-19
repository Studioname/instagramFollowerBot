from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time

class InstaFollower():
    def __init__(self, driver_path, instagram_email, instagram_password, similar_account):
        self.driver = webdriver.Chrome(driver_path)
        self.instagram_email = instagram_email
        self.instagram_password = instagram_password
        self.similar_account = similar_account
        self.login_address = "https://www.instagram.com/accounts/login/"
        self.chains = ActionChains(self.driver)

    def login(self):
        self.driver.get(self.login_address)
        self.driver.set_window_size(1024,600)
        self.driver.maximize_window()
        time.sleep(1)
        #accept cookies
        self.driver.find_element_by_css_selector(".RnEpo button").click() #Yx5HN _4Yzd2 .HoLwm
        time.sleep(1)
        #enter inputs to login
        inputs = self.driver.find_elements_by_css_selector("._9GP1n input")
        time.sleep(1)
        inputs[0].send_keys(self.instagram_email)
        inputs[1].send_keys(self.instagram_password + Keys.ENTER)
        time.sleep(3)
        #do not save login info
        self.driver.find_element_by_css_selector(".cmbtv button").click()
        time.sleep(1)
        #turn off notifications
        self.driver.find_element_by_css_selector(".mt3GC .HoLwm").click()


    def find_followers(self):
        self.driver.get(self.similar_account)
        time.sleep(1)
        self.driver.find_element_by_css_selector(".k9GMp .Y8-fY a").click()
        time.sleep(3)
        # popup_body = self.driver.find_element_by_class_name("isgrP")
        scroll = 0
        while scroll < 10:
            popup_body = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup_body)
            scroll += 1
            time.sleep(1)
        button_list = self.driver.find_elements_by_css_selector(".isgrP button")
        return button_list
    def follow(self, button_list):
        for button in button_list:
            try:
                button.click()
                time.sleep(1.2)

            except ElementClickInterceptedException:
                self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]").click()


