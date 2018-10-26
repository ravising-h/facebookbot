from selenium import webdriver
import os
from time import sleep
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get("https://www.facebook.com/login.php")
browser.find_element_by_id('email').send_keys('')
browser.find_element_by_id('pass').send_keys('')
browser.find_element_by_id('loginbutton').click()
browser.find_element_by_xpath("//textarea[@name='xhpc_message']").send_keys(open('caption.txt', 'r').read())
browser.find_element_by_class_name("_5xmp").click()
os.chdir(r'C:\Users\RAVISINGH\Downloads\Python')
os.system('sc.exe')
sleep(2)
browser.find_element_by_xpath("//button[@class='_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft']").click()
sleep(9)
browser.get("https://www.facebook.com/ieee.mait/")
browser.find_element_by_class_name("likeButton ").click()
