# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
from datetime import datetime


def size_file_mb(file):
    """Возвращает размер файла в мегабайтах"""
    start = datetime.now().timestamp()
    while 1:
        try:
            assert start + 30 >= datetime.now().timestamp(), "Файл не загрузился"
            size_file = file.stat().st_size
            break
        except FileNotFoundError:
            pass
    return size_file / 1024 ** 2


chromeOptions = webdriver.ChromeOptions()
prefs = {'download.default_directory': str(Path.cwd()),
         'safebrowsing.enabled': 'false',
         "download.directory_upgrade": True}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)
sbis_site = 'https://sbis.ru/'

try:
    driver.get(sbis_site)
    download = driver.find_element(By.CSS_SELECTOR, '[href="/download?tab=ereport&innerTab=ereport25"]')
    assert download.is_displayed(), 'Элемент не отображается'
    assert download.text == 'Скачать СБИС', f"{download.text}"
    driver.execute_script("return arguments[0].scrollIntoView(true);", download)
    download.click()

    assert driver.title == 'Скачать СБИС и дополнительное ПО', f"{driver.title}"
    assert driver.current_url == 'https://sbis.ru/download?tab=ereport&innerTab=ereport25', f"{driver.current_url}"
    download_plugin = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
    assert download_plugin.is_displayed(), 'Элемент не отображается'
    download_plugin.click()
    assert driver.current_url == 'https://sbis.ru/download?tab=plugin&innerTab=default'
    download_exe = driver.find_element(By.CSS_SELECTOR, '[href="https://update.sbis.ru/'
                                                        'Sbis3Plugin/master/win32/'
                                                        'sbisplugin-setup-web.exe"]')
    download_exe.click()

    file_plugin = Path('sbisplugin-setup-web.exe')
    print(size_file_mb(file_plugin))
    file_plugin.unlink()
finally:
    driver.quit()
