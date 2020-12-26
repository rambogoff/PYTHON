from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

path = "C:/Users/ramazan.urkmez/Desktop/VeriCekme/chromedriver/chromedriver.exe"
browser = webdriver.Chrome(path)


browser.get("https://www.linkedin.com/")

browser.fullscreen_window()
time.sleep(5)

login = browser.find_element_by_xpath("/html/body/nav/div/a[2]")
login.click()
time.sleep(5)

email = browser.find_element_by_xpath("//*[@id='username']")
password = browser.find_element_by_xpath("//*[@id='password']")

email.send_keys("**************")
password.send_keys("***********")

login_button = browser.find_element_by_xpath("//*[@id='app__container']/main/div[2]/form/div[3]/button")
login_button.click()

time.sleep(5)

search_bar = browser.find_element_by_xpath("//*[@id='ember20']/input")
search_bar.send_keys("#python")
search_bar.send_keys(Keys.RETURN)
time.sleep(10)


contacts = browser.find_element_by_xpath("//*[@id='ember26']/svg")
contacts.click()
time.sleep(5)

contact_button = browser.find_element_by_xpath("//*[@id='ember3695']/div/div[1]")
contact_button.click()
time.sleep(5)

for i in range(1,3):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)

followers = browser.find_element_by_xpath("//*[@id='ember4592']/span[2]")
fallowerList=[]

for follower in followers:
    fallowerList.append(follower.text)

with open ("follower.txt","w",encoding = "UTF-8") as file:
    for follower in fallowerList:
        file.write(follower + "/n")
time.sleep(5)

browser.quit()