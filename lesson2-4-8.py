from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math
import os

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    if WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")):
        sub = browser.find_element_by_xpath('//button[text()="Book"]')
        sub.click()
        print("100")

        x_elem = browser.find_element_by_id("input_value")
        num1 = int(x_elem.text)
        ans = str(math.log(abs(12 * math.sin(num1))))

        x_elem = browser.find_element_by_id("answer")
        x_elem.send_keys(ans)

        sub = browser.find_element_by_xpath('//button[text()="Submit"]')
        browser.execute_script("return arguments[0].scrollIntoView(true);", sub)
        sub.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # driver.close()
# не забываем оставить пустую строку в конце файла