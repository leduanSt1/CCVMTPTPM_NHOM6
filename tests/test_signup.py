from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import unittest


signup_url = "http://127.0.0.1:50000/auth/signup"
driver = webdriver.Chrome()

def test_signup_success():
    driver.maximize_window()
    driver.get(signup_url)
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    fullname = driver.find_element(By.NAME, "fullname")
    age = driver.find_element(By.NAME, "age")
    address = driver.find_element(By.NAME, "address")
    roleNormal = driver.find_element(By.NAME, "normal")
    roleAdmin = driver.find_element(By.NAME,"admin") 
    submit = driver.find_element(By.NAME, "SignUp-btn")
        
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    username.send_keys("test_user12")
    time.sleep(1)
    password.send_keys("Pswd123")
    time.sleep(1)
    fullname.send_keys("Test User")
    time.sleep(1)
    age.send_keys("20")
    time.sleep(1)
    address.send_keys("Test Address")
    time.sleep(1)
    roleNormal.click()
    
    time.sleep(1)
    submit.click()
    #Nếu đăng kí thành công thì có thông báo success
    alert_checkCredentials = driver.find_element(By.NAME, "signup_success")
    assert alert_checkCredentials is not None
    driver.implicitly_wait(10)
    time.sleep(1)
    #driver.quit()

def test_signup_empty_fields():
    driver.get(signup_url)
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    fullname = driver.find_element(By.NAME, "fullname")
    age = driver.find_element(By.NAME, "age")
    address = driver.find_element(By.NAME, "address")
    roleNormal = driver.find_element(By.NAME, "normal")
    roleAdmin = driver.find_element(By.NAME,"admin")
    submit = driver.find_element(By.NAME, "SignUp-btn")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    username.send_keys("")
    time.sleep(1)
    password.send_keys("")
    time.sleep(1)
    fullname.send_keys("")
    time.sleep(1)
    age.send_keys("abc")
    time.sleep(1)
    address.send_keys("")
    time.sleep(1)
    roleAdmin.click()
    time.sleep(1)
    submit.click()
    # Assert that the error message is displayed on the page after unsuccessful registration
    alert_checkCredentials = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
    assert "Vui lòng nhập tên đăng nhập" in alert_checkCredentials.text
    driver.implicitly_wait(10)
    time.sleep(1)
def test_signup_empty_username():
    driver.get(signup_url)
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    fullname = driver.find_element(By.NAME, "fullname")
    age = driver.find_element(By.NAME, "age")
    address = driver.find_element(By.NAME, "address")
    roleNormal = driver.find_element(By.NAME, "normal")
    roleAdmin = driver.find_element(By.NAME,"admin")
    submit = driver.find_element(By.NAME, "SignUp-btn")
    
    time.sleep(1)
    username.send_keys("")
    time.sleep(1)
    password.send_keys("Duan210")
    time.sleep(1)
    fullname.send_keys("Le Duan")
    time.sleep(1)
    age.send_keys("21")
    time.sleep(1)
    address.send_keys("HCM")
    time.sleep(1)
    roleAdmin.click()
    time.sleep(1)
    submit.click()
    # Assert that the error message is displayed on the page after unsuccessful registration
    alert_checkCredentials = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
    assert"Vui lòng nhập tên đăng nhập" in alert_checkCredentials.text
    driver.implicitly_wait(10)
    time.sleep(1)
def test_signup_empty_age():
    driver.get(signup_url)
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    fullname = driver.find_element(By.NAME, "fullname")
    age = driver.find_element(By.NAME, "age")
    address = driver.find_element(By.NAME, "address")
    roleNormal = driver.find_element(By.NAME, "normal")
    roleAdmin = driver.find_element(By.NAME,"admin")
    submit = driver.find_element(By.NAME, "SignUp-btn")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    username.send_keys("duan123")
    time.sleep(1)
    password.send_keys("Duan210")
    time.sleep(1)
    fullname.send_keys("Le Duan")
    time.sleep(1)
    age.send_keys("")
    time.sleep(1)
    address.send_keys("HCM")
    time.sleep(1)
    roleAdmin.click()
    time.sleep(1)
    submit.click()
    # Assert that the error message is displayed on the page after unsuccessful registration
    alert_checkCredentials = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
    assert "Vui lòng nhập tuổi" in alert_checkCredentials.text
    driver.implicitly_wait(10)
    time.sleep(1)
def test_signup_empty_address():
    driver.get(signup_url)
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    fullname = driver.find_element(By.NAME, "fullname")
    age = driver.find_element(By.NAME, "age")
    address = driver.find_element(By.NAME, "address")
    roleNormal = driver.find_element(By.NAME, "normal")
    roleAdmin = driver.find_element(By.NAME,"admin")
    submit = driver.find_element(By.NAME, "SignUp-btn")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    username.send_keys("duan123")
    time.sleep(1)
    password.send_keys("Duan210")
    time.sleep(1)
    fullname.send_keys("Le Duan")
    time.sleep(1)
    age.send_keys("21")
    time.sleep(1)
    address.send_keys("")
    time.sleep(1)
    roleAdmin.click()
    time.sleep(1)
    submit.click()
    # Assert that the error message is displayed on the page after unsuccessful registration
    alert_checkCredentials = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
    assert "Vui lòng nhập địa chỉ" in alert_checkCredentials.text
    driver.implicitly_wait(10)
    time.sleep(1)
def test_signup_duplicate_username():
    driver.get(signup_url)
    username = driver.find_element(By.NAME,"username")
    password = driver.find_element(By.NAME,"password")
    fullname = driver.find_element(By.NAME,"fullname")
    age = driver.find_element(By.NAME,"age")
    address = driver.find_element(By.NAME,"address")
    roleNormal = driver.find_element(By.NAME,"normal")
    roleAdmin = driver.find_element(By.NAME,"admin")
    submit = driver.find_element(By.NAME, "SignUp-btn")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    username.send_keys('leduan1')
    time.sleep(1)
    password.send_keys('Duan123@')
    time.sleep(1)
    fullname.send_keys('Le Quang Duan')
    time.sleep(1)
    age.send_keys('20')
    time.sleep(1)
    address.send_keys('TPHCM')
    time.sleep(1)
    roleNormal.click()
    time.sleep(1)
    submit.click()

    alert_checkCredentials = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
    assert "tồn tại" in alert_checkCredentials.text
    driver.implicitly_wait(10)
    time.sleep(1)
def test_signup_weak_password():
    driver.get(signup_url)
    username = driver.find_element(By.NAME,"username")
    password = driver.find_element(By.NAME,"password")
    fullname = driver.find_element(By.NAME,"fullname")
    age = driver.find_element(By.NAME,"age")
    address = driver.find_element(By.NAME,"address")
    roleNormal = driver.find_element(By.NAME,"normal")
    submit = driver.find_element(By.NAME, "SignUp-btn")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Điền thông tin đăng ký vào các trường tương ứng, sử dụng mật khẩu yếu
    time.sleep(1)
    username.send_keys('user123')
    time.sleep(1)
    # Password yếu do không có đủ số, chữ thường, chữ hoa
    password.send_keys('password')
    time.sleep(1)
    fullname.send_keys('User')
    time.sleep(1)
    age.send_keys('30')
    time.sleep(1)
    address.send_keys('HCM')
    time.sleep(1)
    roleNormal.click()
    time.sleep(1)
    submit.click()

    # Kiểm tra xem có thông báo lỗi nào xuất hiện không Vui lòng nhập mật khẩu
    alert_danger = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
    assert "Mật khẩu phải chứa" in alert_danger.text
    driver.implicitly_wait(10)
    time.sleep(1)
def test_signup_empty_password():
    driver.get(signup_url)
    username = driver.find_element(By.NAME,"username")
    password = driver.find_element(By.NAME,"password")
    fullname = driver.find_element(By.NAME,"fullname")
    age = driver.find_element(By.NAME,"age")
    address = driver.find_element(By.NAME,"address")
    roleNormal = driver.find_element(By.NAME,"normal")
    submit = driver.find_element(By.NAME, "SignUp-btn")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Điền thông tin đăng ký vào các trường tương ứng, sử dụng mật khẩu yếu
    time.sleep(1)
    username.send_keys('user123')
    time.sleep(1)
    # Password trống
    password.send_keys('')
    time.sleep(1)
    fullname.send_keys('User')
    time.sleep(1)
    age.send_keys('30')
    time.sleep(1)
    address.send_keys('HCM')
    time.sleep(1)
    roleNormal.click()
    time.sleep(1)
    submit.click()

    # Kiểm tra xem có thông báo lỗi nào xuất hiện không 
    alert_danger = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
    assert "Vui lòng nhập mật khẩu" in alert_danger.text
    driver.implicitly_wait(10)
    time.sleep(1)
def test_signup_short_password():
    driver.get(signup_url)
    username = driver.find_element(By.NAME,"username")
    password = driver.find_element(By.NAME,"password")
    fullname = driver.find_element(By.NAME,"fullname")
    age = driver.find_element(By.NAME,"age")
    address = driver.find_element(By.NAME,"address")
    roleNormal = driver.find_element(By.NAME,"normal")
    submit = driver.find_element(By.NAME, "SignUp-btn")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Điền thông tin đăng ký vào các trường tương ứng, sử dụng mật khẩu yếu
    time.sleep(1)
    username.send_keys('user123')
    time.sleep(1)
    password.send_keys('pswd')
    time.sleep(1)
    fullname.send_keys('User')
    time.sleep(1)
    age.send_keys('30')
    time.sleep(1)
    address.send_keys('HCM')
    time.sleep(1)
    roleNormal.click()
    time.sleep(1)
    submit.click()

    # Kiểm tra xem có thông báo lỗi nào xuất hiện không
    alert_danger = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
    assert "Mật khẩu phải từ 6 đến 8 ký tự" in alert_danger.text
    driver.implicitly_wait(10)
    time.sleep(1)
    driver.quit()
