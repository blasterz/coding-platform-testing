import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://test.algocademy.com/")
list = []
list1 = []
# cumparaturi = driver.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
# pt css selectors am folosit tagname.className
time.sleep(4)
cumparaturi = driver.find_elements_by_xpath("//div[@class='products']/div")
# //div[@class='products']/div - produsele noastre sunt un copil al clasei mare products, de aceea punem div la sf
count = len(cumparaturi)
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4
# in python, putem merge si inapoi, la parent, la parentul parentului si apoi iar in jos
#pt a afisa si numele casutelor pe care le selectam automat cu python
#intoducem in interatia de mai jos
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list)
# buttons deja are partea asta "//div[@class='product-action']/button"
#print(button.find_element_by_xpath("parent::div/parent::div/h4").text) - printeaza denumirea legumelor
#adaugam in lista mai sus creata, elementele de la (button.find_element_by_xpath("parent::div/parent::div/h4")


driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
legume = driver.find_elements_by_css_selector("p.product-name")
for item in legume:
    list1.append(item.text)
print(list1)
assert list == list1
# asta spune ca asteapta pana cand apare clasa "promocode"
# in loc de By.CLASS_NAME puteam sa adaug si By.CSS_SELECTOR
# in exemplu nostru am pus class name pt ca asa era locater-ul
# By trebuie importat
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element_by_class_name("promoInfo").text)

totalAmount = driver.find_element_by_css_selector(".totAmt").text
discountedAmount = driver.find_element_by_css_selector(".discountAmt").text

assert float(discountedAmount) < float(totalAmount)
#trebuie sa transformam in text, adica string si apoi ca sa le comparam, trebuie transformate in float(daca au virgula)
#si integer daca nu are virgula
total = 0
totalProdus = driver.find_elements_by_xpath("//tr/td[5]/p")
for produs in totalProdus:
    total = total + int(produs.text)
print(total)
totalAmount = int(driver.find_element_by_css_selector(".totAmt").text)
assert total == totalAmount

"""exercitiu:
Sa verific daca search merge corect
atunci cand introduc ber, sa fie afisate 3 produse x y z si sa le compar cu o alta lista """
