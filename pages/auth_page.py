from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = url if url else 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    # Test-001
    logo = WebElement(class_name='main-header__logo')
    up_page = WebElement(id='app-header')

    # Test-002
    left_side = WebElement(id='page-left')
    left_logo = WebElement(class_name='what-is-container__logo')
    left_title = WebElement(class_name='what-is__title')
    left_slogan = WebElement(class_name='what-is__desc')

    # Test-003
    right_side = WebElement(id='page-right')
    name_form = WebElement(class_name='card-container__title')
    form_container = WebElement(class_name='card-container__wrapper')

    # Test-004
    registration_link = WebElement(id='kc-register')

    # Test-005
    forgot_passw_link = WebElement(id='forgot_password')
    reset_back_button = WebElement(id='reset-back')

    # Test-006
    name_menu_phone = WebElement(id='t-btn-tab-phone')
    name_menu_mail = WebElement(id='t-btn-tab-mail')
    name_menu_login = WebElement(id='t-btn-tab-login')
    name_menu_ls = WebElement(id='t-btn-tab-ls')
    login_input = WebElement(id='username')  # поле логин
    name_login = ManyWebElements(class_name='rt-input__placeholder')
    password_input = WebElement(id='password')
    btn_enter = WebElement(id='kc-login')

    # Test-007
    checkbox = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[3]/div')
    checkbox_checked = WebElement(class_name='rt-checkbox--checked')

    # Test-009
    captcha = WebElement(xpath='//*[@id="captcha"]')
    last_name = WebElement(class_name='user-name__last-name')  # Фамилия в личном кабинете после авторизации
    form_error = WebElement(id='form-error-message')
    card_title = ManyWebElements(class_name='card-title')

    # Test-010
    login_error = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    get_login_input = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/input[2]')  # то, что остается в поле логин, после ввода

    # Test-021
    card_modal = WebElement(class_name='card-modal__card-wrapper')
    card_modal_title = WebElement(class_name='card-modal__title')  # Учётная запись уже существует
    name_input = WebElement(name='firstName')
    last_name_input = WebElement(name='lastName')
    email_or_phone = WebElement(id='address')
    password_registration = WebElement(id='password')
    password_confirmation = WebElement(id='password-confirm')
    btn_registration = WebElement(name='register')

    # Test-023
    vk_icon = WebElement(id='oidc_vk')
    ok_icon = WebElement(id='oidc_ok')
    mail_icon = WebElement(id='oidc_mail')
    ya_icon = WebElement(id='oidc_ya')
