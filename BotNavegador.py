from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
import time
import random 


class BorrarCacheBot:
    def __init__ (self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
    
    def searchPage(self):
        driver = self.driver
        driver.get('http://www.google.com/')
        time.sleep(3)
        search_box = driver.find_element_by_name('q')
        search  = 'Facebook'
        self.digitarComoPersona(search, search_box)
        search_box.submit()
        time.sleep(3)
        results = driver.find_elements_by_css_selector('div.g')
        link = results[0].find_element_by_tag_name("a")
        href = link.get_attribute("href")
        driver.get(href)
        time.sleep(10)
        self.delete_cache()
            

    @staticmethod
    def digitarComoPersona(frase, donde_digitar):
        for letra in frase:
            donde_digitar.send_keys(letra)
            time.sleep(random.randint(1,2)/30)

    def delete_cache(self):
        driver = self.driver
        actions = ActionChains(driver) 
        actions.send_keys(Keys.F12)
        actions.perform()
        driver.execute_script("window.open('');")
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)
        driver.get('chrome://settings/clearBrowserData')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB * 2 + Keys.ENTER + Keys.DOWN * 4 + Keys.ENTER)
        actions.perform()
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB * 5 + Keys.ENTER)
        actions.perform()
        time.sleep(10)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        driver.close()
        time.sleep(5)


for i in range (9999999):
    try: 
        Bot = BorrarCacheBot()
        Bot.searchPage()
        del Bot
        print(i)
    except Exception as e:
        print(e)
        print(i)

