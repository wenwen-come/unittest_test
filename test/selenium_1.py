from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://baidu.com')
driver.find_element_by_id('kw').send_keys('虚竹')
driver.find_element_by_id('su').click()
