from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

login_url = "http://127.0.0.1:50000/auth/login"
home_url = "http://127.0.0.1:50000/"
signup_url = "http://127.0.0.1:50000/auth/signup"
profile_url = "http://127.0.0.1:50000/profile"
driver = webdriver.Chrome()

def test_successful_get_password():
    #Truy cập đến địa chỉ đăng nhập
    driver.get(login_url)
    driver.maximize_window()
    time.sleep(1)

    # Khởi tạo các element
    forgot_password_redirect = driver.find_element(By.XPATH,"//a[@href='/auth/forgot-password']")

    
    forgot_password_redirect.click()
    time.sleep(1)
    
    email = driver.find_element(By.NAME,"email")
    #submit_btn = driver.find_element(By.XPATH,"//button[@type='submit']")

    email.send_keys("nguyenngocduy12a2@gmail.com")
    email.send_keys(Keys.RETURN)
    time.sleep(25)

    new_password = driver.find_element(By.NAME,"new_password")
    confirm_password = driver.find_element(By.NAME,"confirm_password")

    new_password.send_keys("1902Duy")
    time.sleep(1)
    confirm_password.send_keys("1902Duy")
    time.sleep(1)
    confirm_password.send_keys(Keys.RETURN)
    time.sleep(3)

    relogin_href = driver.find_element(By.XPATH,"//a[@href='/auth/form_login']")
    relogin_href.click()
    time.sleep(1)
    username = driver.find_element(By.XPATH,"//input[@name='username']")
    password = driver.find_element(By.NAME,"password")
    roleUser = driver.find_element(By.NAME,"user")

    username.send_keys("ngocduy")
    password.send_keys("1902Duy")
    roleUser.click()
    roleUser.send_keys(Keys.RETURN)

    assert driver.current_url == home_url

    time.sleep(5)
    driver.implicitly_wait(10)
    driver.quit()