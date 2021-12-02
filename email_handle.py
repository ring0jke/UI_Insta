from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options

'''
Start:
GetAvaliableEmail->Email.Ready+
(Enter Name.Login.Email.Ready.Password)
Load UI_InitialRegistration > Enter initial Data
CheckMail>CodeReady
Load UI_MailCheck(Enters EmailCode,Click Next,Await 5 secs,Check Image for Profile Logo)
'''

def getInstVeriCode(mailName, domain, driver):
    INST_CODE = 'https://email-fake.com/' + domain + '/' + mailName

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(INST_CODE)

    # button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[1]/a/button").click()
    # time.sleep(3)
    t = driver.title

    while True:
        if t[:4] == "Fake":
            driver.refresh()
            t = driver.title
            print(t)
            time.sleep(1)
        else:
            break

    # code = browser.find_element_by_xpath("//*[@id='email-table']/div[2]/div[1]/div/h1").text
    # code = code.replace("is your Instagram code", "")
    code = t[:6]
    driver.switch_to.window(driver.window_handles[0])
    return code


def getFakeMail():
    url = 'https://email-fake.com/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    mail = soup.find_all("span", {"id": "email_ch_text"})
    return mail[0].contents


'''
check = getFakeMail()
print(check)
fMail = check[0].split("@")
mailName = fMail[0]
domain = fMail[1]
print(mailName)
print(domain)
input()

#driver= webdriver(options=options, executable_path=r"/Users/kappa/PycharmProjects/UI_Insta/chromedriver") #File Chromedriver
#getInstVeriCode()
driver = webdriver.Chrome('/Users/kappa/PycharmProjects/UI_Insta/chromedriver')
code = getInstVeriCode(mailName,domain,driver)
print(code)

'''


