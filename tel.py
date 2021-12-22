from requests import *
import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from telegram import *
from telegram.ext import *
from selenium.webdriver.chrome.service import Service
# os.environ['DISPLAY'] = ':0'
# os.environ['XAUTHORITY']='/run/user/1000/gdm/Xauthority'
# import pyautogui

chat_id = '1040677949'
token = '5044607805:AAGXftP7iB21jzrrjQlq5AJ6NaRE32xsBP8'
token2 = '5074614499:AAED77YvgIKWMgF7OHnQ07-hRF8QXWjQX90'
chat_id2 = '1040677949'



def send_t(text):
    url_req = f'https://api.telegram.org/bot{token2}/sendMessage?chat_id={chat_id2}&text={text}'
    result = requests.get(url_req)
    print(result.json())




updater = Updater(token=token2)
dispatcher = updater.dispatcher
print('im listening...')


def startcommand(update: Update, context: CallbackContext):
    #    os.system("python C:/Users/ashachar/portugal/main.py")
    chat_id = '1040677949'
    token = '5044607805:AAGXftP7iB21jzrrjQlq5AJ6NaRE32xsBP8'
    base_url = f'https://api.telegram.org/bot{token}'
    

    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    op.add_argument("--headless")
    op.add_argument("--disable-dev-shm-usage")
    op.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=op)
    browser.get(f"https://agendamentosonline.mne.gov.pt/AgendamentosOnline/app/scheduleAppointmentForm.jsf")
    browser.maximize_window()
    x = 0
    ID = browser.find_element_by_xpath('//*[@id="scheduleForm:tabViewId:ccnum"]')
    ID.send_keys('9057029683')
    time.sleep(1)
    date = browser.find_element_by_xpath('//*[@id="scheduleForm:tabViewId:dataNascimento_input"]')
    date.send_keys("20-05-2000")
    search = browser.find_element_by_xpath('//*[@id="scheduleForm:tabViewId:searchIcon"]')
    search.click()
    time.sleep(2)
    browser.implicitly_wait(10)
    drop = browser.find_element_by_xpath('//*[@id="scheduleForm:postcons"]/div[2]')
    drop.click()
    browser.implicitly_wait(10)
    second = browser.find_element_by_xpath('//*[@id="scheduleForm:postcons_panel"]/div/ul/li[2]')
    second.click()
    browser.implicitly_wait(10)
    drop2 = browser.find_element_by_xpath('//*[@id="scheduleForm:categato"]/div[2]')
    drop2.click()
    second2 = browser.find_element_by_xpath('//*[@id="scheduleForm:categato_panel"]/div/ul/li[2]')
    second2.click()
    browser.implicitly_wait(10)
    browser.find_element_by_id('scheduleForm:bAddAto').click()
    browser.implicitly_wait(10)
    browser.find_element_by_xpath('//*[@id="scheduleForm:dataTableListaAtos:0:selCond"]/div[2]').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="scheduleForm:dataTableListaAtos:0:bCal"]').click()
    time.sleep(2)

    browser.save_screenshot(r'~/port.PNG')
    files = {'photo': open('~/port.PNG', 'rb')}
    url_req = f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id},'
    result = requests.post(url_req, files=files)
    print(result.json())
    browser.minimize_window()

    x = 0
    while x != 1:
        read_msg()
    else:
        pass
    ID = browser.find_element_by_xpath('//*[@id="grantSchedulingFormID:captchaCode"]')
    ID.send_keys(typein)

    con = browser.find_element_by_xpath('//*[@id="grantSchedulingFormID:grantSchedulingContinueBtnID"]')
    con.click()
    time.sleep(2)

    browser.save_screenshot(r'~/status.PNG')
    files = {'photo': open('~/status.PNG', 'rb')}

    url_req = f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id},'
    result = requests.post(url_req, files=files)

    offset = 143766194 + 9999
    time.sleep(30)
    resp = requests.get(base_url + f"/getUpdates?offset={offset}")
    data = resp.json()
    for result in data["result"]:
        print(data)
        offset += 999
        if result["message"]["text"]:
            print("---------------------------------------")
        typein = result["message"]["text"]
        print(typein)
    ID = browser.find_element_by_xpath('//*[@id="grantSchedulingFormID:captchaCode"]')
    ID.send_keys(typein)
    time.sleep(3)
    con = browser.find_element_by_xpath('//*[@id="grantSchedulingFormID:grantSchedulingContinueBtnID"]')
    con.click()
    time.sleep(2)
    # captcha2 = pyautogui.screenshot()
    captcha2.save(r'C:/Users/ashachar/Desktop/for_py/status.PNG')
    files = {'photo': open('C:/Users/ashachar/Desktop/for_py/status.PNG', 'rb')}

    url_req = f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id},'
    result = requests.post(url_req, files=files)


dispatcher.add_handler(CommandHandler("start", startcommand))
updater.start_polling()




