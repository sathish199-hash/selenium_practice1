from selenium import webdriver

def test_verifyTitle():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    assert driver.title == "Google "
    driver.close()
