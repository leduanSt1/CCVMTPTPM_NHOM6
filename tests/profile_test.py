from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

login_url = "http://127.0.0.1:50000/auth/login"
home_url = "http://127.0.0.1:50000/"
signup_url = "http://127.0.0.1:50000/auth/signup"
profile_url = "http://127.0.0.1:50000/profile"
redirect_login_url = "http://localhost:50000/auth/login?next=%2Fprofile"
driver = webdriver.Chrome()

def test_view_profile():
    # driver.get(login_url)
    driver.get(profile_url)

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

    # Thực hiện thao tác view profile
    img_profile = driver.find_element(By.XPATH, "//img[@src='/static/images/profile/profile-image.png']")
    img_profile.click()
    time.sleep(1)
    view_profile_label = driver.find_element(By.XPATH, "//a[@href='/profile']")
    view_profile_label.click()
    time.sleep(1)

    # Kiểm tra có truy cập được đến trang profile hay không
    assert driver.current_url == profile_url
    time.sleep(3)
    driver.quit()