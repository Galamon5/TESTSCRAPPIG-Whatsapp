# TESTSCRAPPIG-Whatsapp

Send Multiple Message through web whatsapp

### Installation

* Python 2 or later
* Pip
* Selenium
* WebDriver for your browser
* be Patient.exe

### Usage

This are based on html so you need knodladge about it

_First you need to describe where is your webdriver.S_  
```python 
web = webdriver.Chrome('C:/Users/Galamon5/Documents/chromedriver')
```  
_You can define it on your Environment Variables._  

_Then specify the person that you want to send the message._  
```python 
elem = web.find_element_by_xpath('//span[contains(text(),"Heber")]')
```  
