from pages.auth_page import AuthPage
import time
from selenium.webdriver.common.by import By
from pages.elements import WebElement
from setting import valid_password, invalid_password, valid_login, invalid_login, valid_email, invalid_email, \
    valid_phone, invalid_phone, name_user, last_name_user
# import imaplib
# import email
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.for_tests import russian_chars, chinese_chars, special_chars, digit_in_char, generate_string, japan_chars, \
    generate_string_num, eng_string


# Test-001 Наличие логотипа в левом верхнем углу страницы.
def test_find_up_logo(web_browser):
    """Тест проверяет наличие логотипа компании в левом верхнем углу страницы."""
    page = AuthPage(web_browser)
    x_y = page.logo.get_location()
    assert page.logo.is_presented() and page.logo.is_visible() and page.up_page.is_presented()
    assert int(x_y['x']) < 200 and int(x_y['y']) < 20, "логотип расположен не в левом верхнем углу"


# Test-002 Наличие заголовка раздела, знака и слогана компании в левом блоке основного контента.
def test_find_left_block(web_browser):
    """Тест проверяет наличие заголовка раздела, знака и слогана компании в левом блоке основного контента."""
    page = AuthPage(web_browser)
    assert page.left_logo.is_presented() and page.logo.is_visible(), "В левом блоке отсутсвует логотип"
    assert page.left_slogan.is_presented() and page.left_slogan.is_visible(), "В левом блоке отсутсвует слоган"
    assert page.left_title.is_presented() and page.left_title.is_visible(), "В левом блоке отсутвует заголовок раздела"
    assert page.left_title.get_text() in page.left_side.get_text()
    assert page.left_slogan.get_text() in page.left_side.get_text()


# Test-003 Наличие формы авторизации в правом блоке основного контента.
def test_find_right_block(web_browser):
    """Тест проверяет наличие формы авторизации в правом блоке основного контента."""
    page = AuthPage(web_browser)
    assert page.right_side.is_presented() and page.name_form.get_text() == "Авторизация"
    assert page.name_menu_phone.get_text() in page.right_side.get_text()
    assert page.name_menu_mail.get_text() in page.right_side.get_text()
    assert page.name_menu_login.get_text() in page.right_side.get_text()
    assert page.name_menu_ls.get_text() in page.right_side.get_text()


# Test-004 Доступность формы "Регистрация" при нажатии на ссылку "Регистрация"
def test_registration_form(web_browser):
    """Тест проверяет доступность формы "Регистрация" при нажатии на ссылку "Регистрация"."""
    page = AuthPage(web_browser)
    page.registration_link.click()
    assert page.name_form.get_text() == "Регистрация"
    assert "Имя\n" and "Фамилия\n" and "Регион\n" and "Пароль\n" in page.form_container.get_text()


# Test-005 Доступность формы "Восстановление пароля" при нажатии на ссылку "Забыл пароль" и возвращение обратно на
# форму авторизации
def test_forgot_password_form(web_browser):
    """Тест проверяет доступность формы "Восстановление пароля" при нажатии на ссылку "Забыл пароль" и возвращение
    обратно на форму авторизации."""
    page = AuthPage(web_browser)
    page.forgot_passw_link.click()
    assert page.name_form.get_text() == "Восстановление пароля"
    assert "Введите данные и нажмите «Продолжить»\n" in page.form_container.get_text()
    assert page.name_menu_phone.get_text() in page.right_side.get_text()
    assert page.name_menu_mail.get_text() in page.right_side.get_text()
    assert page.name_menu_login.get_text() in page.right_side.get_text()
    assert page.name_menu_ls.get_text() in page.right_side.get_text()
    page.reset_back_button.click()
    assert page.name_form.get_text() == "Авторизация"
    assert "Пароль\n" and "Запомнить меня\n" in page.form_container.get_text()


# Test-006 Наличие в форме авторизации меню и необходимых полей для ввода, переход по меню.
# Проверка смены назначения поля ввода данных при переходе по меню.
def test_menu_authorization_form(web_browser):
    """Тест проверяет наличие в форме авторизации меню и необходимых полей для ввода."""
    d = {}  # словарь наличия искомых элементов формы
    page = AuthPage(web_browser)
    if page.name_menu_mail.find():
        page.name_menu_mail.click()
        page.wait_page_loaded()
        print()
        print("-" * 100)
        d['Пункт меню почта'] = '1'
        if page.login_input.find() and page.login_input.is_visible():
            d['Поле ввода почты'] = '1'
            if "Электронная почта" in page.name_login.get_text():
                d['Название поля для ввода почты'] = '1'
            else:
                d['Название поля для ввода почты'] = '0'
        else:
            d['Поле ввода адреса'] = '0'
        if page.password_input.find() and page.password_input.is_visible():
            d['Поле ввода пароля'] = '1'
            if "Пароль" in page.name_login.get_text():
                d['Название поля ввода пароля'] = '1'
            else:
                d['Название поля ввода пароля'] = '0'
        else:
            d['Поле ввода пароля'] = '0'
        if page.btn_enter.find() and page.btn_enter.is_clickable():
            d['Кнопка войти'] = '1'
        else:
            d['Кнопка войти'] = '0'
    else:
        d['Элемент меню Почта'] = '0'
    print(d)
    try:
        assert '0' not in d.values(), "Элемент в меню 'Почта' не найден"
    except Exception as e:
        print(e)
        pass
    d.clear()
    print("-" * 100)
    if page.name_menu_phone.find():
        page.name_menu_phone.click()
        page.wait_page_loaded()
        if page.login_input.find() and page.login_input.is_visible():
            d['Поле ввода телефона'] = '1'
            if "Мобильный телефон" in page.name_login.get_text():
                d['Название поля для ввода телефона'] = '1'
            else:
                d['Название поля для ввода телефона'] = '0'
        else:
            d['Поле ввода телефона'] = '0'
        if page.password_input.find() and page.password_input.is_visible():
            d['Поле ввода пароля'] = '1'
            if "Пароль" in page.name_login.get_text():
                d['Название поля ввода пароля'] = '1'
            else:
                d['Название поля ввода пароля'] = '0'
        else:
            d['Поле ввода пароля'] = '0'
        if page.btn_enter.find() and page.btn_enter.is_clickable():
            d['Кнопка войти'] = '1'
        else:
            d['Кнопка войти'] = '0'
    else:
        d['Элемент меню Почта'] = '0'
    print(d)
    try:
        assert '0' not in d.values(), "Элемент в меню 'Телефон' не найден"
    except Exception as e:
        print(e)
        pass
    d.clear()
    print("-" * 100)
    if page.name_menu_login.find():
        page.name_menu_login.click()
        page.wait_page_loaded()
        if page.login_input.find() and page.login_input.is_visible():
            d['Поле ввода логина'] = '1'
            if "Логин" in page.name_login.get_text():
                d['Название поля для ввода логина'] = '1'
            else:
                d['Название поля для ввода логина'] = '0'
        else:
            d['Поле ввода логина'] = '0'
        if page.password_input.find() and page.password_input.is_visible():
            d['Поле ввода пароля'] = '1'
            if "Пароль" in page.name_login.get_text():
                d['Название поля ввода пароля'] = '1'
            else:
                d['Название поля ввода пароля'] = '0'
        else:
            d['Поле ввода пароля'] = '0'
        if page.btn_enter.find() and page.btn_enter.is_clickable():
            d['Кнопка войти'] = '1'
        else:
            d['Кнопка войти'] = '0'
    else:
        d['Элемент меню Почта'] = '0'
    print(d)
    try:
        assert '0' not in d.values(), "Элемент в меню 'Логин' не найден"
    except Exception as e:
        print(e)
        pass
    d.clear()
    print("-" * 100)
    if page.name_menu_ls.find():
        page.name_menu_ls.click()
        page.wait_page_loaded()
        if page.login_input.find() and page.login_input.is_visible():
            d['Поле ввода номера лицевого счета'] = '1'
            if "Лицевой счёт" in page.name_login.get_text():
                d['Название поля для ввода лс'] = '1'
            else:
                d['Название поля для ввода лс'] = '0'
        else:
            d['Поле ввода телефона'] = '0'
        if page.password_input.find() and page.password_input.is_visible():
            d['Поле ввода номера лицевого счета'] = '1'
            if "Пароль" in page.name_login.get_text():
                d['Название поля ввода пароля'] = '1'
            else:
                d['Название поля ввода пароля'] = '0'
        else:
            d['Поле ввода пароля'] = '0'
        if page.btn_enter.find() and page.btn_enter.is_clickable():
            d['Кнопка войти'] = '1'
        else:
            d['Кнопка войти'] = '0'
    else:
        d['Элемент меню Почта'] = '0'
    print(d)
    try:
        assert '0' not in d.values(), "Элемент в меню 'Лицевой счёт' не найден"
    except Exception as e:
        print(e)
        pass
    d.clear()
    print("-" * 100)


# Test-007 Проверка автоматического изменения таба выбора аутентификации при корректных данных
def test_auto_authentication_phone(web_browser):
    """Проверка автоматического изменения таба выбора аутентификации при корректных данных. Для таба: телефон."""
    page = AuthPage(web_browser)
    page.name_menu_phone.click()
    page.login_input.send_keys(digit_in_char(10))
    page.password_input.click()
    try:
        assert page.name_login.get_text()[0] == "Мобильный телефон", "Не остались на таб: телефон"
    except Exception as e:
        print(e)
        pass

    page.name_menu_phone.click()
    page.login_input.send_keys("exam@exam.ru")
    page.password_input.click()
    try:
        assert page.name_login.get_text()[0] == "Электронная почта", "Не перешли на таб: электронная почта"
    except Exception as e:
        print(e)
        pass
    page.name_menu_phone.click()
    page.login_input.send_keys(digit_in_char(11))
    page.password_input.click()
    try:
        assert page.name_login.get_text()[0] == "Лицевой счёт", "Не перешли на таб: лицевой счет"
    except Exception as e:
        print(e)
        pass
    page.name_menu_phone.click()
    page.login_input.send_keys("rtkid_1691570760805")
    page.password_input.click()
    try:
        assert page.name_login.get_text()[0] == "Логин", "Не перешли на таб: логин"
    except Exception as e:
        print(e)
        pass


# Test-008 Наличие в форме авторизации чекбокса "Запомнить меня" и его переключение.
def test_checkbox_work_in_authorization_form(web_browser):
    page = AuthPage(web_browser)
    page.checkbox.find()
    assert page.checkbox.is_clickable(), "Чекбокс не активен"
    if page.checkbox_checked.is_presented():
        page.checkbox.click()
    page.checkbox.click()
    assert page.checkbox_checked.is_presented(), "В чекбоксе нет значка выбора"
    page.checkbox.click()
    assert not page.checkbox_checked.is_presented(), "Значок выбора остался"
    print("Чекбокс активен, при нажатии появляется или убирается значок выбора")


# Test-009 Проверка поля ввода телефона (позитивная)
@pytest.mark.parametrize('phone', [digit_in_char(10, "7"), digit_in_char(10, "8"), digit_in_char(9, "3"),
                                   digit_in_char(9, "37"), digit_in_char(9, "375"), digit_in_char(9)],
                         ids=["first 7 - eleven digits", "first 8 - eleven digits", "first 3 - twelve digits",
                              "first 37 - twelve digits", "first 375 - twelve digits", "ten digits"])
@pytest.mark.parametrize('password', [valid_password], ids=["positive_password"])
def test_login_phone_input_positive(web_browser, phone, password):
    """ Позитивная проверка поля ввода номера телефона"""
    page = AuthPage(web_browser)
    page.name_menu_phone.click()
    page.login_input.send_keys(phone)
    login_data = page.get_login_input.get_attribute("value")
    page.password_input.send_keys(password)
    if login_data[0:3] == "375":
        assert not page.login_error.is_visible() and len(login_data) == 12  # позитивная проверка на +3
    else:
        assert not page.login_error.is_visible() and login_data[0:1] == "7" and len(
            login_data) == 11  # позитивная проверка


# Test-010 Проверка поля ввода телефона (негативная) на колличество цифр
@pytest.mark.parametrize('phone', [digit_in_char(0), digit_in_char(1), digit_in_char(4),
                                   digit_in_char(11, "7"), digit_in_char(9, "7"), digit_in_char(11, "8"),
                                   digit_in_char(9, "8"), digit_in_char(10, "3"), digit_in_char(8, "3"),
                                   digit_in_char(8), digit_in_char(10), "595  567", "   8589"],
                         ids=["one digit", "two digits", "five digits", "first 7 - twelve digits",
                              "first 7 - ten digits", "first 8 - twelve digits", "first 8 - ten digits",
                              "first 3 - thirteen digits", "first 3 - eleven digits", "nine digits", "eleven digits",
                              "six digits with middle whitespaces", "first whitespaces and four digits "])
@pytest.mark.parametrize('password', [valid_password], ids=["positive_password"])
def test_login_phone_input_negative_num(web_browser, phone, password):
    """ Негативная проверка поля ввода номера телефона на введение неверного колличества цифр"""
    page = AuthPage(web_browser)
    page.name_menu_phone.click()
    mail_input = phone
    page.login_input.send_keys(mail_input)
    login_data = page.get_login_input.get_attribute("value")
    page.password_input.send_keys(password)
    if mail_input[0] == "3" and len(mail_input) > 10:
        assert login_data[0:3] == "375" and len(login_data) == 12 and not page.login_error.is_visible()
    elif mail_input[0] == "3" and len(mail_input) < 10:
        assert login_data[0:3] == "375" and len(
            login_data) < 12 and page.login_error.get_text() == "Неверный формат телефона"
    elif (mail_input[0] == "7" or mail_input[0] == "8") and len(mail_input) > 11:
        assert login_data[0] == "7" and len(login_data) == 11 and not page.login_error.is_visible()
    elif (mail_input[0] == "7" or mail_input[0] == "8") and len(mail_input) < 11:
        assert login_data[0] == "7" and len(
            login_data) < 11 and page.login_error.get_text() == "Неверный формат телефона"
    elif len(mail_input) > 10 and mail_input[0] in ["1", "2", "4", "5", "6", "9", "0"]:
        assert login_data[0] == "7" and len(login_data) == 11 and login_data[
            0] == "7" and not page.login_error.is_visible()
    elif len(mail_input) < 10 and mail_input[0] in ["1", "2", "4", "5", "6", "9", "0"]:
        if "" in mail_input:
            assert "" in login_data, "В поле ввода телефона остались пробелы"
        assert login_data[0] == "7" and len(
            login_data) < 11 and page.login_error.get_text() == "Неверный формат телефона"


# Test-011 Проверка поля ввода телефона (негативная) на строки
@pytest.mark.parametrize('phone', ["", "  ", russian_chars(), russian_chars().upper(), chinese_chars(),
                                   special_chars(), generate_string(255), generate_string(1001), japan_chars(),
                                   generate_string_num(255)],
                         ids=["empty string", "whitespace", "russian", "RUSSIAN", "chinese", "special symbols",
                              "string 255", "string 1001", "japan", "string 255 with digits"])
@pytest.mark.parametrize('password', [valid_password], ids=["positive_password"])
def test_login_phone_input_negative_char(web_browser, phone, password):
    """ Негативная проверка поля ввода номера телефона на ввод символов"""
    page = AuthPage(web_browser)
    page.name_menu_phone.click()
    mail_input = phone
    page.login_input.send_keys(mail_input)
    login_data = page.login_input.get_attribute("value")
    page.password_input.send_keys(password)
    if not mail_input:
        assert page.login_error.get_text() == "Введите номер телефона"
    elif len(mail_input):
        if len(login_data):
            assert login_data.isdigit()
        else:
            assert len(login_data) == "" and page.login_error.is_visible()


# Test-12 Проверка поля ввода адреса электронной почты (набор позитивных проверок)
@pytest.mark.parametrize('mail', ["name.surname@gmail.com", "anonymous123@yahoo.co.uk", "name.surname@gmail.com",
                                  "123@mail.ru", "123.surname@gmail.com",
                                  "ano.nym.oj" + eng_string(255) + "us@yandex.ru"],
                         ids=["name.surname@gmail.com", "anonymous123@yahoo.co.uk", "name.surname@gmail.com",
                              "123@mail.ru", "123.surname@gmail.com", "ano.nym.oj" + eng_string(255) + "us@yandex.ru"])
@pytest.mark.parametrize('password', [valid_password], ids=["positive_password"])
def test_login_email_input_positive(web_browser, mail, password):
    """ Тест осуществляют проверку поля ввода адреса электронной почты (набор позитивных проверок)"""
    page = AuthPage(web_browser)
    page.name_menu_mail.click()
    mail_input = mail
    page.login_input.send_keys(mail_input)
    mail_data = page.login_input.get_attribute("value")
    page.password_input.send_keys(password)
    assert not page.login_error.is_visible() and mail == mail_data


# Test-13 Проверка поля ввода адреса электронной почты (набор негативных проверок)
@pytest.mark.parametrize('mail', ["", "  ", eng_string(255) + "us@yandex", "]-o@mail.ru", "@   mail.ru",
                                  "user@ru", "user@.mail.ru", generate_string(10) + "us@yandex.ru", "user.mail.ru",
                                  "user  user@mail.ru"],
                         ids=["empty string", "whitespace", eng_string(255) + "us@yandex", "]-o@mail.ru", "@   mail.ru",
                              "user@ru", "user@.mail.ru", generate_string(10) + "us@yandex.ru", "user.mail.ru",
                              "user  user@mail.ru"])
@pytest.mark.parametrize('password', [valid_password], ids=["positive_password"])
def test_login_email_input_negative(web_browser, mail, password):
    """ Тест осуществляют проверку поля ввода адреса электронной почты (набор негативных проверок)"""
    page = AuthPage(web_browser)
    page.name_menu_mail.click()
    mail_input = mail
    page.login_input.send_keys(mail_input)
    page.password_input.send_keys(password)
    assert page.login_error.is_visible()


# Test-014 Проверка поля ввода логина (позитивная и негативная)
@pytest.mark.parametrize('login', ["", "  ", russian_chars(), russian_chars().upper(), chinese_chars(),
                                   special_chars(), generate_string(255), generate_string(1001), japan_chars(),
                                   generate_string_num(255), "rtkid_1691570760805", "_1691570760805",
                                   "rtkid_1691570760805789", digit_in_char(0), digit_in_char(1), digit_in_char(4),
                                   digit_in_char(11)],
                         ids=["empty string", "whitespace", "russian", "RUSSIAN", "chinese", "special symbols",
                              "string 255", "string 1001", "japan", "string 255 with digits", "right format login",
                              "no format login", "right format login 16 number", "one digit", "two digits",
                              "five digits", "twelve digits"])
@pytest.mark.parametrize('password', [valid_password], ids=["positive_password"])
def test_login_login_input(web_browser, login, password):
    """ Проверка поля ввода логина"""
    page = AuthPage(web_browser)
    page.name_menu_login.click()
    login_input = login
    page.login_input.send_keys(login_input)
    login_data = page.login_input.get_attribute("value")
    page.password_input.send_keys(password)
    if not login_input:
        assert page.login_error.is_visible()
    elif login_input and login_data:
        if len(login_data) and login_data[:6] == "rtkid_":
            assert 6 < len(login_data) < 30 and login_data[6:].isdigit()
            print("Входные данные соответсвуют")
        else:
            assert page.login_error.is_visible()


# Test-015 Проверка поля ввода лицевого счета на колличество цифр
@pytest.mark.parametrize('ls', [digit_in_char(0), digit_in_char(4),
                                digit_in_char(10), digit_in_char(11), digit_in_char(12), "595  567", "   8589"],
                         ids=["one digit", "five digits", "eleven digits", "twelve digits", "thirteen digits",
                              "six digits with middle whitespaces", "first whitespaces and four digits "])
@pytest.mark.parametrize('password', [valid_password], ids=["positive_password"])
def test_login_ls_input_num(web_browser, ls, password):
    """ Позитивная и негативная проверка поля ввода лицевого счета на введение разного колличества цифр"""
    page = AuthPage(web_browser)
    page.name_menu_ls.click()
    ls_input = ls
    page.login_input.send_keys(ls_input)
    login_data = page.get_login_input.get_attribute("value")
    page.password_input.send_keys(password)
    if len(ls_input) == 12:
        assert len(login_data) == 12 and not page.login_error.is_visible()  # Позитивная проверка
    elif len(ls_input) < 12:
        if "" in ls_input:
            assert "" in login_data, "В поле ввода номера лицевого счета остались пробелы"
        assert len(login_data) < 12 and page.login_error.get_text() == "Проверьте, пожалуйста, номер лицевого счета"
    elif len(ls_input) > 12:
        assert len(login_data) == 12 and not page.login_error.is_visible()


# Test-016 Проверка поля ввода лицевого счета на строки
@pytest.mark.parametrize('ls', ["", "  ", russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(),
                                generate_string(255), generate_string(1001), japan_chars(), generate_string_num(255)],
                         ids=["empty string", "whitespace", "russian", "RUSSIAN", "chinese", "special symbols",
                              "string 255", "string 1001", "japan", "string 255 with number"])
@pytest.mark.parametrize('password', [valid_password], ids=["positive_password"])
def test_login_ls_input_negative_char(web_browser, ls, password):
    """ Негативная проверка поля ввода лицевого счета на ввод символов"""
    global login_data_num
    page = AuthPage(web_browser)
    page.name_menu_ls.click()
    ls_input = ls
    page.login_input.send_keys(ls_input)
    login_data = page.login_input.get_attribute("value")
    page.password_input.send_keys(password)
    if not login_data:
        assert page.login_error.get_text() == "Проверьте, пожалуйста, номер лицевого счета"
    elif ls_input and login_data:
        if len(login_data) == 12 and login_data.isdigit():
            assert not page.login_error.is_visible()
        elif len(login_data) < 12 and login_data.isdigit():
            assert page.login_error.get_text() == "Проверьте, пожалуйста, номер лицевого счета"
        elif len(login_data) > 12 and login_data.isdigit():
            assert len(login_data) == 12, "Лицевой счет должен содержать ровно 12 символов"
        else:
            assert not len(login_data), "Нельзя вводить символы в числове поле"


# Test-017  "Авторизация по номеру телефона" (форма "Авторизация")
@pytest.mark.parametrize('phone', [invalid_phone, valid_phone], ids=["negative_phone", "positive_phone"])
@pytest.mark.parametrize('password', [valid_password, invalid_password], ids=["positive_password", "negative_password"])
def test_authorization_by_phone(web_browser, phone, password):
    """Тecт проверки авторизации по номеру (форма авторизации), позитивный и негативные с корректными данными."""
    page = AuthPage(web_browser)
    if page.captcha.find():  # Проверка, что есть капча
        pytest.skip("Присутствует капча")
    page.name_menu_phone.click()
    page.login_input.send_keys(phone)
    page.password_input.send_keys(password)
    page.btn_enter.click()
    page.wait_page_loaded()
    if page.form_error.find():
        value = page.form_error.get_text()
        assert not page.last_name.find() and value == "Неверный логин или пароль"
        print("-" * 100, value, "-" * 100, sep="\n")
    else:
        page.last_name.find()
        value_name = page.last_name.get_text()
        assert 'Учетные данные' in page.card_title.get_text()  # Проверка входа в личный кабинет пользователя
        print(f"Личный кабинет принадлежит пользователю: {value_name}")
        print("-" * 100, "Указаны верные данные", "-" * 100, sep="\n")


# Test-018 "Авторизация по email" (форма "Авторизация")
@pytest.mark.parametrize('mail', [invalid_email, valid_email], ids=["negative_email", "positive_email"])
@pytest.mark.parametrize('password', [valid_password, invalid_password], ids=["positive_password", "negative_password"])
def test_authorization_by_email(web_browser, mail, password):
    """Тecт проверки авторизации по email (форма авторизации), позитивный и негативные с корректными данными."""
    page = AuthPage(web_browser)
    if page.captcha.find():  # Проверка, что есть капча
        pytest.skip("Присутствует капча")
    page.name_menu_login.click()
    page.login_input.send_keys(mail)
    page.password_input.send_keys(password)
    page.btn_enter.click()
    page.wait_page_loaded()
    if page.form_error.find():
        value = page.form_error.get_text()
        assert not page.last_name.find() and value == "Неверный логин или пароль"
        print("-" * 100, value, "-" * 100, sep="\n")
    else:
        page.last_name.find()
        value_name = page.last_name.get_text()
        assert 'Учетные данные' in page.card_title.get_text()  # Проверка входа в личный кабинет пользователя
        print(f"Личный кабинет принадлежит пользователю: {value_name}")
        print("-" * 100, "Указаны верные данные", "-" * 100, sep="\n")


# Test-019 "Авторизация по логину" (форма "Авторизация")
@pytest.mark.parametrize('login', [invalid_login, valid_login], ids=["negative_login", "positive_login"])
@pytest.mark.parametrize('password', [valid_password, invalid_password], ids=["positive_password", "negative_password"])
def test_authorization_by_login(web_browser, login, password):
    """Тecт проверки авторизации по логину (форма авторизации), позитивный и негативные с корректными данными."""
    page = AuthPage(web_browser)
    if page.captcha.find():  # Проверка, что есть капча
        pytest.skip("Присутствует капча")
    page.name_menu_login.click()
    page.login_input.send_keys(login)
    page.password_input.send_keys(password)
    page.btn_enter.click()
    page.wait_page_loaded()
    if page.form_error.find():
        value = page.form_error.get_text()
        assert not page.last_name.find() and value == "Неверный логин или пароль"
        print("-" * 100, value, "-" * 100, sep="\n")
    else:
        page.last_name.find()
        value_name = page.last_name.get_text()
        assert 'Учетные данные' in page.card_title.get_text()  # Проверка входа в личный кабинет пользователя
        print(f"Личный кабинет принадлежит пользователю: {value_name}")
        print("-" * 100, "Указаны верные данные", "*" * 100, sep="\n")


# Test-020 "Авторизация по лицевому счету" (форма "Авторизация") только негативная
@pytest.mark.parametrize('ls', ["234563479526"], ids=["negative_ls"])
@pytest.mark.parametrize('password', [valid_password, invalid_password], ids=["positive_password", "negative_password"])
def test_authorization_by_ls(web_browser, ls, password):
    """Тecт проверки авторизации по номеру лицевого счета (форма авторизации), только негативный с корректными
    данными."""
    page = AuthPage(web_browser)
    if page.captcha.find():  # Проверка, что есть капча
        pytest.skip("Присутствует капча")
    page.name_menu_ls.click()
    page.login_input.send_keys(ls)
    page.password_input.send_keys(password)
    page.btn_enter.click()
    page.wait_page_loaded()
    if page.form_error.find():
        value = page.form_error.get_text()
        assert not page.last_name.find() and value == "Неверный логин или пароль"
        print("-" * 100, value, "-" * 100, sep="\n")
    else:
        page.last_name.find()
        value_name = page.last_name.get_text()
        assert 'Учетные данные' in page.card_title.get_text()  # Проверка входа в личный кабинет пользователя
        print(f"Личный кабинет принадлежит пользователю: {value_name}")
        print("-" * 100, "Указаны верные данные", "-" * 100, sep="\n")


# Test-021 "Проверка возможности зарегистрировать аккаунт, дублирующий существующий по номеру телефона"
# (форма "Регистрация")
def test_check_double_account_by_phone(web_browser):
    """Тecт проверки возможности зарегистрировать аккаунт, с номером телефона, который уже используется в другом
    личном кабинете, с корректными данными."""
    page = AuthPage(web_browser)
    page.registration_link.click()
    page.name_input.send_keys(name_user)
    page.last_name_input.send_keys(last_name_user)
    page.email_or_phone.send_keys(valid_phone)
    page.password_registration.send_keys(valid_password)
    page.password_confirmation.send_keys(valid_password)
    page.btn_registration.click()
    page.card_modal.wait_until_not_visible()
    assert page.card_modal.find()
    value = page.card_modal_title.get_text()
    assert value == 'Учётная запись уже существует'
    print('\n', value)


# Test-022 "Проверка возможности зарегистрировать аккаунт, дублирующий существующий по email" (форма "Регистрация")
def test_check_double_account_by_email(web_browser):
    """Тecт проверки возможности регистрации аккаунта, с адресом электронной почты, на которой уже зарегистрирован
        другой аккаунт, с корректными данными."""
    page = AuthPage(web_browser)
    page.registration_link.click()
    page.name_input.send_keys(name_user)
    page.last_name_input.send_keys(last_name_user)
    page.email_or_phone.send_keys(valid_email)
    page.password_registration.send_keys(valid_password)
    page.password_confirmation.send_keys(valid_password)
    page.btn_registration.click()
    page.card_modal.wait_until_not_visible()
    assert page.card_modal.find()
    value = page.card_modal_title.get_text()
    assert value == 'Учётная запись уже существует'
    print('\n', value)


# Test-023 Проверка наличия и кликабельности иконок входа через соцсети
def test_click_icons_social_network(web_browser):
    """Тecт проверки наличия и кликабельности иконок входа через соцсети."""
    page = AuthPage(web_browser)
    page.ya_icon.find()
    assert page.ya_icon.is_visible() and page.ya_icon.is_clickable()
    page.mail_icon.find()
    assert page.mail_icon.is_visible() and page.mail_icon.is_clickable()
    page.ok_icon.find()
    assert page.ok_icon.is_visible() and page.ok_icon.is_clickable()
    page.vk_icon.find()
    assert page.vk_icon.is_visible() and page.vk_icon.is_clickable()
