Финальный тестовый проект SkillFactory курса QAP

Автоматизированное тестирование сайта: https://www.labirint.ru/ с использованием PyTest и Selenium.


1. С тест-кейсами можно ознакомиться в папке files

2. В папке pages файл base.py содержит реализацию шаблона PageObject для Python
3. В папке pages файл elements.py содержит вспомогательный класс для определения веб-элементов на веб-страницах
4. В папке pages файл conftest.py содержит код для отлова неудачных тестовых случаев и создания скриншота страницы в случае, если какой-либо тест не сработает.

5. В папке pages в файле locators.py находятся локаторы элементов сайта, используемых при тестировании

6. В корне проекта в файле requirements.py описаны используемые библиотеки.

7. В папке tests в файлe test_labirint.py находится 51 тест для сайта онлайн-магазина "Лабиринт" 

Файлы base.py, elements.py, conftest.py взяты из репозитория библиотеки https://github.com/TimurNurlygayanov/ui-tests-example (который использовался при выполнении практики по 26 модулю курса QAP).

Для запуска тестов необходимо загрузить Selenium WebDriver с https://chromedriver.chromium.org/downloads (версию, совместимую с используемым браузером) Запускать тесты необходимо в консоли командой: python3 -m pytest -v --driver Chrome --driver-path /<chromedriver_file> tests/test_labirint.py





