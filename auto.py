from selenium import webdriver
import time
import re
#Ponta账户
user=""
pw=""
#Line账户
line=""
linepw=""
#加载环境
driver = webdriver.Chrome()
#LinePoint登录
driver.get("https://points.line.me/pointcode/")
ele=driver.find_element_by_name("pincode")
ele.send_keys(1)
ele=driver.find_element_by_class_name("MdBtn01")
ele.click()
ele=driver.find_element_by_name("tid")
ele.send_keys(line)
ele=driver.find_element_by_name("tpasswd")
ele.send_keys(linepw)
ele=driver.find_element_by_class_name("MdBtn03Login")
ele.click()
time.sleep(2)
#Ponta登陆
driver.get('https://spend.ponta.jp/Form/Order/CartList.aspx?shop=0&pid=LN-000001&vid=LN-000001&ckbn=1&prdcnt=1')
driver.execute_script('javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions("ctl00$ContentPlaceHolder1$lbNext", "", true, "OrderShipping", "", false, true))')
time.sleep(1)
ele=driver.find_element_by_class_name("rid-login-box")
ele.click()
time.sleep(1)
ele=driver.find_element_by_id("form01_text01")
ele.send_keys(user)
ele=driver.find_element_by_id("form01_text02")
ele.send_keys(pw)
ele=driver.find_element_by_class_name("btnAction01_LV01Lg")
ele.click()
time.sleep(30)
#循环100次
count = 0
while (count < 100):
    driver.get('https://spend.ponta.jp/Form/Order/CartList.aspx?shop=0&pid=LN-000001&vid=LN-000001&ckbn=1&prdcnt=1')
    driver.execute_script('javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions("ctl00$ContentPlaceHolder1$lbNext", "", true, "OrderShipping", "", false, true))')
    time.sleep(1)

    ele=driver.find_element_by_class_name("rid-login-box")
    ele.click()

    time.sleep(1)
    ele=driver.find_element_by_name("passwd")
    ele.send_keys(pw)
    ele=driver.find_element_by_class_name("btnAction01_LV01Lg")
    ele.click()

    driver.execute_script('javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions("ctl00$ContentPlaceHolder1$lbNext", "", true, "OrderShipping", "", false, true))')
    driver.execute_script('javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions("ctl00$ContentPlaceHolder1$lbNext", "", true, "OrderShipping", "", false, true))')
    ele=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lbComplete2")
    ele.click()
    code = driver.page_source
    code = re.findall(r'\d{16}(?=<)',code)
    #交换Point
    driver.get("https://points.line.me/pointcode/")
    ele=driver.find_element_by_id("pincode")
    ele.send_keys(code[0])
    ele=driver.find_element_by_class_name("MdBtn01")
    ele.click()  
    
    count = count + 1
