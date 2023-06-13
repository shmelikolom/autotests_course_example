# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import pytest
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep
from datetime import datetime

driver = webdriver.Chrome()
sbis_site = 'https://fix-online.sbis.ru/'
contact_site = 'https://fix-online.sbis.ru/page/dialogs'
user_login, user_password = 'Marat3', 'Marat12!Marat12!'
date_now = datetime.now().strftime("%d.%m %H:%M:%S")
message_text = f'Я новое сообщение для проверки отправки {date_now}'


def send_login_password(selector, key):
    while True:
        try:
            input_line = driver.find_element(By.CSS_SELECTOR, selector)
            input_line.send_keys(key, Keys.ENTER)
        except StaleElementReferenceException:
            pass
        else:
            break
    return input_line


try:
    driver.get(sbis_site)
    driver.maximize_window()
    login = send_login_password('[name="Login"]', user_login)
    assert login.get_attribute('value') == user_login
    password = send_login_password('[name="Password"]', user_password)
    sleep(30)

    assert driver.title == "СБИС", f"{driver.title}"
    assert driver.current_url == sbis_site, f"{driver.current_url}"

    contacts = driver.find_element(By.CSS_SELECTOR, '[data-name="contacts"]')
    assert contacts.is_displayed(), 'Элемент не отображается'
    contacts.click()
    sleep(15)
    contacts = driver.find_element(By.CSS_SELECTOR, '[name="headTitle"]')
    assert contacts.is_displayed(), 'Элемент не отображается'
    contacts.click()
    sleep(30)

    assert driver.current_url == contact_site, f"{driver.current_url}"
    assert driver.title == "Контакты", f"{driver.title}"
    plus_message = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
    assert plus_message.is_displayed(), 'Элемент не отображается'
    plus_message.click()
    sleep(30)

    search = driver.find_element(By.CSS_SELECTOR, '[class="controls-StackTemplate-content"] input')
    assert search.is_displayed(), 'Элемент не отображается'
    search.send_keys("Marat3", Keys.ENTER)
    assert search.get_attribute('value') == "Marat3"
    sleep(15)

    human = driver.find_element(By.CSS_SELECTOR, '[title="MArat3 Marat3"]')
    assert human.is_displayed(), 'Элемент не отображается'
    human.click()
    sleep(15)

    message = driver.find_element(By.CSS_SELECTOR, '[role="textbox"]')
    assert message.is_displayed(), 'Элемент не отображается'
    message.send_keys(message_text)
    assert message.text == message_text, f"{message.get_attribute('value')}"

    send = driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]')
    assert send.is_displayed(), 'Элемент не отображается'
    send.click()
    sleep(15)

    message_new = driver.find_element(By.XPATH,f"//p[contains(text(), '{message_text}')]")
    assert message_new.text == message_text, f"{message_new.text}"
    assert message_new.is_displayed(), 'Элемент не отображается'

    hover = ActionChains(driver).move_to_element(message_new).perform()
    delete_messages = driver.find_elements(By.CSS_SELECTOR, '[title="Перенести в удаленные"]')
    assert delete_messages[0].is_displayed(), 'Элемент не отображается'
    delete_messages[0].click()

    with pytest.raises(NoSuchElementException):
        message_new = driver.find_element(By.XPATH, f"//p[contains(text(),'{message_text}')]")

finally:
    driver.quit()
