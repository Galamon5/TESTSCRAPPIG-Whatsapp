
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Let's use Firefox as our browser
web = webdriver.Chrome('C:/Users/Galamon5/Documents/chromedriver')
web.get('http://web.whatsapp.com')
input()

#Replace Mr Kelvin with the name of your friend to spam
elem = web.find_element_by_xpath('//span[contains(text(),"Heber")]')
elem.click()
elem1 = web.find_elements_by_xpath("//div[@class='_2S1VP copyable-text selectable-text']")
i=0
for i in range(10):
    elem1[0].send_keys('hahahahahahaha')
elem1[0].send_keys(Keys.RETURN)
