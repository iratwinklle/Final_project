import pytest
from selenium import webdriver
import unittest
from pages.labirint import MainPage
import time

#запуск кода:pytest -v --driver Chrome --driver-path C:\use_python\chromedriver


def test_searching_with_correct_data(web_browser):
    """ Проверка, что поиск товаров работает нормально. 1"""
    page = MainPage(web_browser)
    page.search = 'Пушкин'
    page.search_run_button.click()
     # Проверяем, что пользователь может видеть список товаров:
    assert page.search_results.count() >= 1
     # Проверяем, что пользователь нашел соответствующие товары:
    for title in page.search_results.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'пушкин' in title.lower(), msg


def test_searching_with_simbols(web_browser):
    """ Проверка, что при вводе символов
    поиск работает нормально и выдает ошибку. """
    page = MainPage(web_browser)
    # Попробовать ввести несколько знаков:
    page.search = '%!*'
    page.search_run_button.click()
    # Проверяем, что в списоке нет найденных товаров:
    assert page.search_results.count() == 0
    # Проверяем, что появилось сообщение, что ничего не найдено:
    assert page.search_error.get_text() == "Мы ничего не нашли по вашему запросу! Что делать?"


def test_searching_incorrect_keyboard_layout(web_browser):
    """ Проверка, что при вводе поискового запроса с неправильной раскладкой клавиатуры
#     поиск работает нормально """
    page = MainPage(web_browser)
    # ввести «Достоевский» в английской раскладке клавиатуры:
    page.search = 'Ljcnjtdcrbq'
    page.search_run_button.click()
    # Проверяем, что пользователь может видеть список товаров:
    assert page.search_results.count() >= 1
    # Проверяем первые несколько товаров, что пользователь нашел соответствующие запросу товары:
    for title in page.search_results.get_text()[0:20]:
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'достоевск' in title.lower(), msg


def test_searching_with_mistake_in_name(web_browser):
    '''Проверка, что при вводе данных с орфографиечскими ошибками
    поиск работает нормально'''
    page = MainPage(web_browser)
    #ввести "Джек Лундон"
    page.search = 'Джек Лундон'
    page.search_run_button.click()
    # Проверяем, что пользователь может видеть список товаров:
    assert page.search_results.count() >= 1
    # Проверяем первые несколько товаров соответвуют запросу пользователя:
    for title in page.search_results.get_text()[0:5]:
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'лондон' in title.lower(), msg


def test_result_searching_electronic_product_type_correct(web_browser):
    '''Проверяем, что установка фильтра "Электронные книги" в фильтре "тип товара"
    в результатах поиска работает корректно'''
    page = MainPage(web_browser)
    # ввести "Пушкин"
    page.search = 'Пушкин'
    page.search_run_button.click()
    page.search_product_type.click()
    #убираем из результатов поиска бумажные книги и другие товары (чтобы остались только "Электронные книги")
    page.search_product_type_paper_books.click()
    page.search_product_type_another_products.click()
    page.search_product_type_show_button.click()
    time.sleep(5)
    # Проверяем, что пользователь может видеть список книг:
    assert page.search_results.count() >= 1
    # Проверяем, что пользователь нашел товары соответсвующие фильтру "Электронные книги":
    for title in page.search_product_type_electronic_books.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'электронная книга"' in title.lower(), msg


def test_result_searching_paper_product_type_correct(web_browser):
    '''Проверяем, что установка фильтра "Бумажные книги" в фильтре "Тип товара"
    в результатах поиска работает корректно'''
    page = MainPage(web_browser)
    # ввести "Пушкин"
    page.search = 'Пушкин'
    page.search_run_button.click()
    page.search_product_type.click()
    #убираем из результатов поиска электронные книги и другие товары (чтобы остались только "Электронные книги")
    page.search_product_type_electronic_books.click()
    page.search_product_type_another_products.click()
    page.search_product_type_show_button.click()
    time.sleep(5)
    # Проверяем, что пользователь может видеть список товаров:
    assert page.search_results.count() >= 1
    # Проверяем, что "Электронные книги" отсутвуют в списке товаров:
    for title in page.search_product_type_electronic_books.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'электронная книга"' not in title.lower(), msg


def test_result_searching_sale_price(web_browser):
    '''Проверка корректной работы поиска товаров по фильтру "Цена со скидкой" '''
    page = MainPage(web_browser)
    page.search = 'Джордж Мартин'
    page.search_run_button.click()
    #устанавливаем фильтр о поиске товаров со скидкой
    page.search_filter_price.click()
    page.search_filter_price_with_sale.click()
    page.search_filter_price_run_button.click()
    # Проверяем, что пользователь видит товары со скидкой:
    assert page.search_results.count() >= 1
    assert "Выгода" in page.search_results_contain_profit_in_price.get_text()


def test_result_searching_filter_exclution(web_browser):
    '''Проверка корректной работы поиска товаров, при использовании
     кнопок исключения из результатов поиска разных категорий товаров'''
    page = MainPage(web_browser)
    page.search = 'Пушкин'
    page.search_run_button.click()
    page.search_product_type.click()
    #убираем из результатов поиска бумажные книги и другие товары (чтобы остались только "Электронные книги")
    page.without_paper_books_button.click()
    page.without_others_products_button.click()
    time.sleep(5)
    # Проверяем, что пользователь может видеть список книг:
    assert page.search_results.count() >= 1
    # Проверяем книг, что пользователь нашел товары соответсвующие фильтру "Электронные книги":
    for title in page.search_product_type_electronic_books.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'электронная книга"' in title.lower(), msg


def test_correct_adding_product_in_basket(web_browser):
    '''Проверка корректного добавления выбранного товара на главной странице в корзину'''
    page = MainPage(web_browser)
    # запомним  название товара на главной странице, который будем добавлять в корзину
    name1 = page.first_book_mainpage_booksalesection_name.get_text()
    page.first_book_mainpage_basket_button.click()
    page.my_basket.click()
    # запоминаем название товара в корзине
    name2 = page.my_basket_first_book_name.get_text()
    time.sleep(7)
    #Проверяем, что в корзине есть товары
    assert page.my_basket_book_name.count() >= 1
    #Проверяем, что название товара, который мы добавили в корзину, совпадает с тем, что находится в корзине
    assert name1 == name2


def test_correct_adding_search_product_in_busket(web_browser):
    '''Проверка корректного добавления товара, найденного через поиск, в корзину. 10'''
    page = MainPage(web_browser)
    # находим товар через поисковую строку
    page.search = 'белый клык'
    page.search_run_button.click()
    # запоминаем название товара, который добавим в корзину
    name1 = page.search_result_name_first_book.get_text()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    # запоминаем название товара в корзине
    name2 = page.my_basket_first_book_name.get_text()
    #Проверяем, что в корзине есть книги
    assert page.my_basket_book_name.count() >= 1
    #Проверяем, что названия книги, которую мы добавили в корзину совпадает с тем, что находится в корзине
    assert name1 == name2


def test_correct_empty_basket(web_browser):
    '''Проверка корректного очищения корзины'''
    page = MainPage(web_browser)
    #находим и добавляем в корзину товар
    page.search = 'сказки пушкина'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    # запоминаем число товаров в корзине до очищения
    before = page.my_basket_quant_of_books_info.get_text()
    page.my_basket_empty_button.click()
    #проверяем, что до очищения в корзине были товары
    assert int(before) > 0
    #проверяем, что после очищения корзина пуста
    assert "ваша корзина пуста" in page.my_basket_empty_message.get_text().lower()


def test_correct_empty_basket(web_browser):
    '''Проверка корректного восстановления удаленных из корзины товаров'''
    page = MainPage(web_browser)
    #находим и добавляем в корзину выбранный товар
    page.search = 'европа'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    # запоминаем название товара до очищения корзины
    before = page.my_basket_first_book_name.get_text()
    page.my_basket_empty_button.click()
    empty_message = page.my_basket_empty_message.get_text().lower()
    #восстанавлиев все удаленные товары
    page.my_basket_restore_deleted_button.click()
    # запоминаем название товара после восстановления корзины
    after = page.my_basket_first_book_name.get_text()
    #проверяем, что корзина точно была очищена
    assert "ваша корзина пуста" in empty_message
    #проверяем, что после восстановления в корзине есть книги
    assert page.my_basket_book_name.count() >= 1
    #проверяем, что книги до очищения корзины, и после восстановления одинаковые
    assert before == after


def test_correct_open_page_ordering(web_browser):
    '''Проверка открытия страницы начала оформления заказа'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    #находим и добавляем в корзину выбранную книгу
    page.search = 'властелин колец'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(3)
    # нажимаем на кнопку "перейти к оформлению"
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    assert "Оформление заказа" in page.page_title.get_text()


def test_correct_ordering_delivery_page(web_browser):
    '''Проверка открытия страницы с выбором места и способа доставки при оформлении заказа'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    #находим и добавляем в корзину выбранную книгу
    page.search = 'властелин колец'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    #переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # открываем страницу "выбрать новое место и способ доставки"
    page.ordering_change_delivery_address.click()
    time.sleep(3)
    assert "Адрес места доставки" in page.delivery_address_field_name.get_text()


def test_correct_ordering_selfdelivery_choice_(web_browser):
    '''Проверка корректной работы выбора места и способа доставки самовывоз
    при оформлении заказа'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    #находим и добавляем в корзину выбранную книгу
    page.search = 'властелин колец'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    #переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # нажимаем на кнопку "выбрать новое место и способ доставки"
    page.ordering_change_delivery_address.click()
    time.sleep(3)
    page.delivery_address_field = 'Дворцовая площадь 10 Санкт-Петербург'
    time.sleep(4)
    # выбираем способ доставки "самовывоз"
    page.shipping_methods_self_delivery.click()
    time.sleep(1)
    # выбираем пункт доставки
    page.self_delivery_first_pick_up_point.click()
    # Нажимаем на кнопку "Заберу отсюда" в окне выбора способа доставки
    page.delivery_pick_up_run_button.click()
    #проверяем, что после выбора способа и метода доставки мы вернулись на страницу "оформление заказа"
    assert "Оформление заказа" in page.page_title.get_text()
    #проверяем, что способо доставки выбран
    assert "самовывоз" in page.ordering_page_info_about_selfdelivery.get_text()


def test_correct_ordering_courierdelivery_choice(web_browser):
    '''Проверка корректной работы выбора места и способа доставки курьер
    при оформлении заказа'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    #находим и добавляем в корзину выбранный товар
    page.search = 'властелин колец'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    # переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # нажимаем на кнопку "выбрать новое место и способ доставки"
    page.ordering_change_delivery_address.click()
    time.sleep(3)
    page.delivery_address_field = 'Дворцовая площадь 10 Санкт-Петербург'
    time.sleep(4)
    #выбираем способ доставки "курьер"
    page.shipping_method_courier_delivery.click()
    time.sleep(1)
    # выбираем службу доставки
    page.courier_delivery_first_courier_point.click()
    # Кнопка "Выбрать эту доставку" в окне выбора способа доставки
    page.delivery_pick_up_run_button.click()
    # проверяем, что после выбора способа и метода доставки мы вернулись на страницу "оформление заказа"
    assert "Оформление заказа" in page.page_title.get_text()
    # проверяем, что способо доставки выбран
    assert "курьер" in page.ordering_page_info_about_selfdelivery.get_text()


def test_error_mess_ordering_delivery_simbols(web_browser):
    '''Проверка появления сообщения об ошибке
    при вводе символов в поле адреса доставки при оформления заказа'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    # находим и добавляем в корзину выбранный товар
    page.search = 'география'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    # Переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # нажимаем на кнопку "выбрать новое место и способ доставки"
    page.ordering_change_delivery_address.click()
    time.sleep(3)
    #в строку адреса вводим некорректные данные
    page.delivery_address_field = '@#$%^'
    page.shipping_method_courier_delivery.click()
    # проверяем, что появилось сообщение об ошибке
    assert "Уточните адрес" in page.delivery_address_error_address.get_text()


def test_error_mess_ordering_delivery_digits(web_browser):
    '''Проверка появления сообщения об ошибке
    при вводе цифр в поле адреса доставки при оформления заказа'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    # находим и добавляем в корзину выбранный товар
    page.search = 'география'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    # Переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # нажимаем на кнопку "выбрать новое место и способ доставки"
    page.ordering_change_delivery_address.click()
    time.sleep(3)
    # в строку адреса вводим некорректные данные
    page.delivery_address_field = '111111111111111111111111111111'
    page.shipping_method_courier_delivery.click()
    # проверяем, что появилось сообщение об ошибке
    assert "Уточните адрес" in page.delivery_address_error_address.get_text()


def test_error_mess_ordering_delivery_english(web_browser):
    '''Проверка появления сообщения об ошибке при вводе адреса
    с неправильной раскладкой клавиатуры в поле адреса доставки при оформления заказа'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    # находим и добавляем в корзину выбранную книгу
    page.search = 'география'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    # Переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # нажимаем на кнопку "выбрать новое место и способ доставки"
    page.ordering_change_delivery_address.click()
    time.sleep(3)
    # в строку адреса вводим некорректные данные
    page.delivery_address_field = 'ghjcgtrn ktybyf 37 gtnhjpfdjlcr'
    page.shipping_method_courier_delivery.click()
    # проверяем, что появилось сообщение об ошибке
    assert "Уточните адрес" in page.delivery_address_error_address.get_text()


def test_order_error_message_name(web_browser):
    '''Проверка появления сообщения об ошибке
     при вводе неверного имени нового пользователя в поле "Имя" на странице Оформление заказа. 20'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    # находим и добавляем в корзину выбранную книгу
    page.search = 'физика'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    # Переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # вводим символы в поле "Имя"
    page.ordering_field_name_new_user = "##%%^"
    # заполняем остальные поля данных Пользователя корректными данными
    page.ordering_field_surname_new_user = "Иванов"
    page.ordering_field_email_new_user = "oleg.ivanov@gmail.com"
    page.ordering_field_phone_new_user = "9114102121"
    page.ordering_place_an_order_button.click()
    # проверяем, что мы находимся на странице "оформление заказа"
    assert "Оформление заказа" in page.page_title.get_text()
    # проверяем, что появилось сообщение об ошибке
    assert "разрешены только буквы" in page.ordering_error_message.get_text().lower()


def test_order_error_message_emptyname(web_browser):
    '''Проверка появления сообщения об ошибке
     при незаполнении поля "Имя" на странице Оформление заказа'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    # находим и добавляем в корзину выбранную книгу
    page.search = 'физика'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    # Переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # оставляем поле "Имя"  незаполненным
    page.ordering_field_name_new_user = ""
    # заполняем поля данных Пользователя корректными данными
    page.ordering_field_surname_new_user = "Иванов"
    page.ordering_field_email_new_user = "oleg.ivanov@gmail.com"
    page.ordering_field_phone_new_user = "9114102121"
    page.ordering_place_an_order_button.click()
    # проверяем, что мы находимся на странице "оформление заказа"
    assert "Оформление заказа" in page.page_title.get_text()
    # проверяем, что появилось сообщение об ошибке
    assert "имя обязательно" in page.ordering_error_message.get_text().lower()


def test_order_error_message_emptysurname(web_browser):
    '''Проверка появления сообщения об ошибке
     при незаполнении поля "Фамилия" на странице Оформление заказа'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    # находим и добавляем в корзину выбранную книгу
    page.search = 'физика'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    # Переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # оставляем поле "Фамилия"  незаполненным
    page.ordering_field_surname_new_user = ""
    # заполняем поля данных Пользователя корректными данными
    page.ordering_field_name_new_user = "Олег"
    page.ordering_field_email_new_user = "oleg.ivanov@gmail.com"
    page.ordering_field_phone_new_user = "9114102121"
    page.ordering_place_an_order_button.click()
    # проверяем, что мы находимся на странице "оформление заказа"
    assert "Оформление заказа" in page.page_title.get_text()
    # проверяем, что появилось сообщение об ошибке
    assert "фамилия обязательна" in page.ordering_error_message.get_text().lower()


def test_order_error_message_emptyphone(web_browser):
    '''Проверка появления сообщения об ошибке
     при незаполнении поля "Мобильный телефон" на странице Оформление заказа'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    # находим и добавляем в корзину выбранную книгу
    page.search = 'химия'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    # Переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # заполняем поля данных Пользователя корректными данными
    page.ordering_field_name_new_user = "Олег"
    page.ordering_field_surname_new_user = "Попов"
    page.ordering_field_email_new_user = "oleg.ivanov@gmail.com"
    # оставляем поле "email"  незаполненным
    page.ordering_field_phone_new_user = ""
    page.ordering_place_an_order_button.click()
    # проверяем, что мы находимся на странице "оформление заказа"
    assert "Оформление заказа" in page.page_title.get_text()
    # проверяем, что появилось сообщение об ошибке
    assert "телефон обязателен" in page.ordering_error_message.get_text().lower()


def test_correct_order_error_message_phone(web_browser):
    '''Проверка появления сообщения об ошибке при вводе неверного номера телефона
    в поле "Мобильный телефон" на странице Оформление заказа'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    # находим и добавляем в корзину выбранную книгу
    page.search = 'биология'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    # Переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # заполняем поля данных Пользователя корректными данными
    page.ordering_field_name_new_user = "Олег"
    page.ordering_field_surname_new_user = "Иванов"
    page.ordering_field_email_new_user = "oleg.ivanov@gmail.com"
    # вводим в поле "Мобильный телефон" некорректное значение
    page.ordering_field_phone_new_user = "1111111111111111111111111111111111"
    page.ordering_place_an_order_button.click()
    # проверяем, что мы находимся на странице "оформление заказа"
    assert "Оформление заказа" in page.page_title.get_text()
    # проверяем, что появилось сообщение об ошибке
    assert "ошибка в номере телефона" in page.ordering_error_message.get_text().lower()


def test_correct_verify_phone_page_start(web_browser):
    '''Проверка открытия страницы  "Подтверждение телефона" при оформлении заказа '''
    page = MainPage(web_browser)
    page.button_cookie.click()
    # находим и добавляем в корзину выбранную книгу
    page.search = 'биология'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    # Переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # заполняем поля данных Пользователя корректными данными
    page.ordering_field_name_new_user = "Олег"
    page.ordering_field_surname_new_user = "Иванов"
    page.ordering_field_email_new_user = "oleg.ivanov@gmail.com"
    page.ordering_field_phone_new_user = "9114010103"
    #нажимаем на кнопку "Проверить" рядом с полем мобильного телефона
    page.ordering_button_verify_phone.click()
    # проверяем, что открылось окно "Подтверждение телефона"
    assert "Подтверждение телефона" in page.verify_phone_title.get_text()


def test_order_error_message_without_at_email(web_browser):
    '''Проверка появления сообщения об ошибке
     при вводе электронной почты без символа @ в поле "Электронная почта" на странице Оформление заказа'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    # находим и добавляем в корзину выбранную книгу
    page.search = 'биология'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    # Переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # заполняем поля данных Пользователя корректными данными
    page.ordering_field_name_new_user = "Олег"
    page.ordering_field_surname_new_user = "Иванов"
    page.ordering_field_phone_new_user = "9119119191"
    # вводим в поле "email" некорректное значение (без @)
    page.ordering_field_email_new_user = "oleg.ivanovgmail.com"
    page.ordering_place_an_order_button.click()
    # проверяем, что мы находимся на странице "оформление заказа"
    assert "Оформление заказа" in page.page_title.get_text()
    # проверяем, что появилось сообщение об ошибке
    assert "ошибка в адресе почты" in page.ordering_error_message_email.get_text().lower()


def test_order_error_message_empty_email(web_browser):
    '''Проверка появления сообщения об ошибке
     при  незаполнении поля "email" на странице Оформление заказа'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    # находим и добавляем в корзину выбранную книгу
    page.search = 'птицы'
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    # заполняем поля данных Пользователя корректными данными
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # заполняем поля данных Пользователя
    page.ordering_field_name_new_user = "Олег"
    page.ordering_field_surname_new_user = "Иванов"
    page.ordering_field_phone_new_user = "9119119191"
    # оставляем поле "email" пустым
    page.ordering_field_email_new_user = ""
    page.ordering_place_an_order_button.click()
    # проверяем, что мы находимся на странице "оформление заказа"
    assert "Оформление заказа" in page.page_title.get_text()
    # проверяем, что появилось сообщение об ошибке
    assert "почта обязательна" in page.ordering_error_message_email.get_text().lower()


def test_correct_order_error_message_russian_email(web_browser):
    '''Проверка появления сообщения об ошибке при вводе в поле "Электронная почта"
    значения на русском языке на странице Оформление заказа.'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    page.search = 'птицы'
    # находим и добавляем в корзину выбранную книгу
    page.search_run_button.click()
    page.search_result_first_book_in_basket_button.click()
    page.my_basket.click()
    time.sleep(2)
    # Переходим к оформлению заказа
    page.my_basket_ordering_run_button.click()
    time.sleep(3)
    # заполняем поля данных Пользователя корректными данными
    page.ordering_field_name_new_user = "Олег"
    page.ordering_field_surname_new_user = "Иванов"
    page.ordering_field_phone_new_user = "9119119191"
    # заполняем поле "email" значением на русском языке
    page.ordering_field_email_new_user = "почта@мэйл.ру"
    page.ordering_place_an_order_button.click()
    # проверяем, что мы находимся на странице "оформление заказа"
    assert "Оформление заказа" in page.page_title.get_text()
    # проверяем, что появилось сообщение об ошибке
    assert "ошибка в адресе почты" in page.ordering_error_message_email.get_text().lower()


def test_correct_open_page_book(web_browser):
    '''Проверка корректного открытия раздела "Книги" в хэдере сайта'''
    page = MainPage(web_browser)
    page.section_books_header.click()
    #проверяем, что открылся нужный раздел
    assert "Книги" in page.page_title.get_text()


def test_correct_open_book_section_child_time(web_browser):
    '''Проверка корректного открытия подподраздела "Десткий досуг" выпадающего списка подраздела
    "Книги для детей"  раздела "Книги" в хэдере сайта. 30'''
    page = MainPage(web_browser)
    page.section_books_header.right_mouse_click()
    page.subsection_books_for_children.right_mouse_click()
    page.sub_subsection_child_time.click()
    # проверяем, что открылся нужный раздел
    assert "Детский досуг" in page.genre_page_title_name.get_text()


def test_correct_open_book_section_main_2022(web_browser):
    '''Проверка корректного открытия подраздела
    "Главное 2022"  выпадающего списка раздела "Книги" в хэдере сайта'''
    page = MainPage(web_browser)
    page.section_books_header.right_mouse_click()
    page.subsection_books_main_2022.click()
    #проверяем, что открылся нужный раздел
    assert "Главные книги" in page.page_title.get_text()


def test_correct_open_page_school(web_browser):
    '''Проверка корректного открытия страницы "Школа"  в хэдере сайта'''
    page = MainPage(web_browser)
    page.section_school.click()
    # проверяем, что открылся нужный раздел
    assert "Все учебники в Лабиринте" in page.school_title.get_text()


def test_correct_open_page_office_supplier(web_browser):
    '''Проверка корректного открытия  страницы "Канцелярские товары"
    выпадающего списка раздела "Книги" в хэдере сайта'''
    page = MainPage(web_browser)
    page.section_office_supplier.click()
    # проверяем, что открылся нужный раздел
    assert "Канцелярские товары" in page.genre_page_title_name.get_text()


def test_correct_open_page_toys(web_browser):
    '''Проверка корректного открытия страницы "Игрушки"   в хэдере сайта'''
    page = MainPage(web_browser)
    page.section_toys.click()
    # проверяем, что открылся нужный раздел
    assert "Игры и игрушки" in page.genre_page_title_name.get_text()

def test_correct_open_page_householder_goods(web_browser):
    '''Проверка корректного открытия страницы "Товары для дома" в хэдере сайта через кнопку "Еще"'''
    page = MainPage(web_browser)
    page.section_else_header.click()
    page.section_else_household_goods.click()
    # проверяем, что открылся нужный раздел
    assert "Товары для дома" in page.genre_page_title_name.get_text()


def test_correct_open_auth_my_lab(web_browser):
    '''Проверка открытия окна авторизации "Мой Лабиринт" в хэдере страницы'''
    page = MainPage(web_browser)
    page.my_Lab.click()
    # проверяем, что открылся нужный раздел
    assert 'Полный доступ к Лабиринту' in page.my_Lab_title.get_text()


def test_correct_open_postpond_page(web_browser):
    '''Проверка открытия окна "Отложенные товары" в хэдере страницы'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    page.postponed.click()
    # проверяем, что открылся нужный раздел
    assert '/cabinet/putorder/' in page.get_current_url()


def test_correct_add_postpond_page(web_browser):
    '''Проверка добавления книги в "отложенные товары"'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    time.sleep(3)
    # запомним название книги, которую добавим в "Отложенные товары"
    name1 = page.first_book_mainpage_booksalesection_name.get_text()
    page.first_book_mainpage_booksalesection_name.click()
    page.postponed_book_button.click()
    page.postponed.click()
    # запоминаем название книги, которая находится на странице "Отложено"
    name2 = page.postponed_name_book.get_text()
    # проверяем, что открылся раздел "отложенные книги"
    assert '/cabinet/putorder/' in page.get_current_url()
    # Проверяем, что названия книги, которую мы отложили совпадает с тем, что находится в разделе "отложенные товары"
    assert name1 == name2


def test_correct_add_and_clear_postpond_page(web_browser):
    '''Проверка очищения раздела "отложенные товары"'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    time.sleep(3)
    # запомним название книги, которую добавим в "Отложенные товары"
    name1 = page.first_book_mainpage_booksalesection_name.get_text()
    page.first_book_mainpage_booksalesection_name.click()
    page.postponed_book_button.click()
    page.postponed.click()
    # запоминаем название книги, которая находится на странице "Отложено"
    name2 = page.postponed_name_book.get_text()
    count_before_clean = page.postponed_name_books.count()
    #нахимаем на кнопку "Очистить" на странице "Отложенные товары"
    page.postponed_clear_all_putorder.click()
    count_after_clear = page.postponed_name_books.count()
    # проверяем, что открылся раздел "отложенные книги"
    assert '/cabinet/putorder/' in page.get_current_url()
    # Проверяем, что названия книги, которую мы отложили совпадает с тем, что находится в разделе "отложенные товары"
    assert name1 == name2
    #сравниваем, что число книг до очищения больше чем после
    assert count_before_clean > count_after_clear
    #проверяем, что в разделе нет книг после очищения страницы "отложенные товары"
    assert count_after_clear == 0


def test_correct_open_delivery_and_payment_page(web_browser):
    '''Проверка корректного открытия раздела "Доставка и оплата" в сером горизонтальном меню хэдера 40'''
    page = MainPage(web_browser)
    page.delivery_and_payment_button.click()
    # проверяем, что открылся нужный раздел
    assert "Доставка" in page.delivery_part.get_text()


def test_correct_open_delivery_page(web_browser):
    '''Проверка корректного открытия раздела "Доставка" раздела "Доставка и оплата" в сером горизонтальном меню хэдера'''
    page = MainPage(web_browser)
    page.delivery_and_payment_button.click()
    page.delivery_part.click()
    # проверяем, что открылся нужный раздел
    assert "Все способы доставки" in page.all_delivery_methods.get_text()


def test_correct_open_dhl_delivery(web_browser):
    '''Проверка корректного открытия раздела "Экспресс-доставка DHL" раздела
    "Доставка и оплата" в сером горизонтальном меню хэдера'''
    page = MainPage(web_browser)
    page.delivery_and_payment_button.click()
    page.delivery_part.click()
    page.delivery_by_DHL.click()
    # проверяем, что открылся нужный раздел
    assert "Экспресс-доставка DHL" in page.DHL_title_name.get_text()


def test_delivery_and_payment_searching_with_correct_data(web_browser):
    '''Проверка корректной работы "Поиска по помощи" на странице "Доставка и оплата"'''
    page = MainPage(web_browser)
    page.delivery_and_payment_button.click()
    # в поисковую строку вводим корректный запрос
    page.help_searching_field = "юридические лица"
    page.help_searching_run_button.click()
    #проверяем, что пользователь может видеть результаты поискового запроса
    assert page.help_searching_titles_name.count() >= 1


def test_delivery_and_payment_searching_with_wrong_keyboard(web_browser):
    '''Проверка, появления сообщения об отсутвии результатов поиска
    при вводе запроса с неправильной раскладкой клавиатуры
    на странице "Доставка и оплата"'''
    page = MainPage(web_browser)
    page.delivery_and_payment_button.click()
    # в поисковую строку вводим корректный запрос
    page.help_searching_field = "ljcnfdrf rehmthjv"
    page.help_searching_run_button.click()
    # проверяем, что появилось сообщение об ошибке
    assert "Сообщение" in page.help_searching_error_message.get_text()


def test_delivery_and_payment_searching_with_symbols(web_browser):
    '''Проверка, появления сообщения об отсутвии результатов поиска
    при вводе символов на странице "Доставка и оплата"'''
    page = MainPage(web_browser)
    page.delivery_and_payment_button.click()
    page.help_searching_field = "№;%:?"
    page.help_searching_run_button.click()
    # проверяем, что появилось сообщение об ошибке
    assert "Сообщение" in page.help_searching_error_message.get_text()


def test_delivery_and_payment_searching_with_numbers(web_browser):
    '''Проверка, появления сообщения об отсутвии результатов поиска
    при вводе чисел на странице "Доставка и оплата"'''
    page = MainPage(web_browser)
    page.delivery_and_payment_button.click()
    page.help_searching_field = "129847465"
    page.help_searching_run_button.click()
    # проверяем, что появилось сообщение об ошибке
    assert "Сообщение" in page.help_searching_error_message.get_text()


def test_correct_open_rating_page(web_browser):
    '''Проверка корректного открытия раздела "Рейтинги" в сером горизонтальном меню хэдера'''
    page = MainPage(web_browser)
    page.rating.click()
    # проверяем, что открылся нужный раздел
    assert "Рейтинг" in page.page_title.get_text()


def test_correct_open_footer_tests(web_browser):
    '''Проверка, что кнопка "Тесты" в футере страницы ведет на страницу "Литературные тесты"'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    page.down_element.scroll_to_element()
    time.sleep(2)
    page.footer_tests.click()
    # проверяем, что открылся нужный раздел
    assert "Литературные тесты" in page.tests_title_name.get_text()


def test_correct_open_footer_how_order(web_browser):
    '''Проверка, что кнопка "Как сделать заказ" в футере страницы ведет на страницу "Поиск по Помощи"'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    page.down_element.scroll_to_element()
    time.sleep(2)
    page.footer_how_do_order.click()
    # проверяем, что открылся нужный раздел
    assert "Поиск по Помощи" in page.help_searching_title.get_text()


def test_footer_open_labirint_holding(web_browser):
    '''Проверка перехода на сайт издательского дома "лабиринт" из футера сайта. 50'''
    page = MainPage(web_browser)
    page.button_cookie.click()
    page.down_element.scroll_to_element()
    page.footer_Lab_holding.click()
    page.switch_to_window(window_number=1)
    #проверяем, что пользователь оказался на нужном стороннем ресурсе
    assert page.get_current_url() == 'https://www.labirint.org/'


# def test_footer_open_vk(web_browser):
#     '''Проверка перехода в группу "Лабиринта" в Вконтакте из футера сайта'''
#     page = MainPage(web_browser)
#     page.button_cookie.click()
#     page.down_element.scroll_to_element()
#     page.footer_vk.click()
#     page.switch_to_window(window_number=1)
#     # проверяем, что пользователь оказался на нужном стороннем ресурсе
#     assert page.get_current_url() == 'https://vk.com/labirintru'