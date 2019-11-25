from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

FILEPATH = 'E-mails'
FILEPATH2= 'Pwned'
driver.get(url="https://haveibeenpwned.com")

def insere(driver, mail):
    driver.find_element_by_class_name("form-control").send_keys(mail)
    sleep(0.3)
    driver.find_element_by_id("searchPwnage").click()
    driver.find_element_by_class_name("form-control").clear()
    if "Oh no — pwned!" in driver.page_source:
        print('Found it!', mail)
    else:
        print('Good news — no pwnage found!')


fopen = open(FILEPATH)
lin = fopen.readline()
print(lin)
pwds = lin.split(",")
for p in pwds:
    sleep(1)
    insere(driver, p)
    sleep(1)