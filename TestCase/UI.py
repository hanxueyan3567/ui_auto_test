from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

def input_demo():
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    # driver.get  打开一个指定网页
    driver.get('http://192.168.60.146:8080/demo1.html')
    # 等待几秒
    # time.sleep(5)
    # 1.定位元素 通过 xpath 去定位
    input_el = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/input")
    # 输入值
    input_el.send_keys("哈哈")
    #clear 清除
    input_el.clear()

def input_demo1():

    # 2.定位元素 通过ID 去定位
    file_el = driver.find_element_by_id('file1')
    file_el.send_keys('C:/Users/Administrator/Pictures/数据库-5.14')

    # 3.定位元素 通过name去定位
    radio_els = driver.find_elements_by_name('radio')
    print(type(radio_els))

    # 操作元素 ,点击
    radio_els[0].click()
    time.sleep(3)
    radio_els[1].click()
    time.sleep(3)

def input_demo2():
    checkbox_els = driver.find_elements_by_class_name('checkbox')
    #多选框 按钮
    checkbox_els[0].click()
    time.sleep(1)

    checkbox_els[1].click()
    time.sleep(1)

    checkbox_els[2].click()
    time.sleep(1)

def input_demo3():
    button_el = driver.find_element_by_xpath('//input[@value="普通按钮"]')  #相对路径
    button_el.click()
    time.sleep(1)
    # 确认弹框
    driver.switch_to.alert.accept()
    time.sleep(1)
    # 取消弹框
    # driver.switch_to.alert.dismiss()
    # time.sleep(5)


def input_demo4():
    # 下拉框 选项
    select_el = driver.find_element_by_css_selector(
        'body > table > tbody > tr:nth-child(12) > td:nth-child(2) > select')

    s = Select(select_el)
    # 通过索引选择
    s.select_by_index(0)
    time.sleep(2)
    # 通过value属性 选择
    s.select_by_value('z2')
    time.sleep(2)
    s.select_by_visible_text('周龙3')
    time.sleep(2)


if __name__ == '__main__':

    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    #driver.get  打开一个指定网页
    driver.get('http://192.168.60.146:8080/demo1.html')





    pass_el = driver.find_element_by_xpath('//input[@type="password"]')
    pass_el.send_keys('123456')
    time.sleep(3)


    #定位超链接
    #全名 访问
    driver.find_element_by_link_text('当当').click()
    time.sleep(3)
    driver.back()
    time.sleep(1)
    #局部 访问
    driver.find_element_by_partial_link_text('问问').click()
    time.sleep(3)
    driver.back()
    time.sleep(1)
    driver.forward()
    time.sleep(3)

    driver.refresh()
    time.sleep(2)




    # 关闭浏览器
    driver.quit()