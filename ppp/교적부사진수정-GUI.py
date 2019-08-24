
# coding: utf-8

# In[4]:


from __future__ import print_function
import pickle
import os.path

from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from multiprocessing import Pool
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print(os.getcwd())

# 교육부 분반선택 
studentClassCode = {"교육부" : "100000000", "소년1부" : "110000000", "소년2부" : "120000000", "영아1부" : "130000000",                 "영아2부" : "140000000", "유년1부" : "150000000", "유년2부" : "160000000", "유아1부" : "170000000",                 "유아2부" : "180000000", "유치1부" : "190000000", "유치2부" : "200000000", "중등부" : "210000000",                "고등부" : "220000000", "초등1부" : "230000000", "초등2부" : "240000000", "영어아동부" : "250000000",                "휴직교사" : "260000000"}
print(studentClassCode.keys())
print("사용할 교육부서를 입력하세요.")
studentClassName = input()



# 웹페이지 로그인
driver = webdriver.Chrome("./chromedriver.exe")
site = "http://web.choongshin.or.kr/WebSchool/Default.aspx"
siteId = "황보라"
password = "bora9909"
driver.get(site)
element = WebDriverWait(driver,5).until(
         EC.element_to_be_clickable((By.ID, "ctl00_cph1_LoginMain1_txtLoginID")))
element.send_keys(siteId)
element = WebDriverWait(driver,5).until(
         EC.element_to_be_clickable((By.ID, "ctl00_cph1_LoginMain1_txtLoginPWD")))
element.send_keys(password)
element = WebDriverWait(driver,5).until(
         EC.element_to_be_clickable((By.ID, "ctl00_cph1_LoginMain1_imgBtnLogin")))
element.click()
alert = Alert(driver)
alert.accept()
driver.switch_to.frame("left")
element = WebDriverWait(driver,5).until(
         EC.element_to_be_clickable((By.XPATH, '//*[@id=' + '"' + studentClassCode[studentClassName] + '"' + ']/a')))
element.click()
driver.switch_to_default_content()
driver.switch_to.frame("right") 
checkbox = True
result = WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "imgCursor")))
page = WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "PageNumber")))
page.append("")
#사진넣는작업
for p in range(0, len(page)+1) :
    code = 0
    for i in result :
        picHave = False
        driver.switch_to_default_content()
        driver.switch_to.frame("right") 
        imgId = "ctl00_cph1_PersonListStudent_tabConSch_tabPnSchMain_lvMain_ctrl" + str(code) + "_imgP"

        student = WebDriverWait(driver,5).until(
            EC.element_to_be_clickable((By.ID, imgId)))
        student.click()

        driver.switch_to_window(driver.window_handles[1])
        element = WebDriverWait(driver,5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_cph1_PersonModifyStudent1_txtName")))
        name = element.get_attribute("value")
        for file in os.listdir(os.getcwd() + "/초등1부얼굴사진"):
            if file.endswith(name + ".jpg"):
                picHave = True
        # 사진이 없는 경우
        if picHave == False : 
            driver.switch_to_window(driver.window_handles[1])
            driver.close()
            driver.switch_to_window(driver.window_handles[0])
            code = code + 1
            continue
        
        element = WebDriverWait(driver,5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_cph1_PersonModifyStudent1_tabPicture_tabPicture1_btnEditPic")))
        element.click()
        driver.implicitly_wait(1)
        driver.switch_to_window(driver.window_handles[2])
        element = WebDriverWait(driver,5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_cph1_fuFile")))
        element.send_keys(os.getcwd() + "/초등1부얼굴사진/" + name + ".jpg" )
        if checkbox == True :
            element = WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.ID, "ctl00_cph1_cbUseCrop")))
            element.click()
            checkbox = False
        element = WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.ID, "ctl00_cph1_imgWrite")))
        element.click()
        alert = Alert(driver)
        alert.accept()
        driver.switch_to_window(driver.window_handles[1])
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        code = code + 1
    driver.switch_to_default_content()
    driver.switch_to.frame("right") 
    pp = WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "PageNumber")))
    pp[p].click()
    time.sleep(3)


