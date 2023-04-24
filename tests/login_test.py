from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

login_url = "http://127.0.0.1:50000/auth/login"
home_url = "http://127.0.0.1:50000/"
signup_url = "http://127.0.0.1:50000/auth/signup"
profile_url = "http://127.0.0.1:50000/profile"
driver = webdriver.Chrome()

def test_successful_login():
    # Truy cập đến địa chỉ đăng nhập
    driver.get(login_url)
    driver.maximize_window()
    time.sleep(1)

    # Khởi tạo các element
    username = driver.find_element(By.XPATH,"//input[@name='username']")
    password = driver.find_element(By.NAME,"password")
    roleUser = driver.find_element(By.NAME,"user")
    roleAdmin = driver.find_element(By.NAME,"admin")
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Nhập username, password, chọn role, bấm đăng nhập
    username.send_keys('ngocduy')
    time.sleep(1)
    password.send_keys('123Duy')
    time.sleep(1)
    roleAdmin.click()
    time.sleep(1)
    submit.click()
    time.sleep(1)

    # Kiểm tra nếu đăng nhập thành công thì url hiện tại sẽ là url của trang dashboard
    assert driver.current_url == home_url

    # menu_btn = driver.find_element(By.XPATH,"//button[@class='main-btn primary-btn btn-hover']")
    # time.sleep(2)
    # menu_btn.click()
    
    
    logout_btn = driver.find_element(By.XPATH,"//div[@id='app']//div[@class='promo-box']//a[@class='main-btn primary-btn btn-hover']")
    #logout_btn = driver.find_element(By.NAME,"logout-btn")
    time.sleep(1)
    logout_btn.click()
    time.sleep(1)

    driver.implicitly_wait(10)
    #driver.quit()


def test_no_credentials_login():
    all_windows = driver.window_handles

    current_window = driver.current_window_handle

    driver.switch_to.window(all_windows[1])
    driver.close()
    time.sleep(1)

    driver.switch_to.window(current_window)

    driver.get(login_url)
    
    

    # Khởi tạo các element
    username = driver.find_element(By.XPATH,"//input[@name='username']")
    password = driver.find_element(By.NAME,"password")
    roleUser = driver.find_element(By.NAME,"user")
    roleAdmin = driver.find_element(By.NAME,"admin")
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Gửi dữ liệu
    username.send_keys('')
    time.sleep(1)
    password.send_keys('')
    time.sleep(1)

    # Bấm login
    submit.click()
    alert_message1 = driver.find_element(By.XPATH,"//span[@id='errorMsg1']")
    alert_message2 = driver.find_element(By.XPATH,"//span[@id='errorMsg2']")
    time.sleep(3)


    # Test
    assert "tên đăng nhập" in alert_message1.text and "mật khẩu" in alert_message2.text

    driver.implicitly_wait(10)
    time.sleep(3)
    driver.quit()

def test_role_isChecked():
    driver.get(login_url)

    # Khởi tạo các element
    username = driver.find_element(By.XPATH,"//input[@name='username']")
    password = driver.find_element(By.NAME,"password")
    roleUser = driver.find_element(By.NAME,"user")
    roleAdmin = driver.find_element(By.NAME,"admin")
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Gửi dữ liệu
    username.send_keys('abc')
    time.sleep(1)
    password.send_keys('abc')
    time.sleep(1)

    # Bấm login
    submit.click()

    # Nếu có thông báo lỗi thì lưu bằng một element
    alert_role_isChecked = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")

    # Test
    assert "checkbox Role" in alert_role_isChecked.text

    driver.implicitly_wait(10)
    time.sleep(3)
    #driver.quit()

def test_invalid_credentials_login():
    driver.get(login_url)

    # Khởi tạo các element
    username = driver.find_element(By.XPATH,"//input[@name='username']")
    password = driver.find_element(By.NAME,"password")
    roleUser = driver.find_element(By.NAME,"user")
    roleAdmin = driver.find_element(By.NAME,"admin")
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Gửi dữ liệu
    username.send_keys('abc')
    time.sleep(1)
    password.send_keys('abc')
    time.sleep(1)
    roleAdmin.click()

    # Bấm login
    submit.click()

    # Nếu có thông báo lỗi thì lưu bằng một element
    alert_invalid_credentials = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")

    # Test
    assert "Invalid" in alert_invalid_credentials.text

    driver.implicitly_wait(10)
    time.sleep(3)
    #driver.quit()

def test_access_denied():
    driver.get(login_url)

    # Khởi tạo các element
    username = driver.find_element(By.XPATH,"//input[@name='username']")
    password = driver.find_element(By.NAME,"password")
    roleUser = driver.find_element(By.NAME,"user")
    roleAdmin = driver.find_element(By.NAME,"admin")
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Gửi dữ liệu
    username.send_keys('ngocduy1')
    time.sleep(1)
    password.send_keys('123Duy')
    time.sleep(1)
    roleUser.click()
    time.sleep(1)

    # Bấm login
    submit.click()

    # Nếu có thông báo lỗi thì lưu bằng một element
    alert_access_denied = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")

    # Test
    assert "Access" in alert_access_denied.text

    driver.implicitly_wait(10)
    time.sleep(3)
    driver.quit()



