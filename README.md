# Итоговый проект по автоматизации тестирования
Данные тесты проверяют объект тестирования: https://b2c.passport.rt.ru

# Структура проекта:
    README.md - содержит информацию о проекте.
    сonftest.py - описание фикстур для проекта.
    requirements.txt - список внешних зависимостей.
    .env - прописаны значения ключей
    settings - описаны используемые ключи

    Директория pages содержит:
    • base_page.py - описание базовых методов.
    • elements.py - описание методов для элементов.
    • auth_page.py - инициализация и описание локаторов проекта.
    • for_tests.py - дополнительные функции, которые используются в проекте
    
    Директория tests содержит:
    • test_auth_page.py - набор тестов для страницы авторизации проекта.

# Настройка проекта:
    1. Создаем виртуапльное окружение командой:
        python -m venv venv
    2. Активируем виртуальное окружение командой (MacOS/Linux):
        source venv/bin/activate
       для Windows другая команда:
        \env\Scripts\activate.bat
    3. Установка зависимостей:
        pip install -r requirements.txt
    4. Настроить в IDE(Pycharm) текущий интерпритатор, выбрав текущее вертуальное окружение

# Запуск тестов:
    1. Нажмите на зеленую стрелочку слева от названия теста, если она вдруг не появилась, 
    значит вы не установили библиотеку pytest. Установите командой: pip install pytest.
    2. Для визуализации тестов (включение UI) необходимо выключить режим headless в файле conftest.
    3. Настроены под запуск с Google Chrome 116.0.5845.97 (64-bit)
