# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'


try:
    driver.get(sbis_site)
    contact = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header [href = "/contacts"]')
    assert contact.text == 'Контакты', 'Раздел "Контакты" называется по другому'
    assert contact.is_displayed(), 'Элемент не отображается'

    contact.click()
    assert driver.title == 'СБИС Контакты — Ярославская область', f'Не верное название вкладки {driver.title}'

    banner_tensor = driver.find_element(By.CSS_SELECTOR, '[id = "contacts_clients"] [href = "https://tensor.ru/"]')
    assert banner_tensor.is_displayed(), 'Элемент не отображается'

    banner_tensor.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://tensor.ru/', f"Перешли на неверный сайт {driver.current_url}"
    assert driver.title == 'Тензор — IT-компания', f'Не верное название вкладки: "{driver.title}"'

    block = driver.find_elements(By.CSS_SELECTOR, '[class = "tensor_ru-Index__block4-content tensor_ru-Index__card"]>p')
    assert len(block) == 4, 'В блоке "Сила в людях" показана не вся информация'
    assert block[0].is_displayed(), 'Элемент не отображается'
    assert block[0].text == "Сила в людях"

    block_more = block[-1].find_element(By.CSS_SELECTOR, '[href="/about"]')
    assert block_more.is_displayed(), 'Элемент не отображается'
    assert block_more.text == 'Подробнее', f'Не верное название "Подробнее": {block_more}'

    driver.execute_script("return arguments[0].scrollIntoView(true);", block[-2])
    block_more.click()
    assert 'https://tensor.ru/about' == driver.current_url, f"Страница на которую перешли {driver.current_url}"
    assert driver.title == 'О компании | Тензор — IT-компания',\
        "Название страницы ({driver.title} не соответсвует ожидаемому"

finally:
    driver.quit()
