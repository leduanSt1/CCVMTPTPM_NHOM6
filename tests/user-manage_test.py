from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import psycopg2
import time

ec2_url = "https://ec2-3-80-82-133.compute-1.amazonaws.com/"

login_url = "http://127.0.0.1:50000/auth/login"
home_url = "http://127.0.0.1:50000/"
signup_url = "http://127.0.0.1:50000/auth/signup"
profile_url = "http://127.0.0.1:50000/profile"
driver = webdriver.Chrome()

def getConnection():
    conn = psycopg2.connect(database="apidashboarddb", user="postgres", password="12345", host="localhost", port="5432")
    return conn

def check_user_in_database_by_email(emailAddress):
    # Kết nối đến cơ sở dữ liệu PostgreSQL
    conn = getConnection()
    # Tạo một con trỏ để thực hiện truy vấn
    cur = conn.cursor()
    # Thực hiện truy vấn lấy dữ liệu từ bảng tblUser
    cur.execute("SELECT * FROM tblUser WHERE email = %s", (emailAddress,))
    # Lấy kết quả truy vấn
    row = cur.fetchone()
    # Đóng kết nối và con trỏ
    cur.close()
    conn.close()
    # Kiểm tra dữ liệu có tồn tại trong cơ sở dữ liệu hay không
    if row is not None:
        return True
    else:
        return False
    
def get_user_id_by_email(emailAddress):
    conn = getConnection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM tblUser WHERE email = %s",(emailAddress,))

    result = cur.fetchone()

    cur.close()
    conn.close()

    return result[0]

def get_fullname_by_email(emailAddress):
    conn = getConnection()
    cur = conn.cursor()
    cur.execute("SELECT fullname FROM tblUser WHERE email = %s",(emailAddress,))

    result = cur.fetchone()

    cur.close()
    conn.close()

    return result[0]

def count_record_from_tblUser():
    conn = getConnection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM tblUser")

    result = cur.fetchone()

    cur.close()
    conn.close()

    return result[0]

def test_view_user_manage_page():
    driver.get(login_url)
    driver.maximize_window()

    # Khởi tạo các element
    username = driver.find_element(By.XPATH,"//input[@name='username']")
    password = driver.find_element(By.NAME,"password")
    roleUser = driver.find_element(By.NAME,"user")
    roleAdmin = driver.find_element(By.NAME,"admin")
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Nhập username, password, chọn role, bấm đăng nhập
    username.send_keys('ngocduy1')
    time.sleep(1)
    password.send_keys('123Duy')
    time.sleep(1)
    roleAdmin.click()
    time.sleep(1)
    submit.click()
    time.sleep(1)

    # Thực hiện thao tác chuyển hướng đến trang quản lý người dùng
    admin_label = driver.find_element(By.XPATH, "//a[@class='collapsed']//span[@class='text']")
    admin_label.click()   
    time.sleep(1)
    user_manage_label = driver.find_element(By.XPATH, "//a[@href='/admin/user-manage']")
    user_manage_label.click()
    time.sleep(1)

    # Lấy danh sách email người dùng từ giao diện
    emailList = driver.find_elements(By.XPATH,"//p//a[@href='#0']")

    # Tiến hành kiểm tra, kiểm tra người dùng ứng với email từ list trên có tồn tài trong db hay không
    allTrue = False
    for email in emailList:
        if (check_user_in_database_by_email(email.text)):
            allTrue = True
        else:
            allTrue = False
            break
    assert allTrue == True

    time.sleep(3)
    # driver.quit()

def test_update_user():
    # Lấy id của người dùng cần cập nhật bằng email của họ
    toUpdateEmail = driver.find_element(By.XPATH,"//p//a[text()='nguyenngocduy12a2@gmail.com']")
    toUpdateId = get_user_id_by_email(toUpdateEmail.text)

    # Thực hiện cập nhật tên người dùng (các thông tin còn lại làm tương tự)
    update_btn = driver.find_element(By.XPATH,"//button[@class='text-primary'][@data-userid=" + str(toUpdateId)+ "]")
    update_btn.click()
    time.sleep(1)
    fullname = driver.find_element(By.NAME,"fullname")
    fullname.clear()
    fullname.send_keys("edited")
    time.sleep(1)
    confirm_btn = driver.find_element(By.XPATH,"//button[@class='swal2-confirm swal2-styled']")
    confirm_btn.click()
    time.sleep(1)
    confirm_btn = driver.find_element(By.XPATH,"//button[@class='swal2-confirm swal2-styled']")
    confirm_btn.click()
    time.sleep(1)

    # Lấy tên mới của người dùng trong db bằng email lấy từ giao diện
    toUpdateEmail = driver.find_element(By.XPATH,"//p//a[text()='nguyenngocduy12a2@gmail.com']")
    new_fullname = get_fullname_by_email(toUpdateEmail.text)

    # Kiểm tra xem tên mới đã được thay đổi chưa (có thêm (edited))
    time.sleep(3)
    assert "edited" in new_fullname
    driver.implicitly_wait(10)
    #driver.quit()
    
def test_delete_user():
    #toDeleteEmail = driver.find_element(By.XPATH,"//p//a[text()='nguyenngocduy12a2@gmail.com']")
    # Lấy và đếm số lượng phần tử của danh sách email ban đầu từ giao diện
    old_emailList = driver.find_elements(By.XPATH,"//p//a[@href='#0']")
    old_length = len(old_emailList)

    # Lấy id của người dùng cần xóa và thực hiện xóa
    toDeleteId = get_user_id_by_email("nguyenngocduy12a2@gmail.com")
    delete_btn = driver.find_element(By.XPATH,"//button[@class='text-danger'][@data-userid=" + str(toDeleteId)+ "]")
    delete_btn.click()
    time.sleep(1)
    confirm_btn = driver.find_element(By.XPATH,"//button[@class='swal2-confirm swal2-styled']")
    confirm_btn.click()
    time.sleep(1)
    confirm_btn = driver.find_element(By.XPATH,"//button[@class='swal2-confirm swal2-styled']")
    confirm_btn.click()
    time.sleep(1)

    # Sau khi xóa thì dộ dài ban đầu phải -1
    old_length -= 1

    # Tính lại độ dài list email lấy từ giao diện sau khi xóa người dùng
    new_emailList = driver.find_elements(By.XPATH,"//p//a[@href='#0']")
    new_length = len(new_emailList)

    # Kiểm tra xem số lượng người dùng theo lý thuyết (old_length) có bằng số lượng 
    # người dùng vừa lấy được từ giao diện
    # hay không
    time.sleep(3)
    assert old_length == new_length
    driver.implicitly_wait(10)
    #driver.quit()

def test_recovery_all_user(): # Trong thùng rác phải có dữ liệu
    # Lấy số lượng người dùng ban đầu từ giao diện
    old_emailList = driver.find_elements(By.XPATH,"//p//a[@href='#0']")
    old_length = len(old_emailList)

    # Đếm số lượng người dùng hiện có trong CSDL
    count_in_db = count_record_from_tblUser()

    # Thực hiện chuyển hướng đến thùng rác
    trash_bin = driver.find_element(By.XPATH,"//i[@class='lni lni-trash-can']")
    trash_bin.click()
    time.sleep(1)

    # Tính số lượng người dùng đang trong thùng rác
    emailList_in_bin = driver.find_elements(By.XPATH,"//p//a[@href='#0']")
    in_bin_length = len(emailList_in_bin)
    
    # Thực hiện khôi phục tất cả người dùng
    recoveryAll = driver.find_element(By.XPATH, "//a[@onclick='recoveryUserDeleted()']")
    recoveryAll.click()
    time.sleep(1)
    confirm_btn = driver.find_element(By.XPATH,"//button[contains(text(), 'Yes')]")
    confirm_btn.click()
    time.sleep(1)
    confirm_btn = driver.find_element(By.XPATH,"//button[@class='swal2-confirm swal2-styled']")
    confirm_btn.click()
    time.sleep(1)

    # Trở lại trang user manage
    return_user_manage_page = driver.find_element(By.XPATH,"//a[text()='User manage']")
    return_user_manage_page.click()
    time.sleep(1)

    # Đếm số lượng người dùng đang hiển thị
    new_emailList = driver.find_elements(By.XPATH,"//p//a[@href='#0']")
    new_length = len(new_emailList)

    # Kiểm tra xem số lượng trước khi khôi phục hiển thị trên giao diện có bằng số lượng trong db trừ số lượng hiển thị
    # trong thùng rác hay không
    # Và kiểm tra xem số lượng hiển thị sau khi khôi phục có bằng số lượng đếm được trong db hay không
    time.sleep(3)
    assert old_length == count_in_db - in_bin_length and new_length == count_in_db
    driver.implicitly_wait(10)
    driver.quit()

# def test_permanently_delete(): #Trong thùng rác phải có dữ liệu
#     # Lấy số lượng người dùng ban đầu từ giao diện
#     old_emailList = driver.find_elements(By.XPATH,"//p//a[@href='#0']")
#     old_length = len(old_emailList)
    
#     # Đếm số lượng người dùng hiện có trong CSDL
#     count_in_db1 = count_record_from_tblUser()

#     # Chuyển hướng trang đến thùng rác
#     trash_bin = driver.find_element(By.XPATH,"//i[@class='lni lni-trash-can']")
#     trash_bin.click()
#     time.sleep(1)

#     # Tính số lượng người dùng đang trong thùng rác
#     emailList_in_bin = driver.find_elements(By.XPATH,"//p//a[@href='#0']")
#     in_bin_length = len(emailList_in_bin)
    
#     # Thực hiện xóa vĩnh viễn
#     deleteAll = driver.find_element(By.XPATH, "//a[@onclick='deleteAllUserDeleted()']")
#     deleteAll.click()
#     time.sleep(1)
#     confirm_btn = driver.find_element(By.XPATH,"//button[contains(text(), 'Yes')]")
#     confirm_btn.click()
#     time.sleep(1)
#     confirm_btn = driver.find_element(By.XPATH,"//button[@class='swal2-confirm swal2-styled']")
#     confirm_btn.click()
#     time.sleep(1)

#     # Trở lại trang user manage
#     return_user_manage_page = driver.find_element(By.XPATH,"//a[text()='User manage']")
#     return_user_manage_page.click()
#     time.sleep(1)

#     # Đếm số lượng người dùng đang hiển thị
#     new_emailList = driver.find_elements(By.XPATH,"//p//a[@href='#0']")
#     new_length = len(new_emailList)

#     # Đếm số lượng người dùng hiện có trong CSDL
#     count_in_db2 = count_record_from_tblUser()

#     # Kiểm tra xem
#     time.sleep(3)
#     assert old_length == new_length and count_in_db2 == count_in_db1 - in_bin_length
#     driver.implicitly_wait(10)
#     driver.quit()

    
