from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

mydriver = webdriver.Firefox()
#chromedriver = 'C:\Users\Gajendra\Downloads\chromedriver_win32\chromedriver.exe'
#mydriver = webdriver.Chrome(chromedriver)
mydriver.get("https://www.facebook.com/login")
username = "xyz"
password = "1234"


mydriver.maximize_window()

wait = WebDriverWait(mydriver, 10)
element = wait.until(EC.presence_of_element_located((By.ID,'email')))
element.send_keys(username)

Pass = mydriver.find_element_by_id("pass")
Pass.send_keys(password)

btnLogin = wait.until(EC.element_to_be_clickable((By.ID,'loginbutton')))
btnLogin.send_keys(Keys.RETURN)
time.sleep(5)
mydriver.get("https://www.facebook.com/messages/")

print "opened msgs"


try:
	wait = WebDriverWait(mydriver, 500)
	element10 = wait.until(EC.presence_of_element_located((By.ID,"wmMasterViewThreadlist")))
	print element10.text
	print "for loop for li elements begins"
	for str10 in element10.find_elements_by_tag_name("li"):
		#print str10.text
		
		element12 = (str10.find_element_by_xpath("//div/a")).get_attribute("href")
		
		print "element12=" + element12
		str10.click()
		#element12.click()
	
		try:
			wait = WebDriverWait(mydriver, 500)
			elem = wait.until(EC.presence_of_element_located((By.ID,'webMessengerRecentMessages')))
			elem1 = elem.find_elements_by_tag_name("li")
			for str1 in elem1:
				try:
					str2 = str1.find_element_by_class_name("timestamp")
					print str2.text
				except NoSuchElementException:
					print ""
				try:
					str2 = str1.find_element_by_css_selector("img")
					print str2.get_attribute("alt")
				except NoSuchElementException:
					print ""
				try:
					str2 = str1.find_elements_by_css_selector('._3hi.clearfix')
					for str3 in str2:
						element = str3.find_elements_by_css_selector(".null>p")
						for str4 in element:
							print (str4.text).encode('utf-8')
					
				except NoSuchElementException:
					print ""
				
		except TimeoutException:
			print "TimeoutException raised in inner loop"
			break
				
except TimeoutException:		
	print "TimeoutException raised in outer loop"
