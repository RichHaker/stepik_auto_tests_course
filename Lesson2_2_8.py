import math, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
message = browser.find_element(By.ID, "book")
message.click()


browser.execute_script("window.scrollBy(0, 100);")
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(int(x))
element1 = browser.find_element(By.CSS_SELECTOR, "#answer")
element1.send_keys(y)

option2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
option2.click()


#assert "successful" in message.text
time.sleep(5)
browser.quit()
