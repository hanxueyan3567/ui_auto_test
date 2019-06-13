from selenium import webdriver
import time
from selenium.webdriver.support.select import Select





if __name__ == '__main__':
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')

    driver.get('http://192.168.60.146:8080/demo1.html')
    input_el = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/input')
    input_el.send_keys('你好')
    time.sleep(2)

    file_el = driver.find_element_by_id('file1')
    file_el.send_keys('C:/Users/Administrator/Pictures/5.28-3.png')
    time.sleep(2)

    radio_el = driver.find_elements_by_name('radio')
    radio_el[0].click()
    time.sleep(1)
    radio_el[1].click()
    time.sleep(1)

    