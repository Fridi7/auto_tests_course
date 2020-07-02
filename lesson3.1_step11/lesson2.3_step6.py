import time
import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(int(x))

    t = browser.find_element_by_css_selector("#answer")
    t.send_keys(y)
    # checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    # checkbox.click()
    # radio = browser.find_element_by_css_selector("#robotsRule")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    # radio.click()
    button = browser.find_element_by_css_selector("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
