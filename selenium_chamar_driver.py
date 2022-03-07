def iniciar_navegador():
    # from selenium import webdriver
    # from selenium.webdriver.common.keys import Keys
    # from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
    # driver = webdriver.Firefox(executable_path="D:\geckodriver.exe") 
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    return driver