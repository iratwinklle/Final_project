#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os, pickle

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)
        # with open('my_cookies.txt', 'rb') as cookiesfile:
        #     cookies = pickle.load(cookiesfile)
        #     for cookie in cookies:
        #         web_driver.add_cookie(cookie)
        #     web_driver.refresh();

    # Поле поиска "Поиск по Лабиринту" в хэдере главной странице
    search = WebElement(id='search-field')
    # Кнопка "Поиск" в поисковой стороке в хэдере главной странице
    search_run_button = WebElement(xpath='//button[@class="b-header-b-search-e-btn"]')
    button_cookie = WebElement(xpath='//button[contains(text(),"Принять")]')
    # Название книг в результатах поиска
    search_results = ManyWebElements(xpath='//a[@class="product-title-link"]')
    #название первой книги в результатах поиска
    search_result_name_first_book = WebElement(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/div/div[1]/div/div[1]/a/span')
    # кнопка "в корзину" под первой книгой в результатах поиска
    search_result_first_book_in_basket_button = WebElement(
        xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/div/div[1]/div/div[4]/div/div[1]')
    #названия авторов в результатах поиска
    search_results_authors = ManyWebElements(xpath='//div[@class="product-author"]/a/span')
    #Указатель "Электронная книга" в описании товара
    search_results_electronic_books = ManyWebElements(xpath='//*[contains(text(),"Электронная книга")]')
    # Сообщение об ошибке при неверном вводе поискового запроса
    search_error = WebElement(xpath='//*[@id="search"]/div[1]/h1')
    #Кнопка "Тип товара" в результатах поискового запроса
    search_product_type = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[1]/span/span/span[1]')
    #Строка "Бумажные книги в выпадающем списке кнопки "Тип товара" в результатах поиска
    search_product_type_paper_books = WebElement(
        xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[1]/span/span/span[2]/ul/li[1]/label')
    #Строка "Электронные книги в выпадающем списке кнопки "Тип товара" в результатах поиска
    search_product_type_electronic_books = WebElement(
        xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[1]/span/span/span[2]/ul/li[2]/label')
    #Строка "Другие товары" в выпадающем списке кнопки "Тип товара" в результатах поиска
    search_product_type_another_products = WebElement(
        xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[1]/span/span/span[2]/ul/li[3]/label')
    #Кнопка "Показать" в выпадающем списке кнопки "Тип товара" в результатах поиска
    search_product_type_show_button = WebElement(
        xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[1]/span/span/span[2]/ul/li[5]/input')


    #Кнопка "ЦЕНА" в результатах поискового запроса
    search_filter_price = WebElement(
        xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[3]/span/span/span[1]/span')
    #Фильтр "со скидкой" в выпадающем списке кнопки "ЦЕНА" в результатах поиска
    search_filter_price_with_sale = WebElement(
        xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[3]/span/span/span[2]/ul/li[2]/label')
    # Кнопка "Показать" в выпадающем списке кнопки "ЦЕНА" в результатах поиска
    search_filter_price_run_button = WebElement(
        xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[3]/span/span/span[2]/ul/li[4]/input')
    #"выгода" в цене товара
    search_results_contain_profit_in_price = WebElement(xpath='//span[@class="card-label__text card-label__text_inversed"]')


    # Кнопка "Все фильтры" в результатах поиска
    search_all_filters = WebElement(
        xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[5]/span/span/span/span')
    # в горизонтальном меню кнопка исключения из результатов поиска категории "Бумажные книги"
    without_paper_books_button = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[2]/div/div/a[1]/div')
    # в горизонтальном меню кнопка исключения из результатов поиска категории "Электронные книги"
    without_electronic_books_button = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[2]/div/div/a[1]/div')
    # в горизонтальном меню кнопка исключения из результатов поиска категории "Прочие товары"
    without_others_products_button = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[2]/div/div/a[2]/div')
    # в горизонтальном меню кнопка исключения из результатов поиска категории "В наличии"
    sort_products_by_type_in_stock_is = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"В наличии")]')
    # в горизонтальном меню кнопка исключения из результатов поиска категории "Предзаказ"
    sort_products_by_type_order = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Предзаказ")]')
    # в горизонтальном меню кнопка исключения из результатов поиска категории "Ожидаются"
    sort_products_by_type_waiting = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Ожидаются")]')


    # Разделы сайта в основном меню header на черном фоне
    section_titles = ManyWebElements(xpath='//a[contains(@class, "b-header-b-menu-e-text")]')


    # Раздел "Книги" в основном меню header на черном фоне
    section_books_header = WebElement(
        xpath='//*[@id="minwidth"]/div[4]/div/div[1]/div[4]/div/div[1]/ul/li[1]/span/a')
    # Подраздел "Книги для детей" в выпадающем списке раздела "Книги"
    subsection_books_for_children = WebElement(xpath='//*[@id="header-genres"]/div/ul/li[5]/span')
    #Подподраздел "Десткий досуг" выпадающего списка подраздела "Книги для детей"  раздела "Книги"
    sub_subsection_child_time = WebElement(xpath='//a[contains(text(), "Детский досуг")]')
    #Подраздел "Главные книги 2022" в выпадающем списке раздела "Книги"
    subsection_books_main_2022 = WebElement(xpath='//li/a[contains(text(), "Главное 2022")]')
    #заголовок страницы жанра книг
    genre_page_title_name = WebElement(xpath='//h1[@class="genre-name"]')
    # Раздел "Еще" в основном меню header на черном фоне
    section_else_header = WebElement(xpath='//span[@class="b-header-b-menu-e-text" and contains(text(), "Еще")]')
    #Раздел "Канцелярские товары" в выпадающем окне "Еще"
    section_office_supplier = WebElement(xpath='//*[@href="/office/" and @class="b-header-b-menu-e-text"]')
    # Раздел "Игрушки" в выпадающем окне "Еще"
    section_toys = WebElement(xpath='//*[@href="/games/" and @class="b-header-b-menu-e-text"]')
    # Раздел "Школа" в выпадающем окне "Еще"
    section_school = WebElement(xpath='//*[@href="/school/" and @class="b-header-b-menu-e-text"]')
    # Раздел "Товары для дома" в выпадающем окне "Еще"
    section_else_household_goods = WebElement(xpath='//*[@href="/household/" and @title="Товары для дома"]')
    # заголовок страницы "Школа"
    school_title = WebElement(xpath='//*[@class="school-cap__header"]')


    # Кнопка "Доставка и оплата" в сером горизонтальном меню хэдера
    delivery_and_payment_button = WebElement(xpath='//a[contains(text(), "Доставка и оплата")]')
    #Раздел "Доставка" в левом боковом меню на странице "Доставка и оплата"
    delivery_part = WebElement(
        xpath='//a[@id="aHelp" and @href="/help/?clause=1"]')
    #"Поиск по Помощи" на странице "Доставка и оплата"
    help_searching_field = WebElement(xpath='//input[@id="txtwordsadv"]')
    #Кнопка "Поиск" поля "Поиск по Помощи" на странице "Доставка и оплата"
    help_searching_run_button = WebElement(xpath='//input[@class="btn btn-small btn-primary"]')
    #название поля "Поиск по помощи" на странице "Достава и оплата"
    help_searching_title = WebElement(xpath='//span[@class="content-default bold mr10"]')
    #заголовки разделов под полем "Поиск по Помощи" на странице "Доставка и оплата"
    help_searching_titles_name = ManyWebElements(xpath='//*[@class="border-self link-color"]')
    # Сообщение о том, что поиск не дал результатов под полем "Поиск по Помощи" на странице "Доставка и оплата"
    help_searching_error_message = WebElement(xpath='//*[@id="messages-title-b"]')
    # Раздел "Оплата" в левом боковом меню на странице "Доставка и оплата"
    payment_part = WebElement(
        xpath='/html/body/div[1]/div[5]/div[4]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/a')
    #Подраздел "DHL" раздела "Доставка" на странице "Доставка и оплата"
    delivery_by_DHL = WebElement(
        xpath='/html/body/div[1]/div[5]/div[4]/div/div/div/div/div/div/div/div/div[1]/div/div[4]/div[2]/a')
    #"Все способы доставки" раздела "Доставка" на странице "Доставка и оплата"
    all_delivery_methods = WebElement(xpath='//a[@id="aHelp" and @href="/help/?clause=140"]')
    #Заголовок "Экспресс-доставка DHL" на странице подраздела "DHL" раздела "Доставка" на странице "Доставка и оплата"
    DHL_title_name = WebElement(id='jslikeurl41')


    # Кнопка "Рейтинги" в сером горизонтальном меню хэдера
    rating = WebElement(xpath='//*[@href="/rating/?id_genre=-1&nrd=1"]')
    #кнопка "Оценки" на странице "Рейтинги"
    rating_votes_button = WebElement(xpath='//*[@href="/rating/votes/"]')


    # название первого товара в разделе "Книжная распродажа" на главной странице
    first_book_mainpage_booksalesection_name = WebElement(
        xpath='//*[@id="bottom"]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[1]/a[2]/span[2]')
    # кнопка "В корзину" под первым товаром в разделе "Что почитать: выбор редакции" на главной странице
    first_book_mainpage_basket_button = WebElement(
        xpath='//*[@id="bottom"]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[1]')


    # ссылка "Что почитать: выбор редакции" на главной странице
    editor_s_choice = WebElement(xpath='//a[@href="/top/toread/" and @class="block-link-title"]')
    # названия книг в разделе "Что почитать: выбор редакции"
    books_editir_s_choice = ManyWebElements(xpath='//span[@class="product-title large-name"]')
    # заголовок страницы
    page_title = WebElement(xpath='//h1')


    # кнопка "Сертификаты" в горизонтальном меню главной страницы
    certificates_button = WebElement(
        xpath='//*[@id="minwidth"]/div[4]/div/div[2]/div/ul/li[2]/a')
    # содержание раздела на открывшейся странице "Сертификаты"
    section_content = WebElement(
        xpath='//div[@class="b-toppage-content  content-base top-read-area m0auto"]')


    # кнопка "Новинки" в горизонтальном меню главной страницы
    novelties_button = WebElement(
        xpath='//*[@id="minwidth"]/div[4]/div/div[2]/div/ul/li[4]/a')

    # кнопка "Скидки" в горизонтальном меню главной страницы
    discounts_books_button = WebElement(
        xpath='//*[@id="minwidth"]/div[4]/div/div[2]/div/ul/li[5]/a')

    # кнопка "Контакты" в горизонтальном меню главной страницы
    contacts_button = WebElement(
        xpath='//*[@id="minwidth"]/div[4]/div/div[2]/div/ul/li[9]/a')

    # кнопка "Поддержка" в горизонтальном меню главной страницы
    support_button = WebElement(
        xpath='//*[@id="minwidth"]/div[4]/div/div[2]/div/ul/li[10]/a')
    # название раздела на странице "Поддержка"
    section_title_support = WebElement(
        xpath='//a[@class="support-all active"]')

    #кнопка "Мой Лаб" на главной странице
    my_Lab = WebElement(
        xpath='//a[@class="b-header-b-personal-e-link top-link-main top-link-main_cabinet  js-b-autofade-wrap"]')
    #заголовок окна "Полный доступ к Лабиринту"
    my_Lab_title = WebElement(xpath='//*[@id="auth-by-code"]/div[1]')
    #Поле ввода номера телефона или email в окне "Полный доступ к Лабиринту"
    my_Lab_login = WebElement(id="_inputnamecode_35")
    #Чек-бокс о согласии с основными правилами сайта в окне "Полный доступ к Лабиринту"
    my_Lab_check_box = WebElement(xpath='//span[@class="custom-input__status custom-input__status_new-auth"]')
    my_Lab_email_window_message = WebElement(xpath='//*[@id="auth-email-sent"]/div[3]/span[3]/small')
    my_Lab_codefield_email_window = WebElement(xpath='//*[@id="_inputnamecode_7"]')
    #Кнопка "Войти" в окне "Полный доступ к Лабиринту"
    my_Lab_enter_button = WebElement(id="g-recap-0-btn")
    my_Lab_enter_code_button = WebElement(xpath='//*[@id="auth-email-sent"]/input[5]')


    #кнопка "Отложено" на главной странице
    postponed = WebElement(xpath='//a[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    #Надпись"Сейчас у вас нет папок" на странице "Отложенные"
    postponed_no_folders_message = WebElement(xpath='//span[@class=" g-alttext-middle-tight g-alttext-black  g-alttext-center"]')
    #заголовок страницы "Отложенные товары"
    postponed_title = WebElement(xpath='/html/body/div[1]/div[5]/div[3]/div[1]/div/div/ul/li[5]/a/span/text()')
    #кнопка "Добавить в отложенные" на странице товара
    postponed_book_button = WebElement(xpath='//a[@title="Добавить в отложенные и отслеживать появление в продаже"]')
    # название товара на странице "Отложенные товары"
    postponed_name_book = WebElement(
        xpath='/html/body/div[1]/div[5]/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[1]/a[2]/span[2]')
    #кнопка "Очистить" на странице "Отложенные товары"
    postponed_clear_all_putorder = WebElement(xpath='//a[@onclick="clearAllPutOrder(); return false;"]')
    #названия товаров на странице "Отложенные товары"
    postponed_name_books = ManyWebElements(xpath='//*[@class="product-title"]')


    #кнопка "Корзина" на главной странице
    my_basket = WebElement(
        xpath='//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js cart-icon-js"]')
    #Сообщение "Ваша корзина пуста" на странице "Корзина"
    my_basket_empty_message = WebElement(xpath='//span[contains(text(),"Ваша корзина пуста")]')
    #кнопка "Моя корзина:__" на странице "Корзина", когда в корзине есть добавленные товары
    my_basket_quant_of_books_info = WebElement(xpath='//*[@id="ui-id-4"]/b')
    #названия книг в моей корзине
    my_basket_book_name = ManyWebElements(xpath='//span[@class="product-title"]')
    #название первой книги
    my_basket_first_book_name = WebElement(
        xpath='//*[@id="basket-step1-default"]/div[2]/div[2]/div/div/div[1]/div/div[1]/a[2]/span[2]')
    # кнопка "очистить корзину" на странице "Корзина"
    my_basket_empty_button = WebElement(xpath='//div[@class="text-regular empty-basket-link"]')
    #кнопка "Восстановить удаленное" на странице "Корзина"
    my_basket_restore_deleted_button = WebElement(xpath='//div[@class="empty-basket-link"]')
    #Цены книг добавленных в корзину на сттанице "Корзина"
    my_basket_prices_of_books = ManyWebElements(xpath='//span[@class="price-val"]')
    #Итоговая сумма за книги в "Корзине"
    my_basket_sumprice = WebElement(id='basket-default-sumprice-discount')
    #кнопка "Перейти к оформлению" внизу страницы "Корзина"
    my_basket_ordering_run_button = WebElement(
        xpath='//*[@class="btn btn-primary btn-large fright start-checkout-js"]')


    #кнопка "Выбрать новое место и способ доставки" на странице "Оформление заказа"
    ordering_change_delivery_address = WebElement(xpath='//button[@class="button-link delivery__profiles-change-btn"]')
    #Поле "Адрес места доставки" в окне выбора нового места и способа доставки
    delivery_address_field = WebElement(id='deliveryAddress')
    delivery_address_field_name = WebElement(
        xpath='//*[@id="basket-delivery delivery"]/div[7]/div/div/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/div/div/label')
    #сообщение об ошибке в адресе
    delivery_address_error_address = WebElement(xpath='//div[@class="mt7 error-informer" and @data-v-7cd7e7e2 and @data-v-05f5bd7e]')
    #Кнопка "Самовывоз" в окне выбора нового места и способа доставки
    shipping_methods_self_delivery = WebElement(xpath='//li[@class="li-select margin-set pointer"]')
    #Кнопки пунктов выдачи "Самовывоз" в окне выбора нового места и способа доставки
    self_delivery_pick_up_points = ManyWebElements(xpath='//div[@class="sdp-info-block"]')
    #Первый пункт выдачи "Самовывоз" в окне выбора нового места и способа доставки
    self_delivery_first_pick_up_point = WebElement(
        xpath='/html/body/div[1]/div[6]/div[3]/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div[7]/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/ul/div[1]/li/div/div')
    #Кнопка "Курьер" в окне выбора нового места и способа доставки
    shipping_method_courier_delivery = WebElement(xpath='//li[@class="li-select margin-set"]')
    # Кнопки служб доставки "Курьер" в окне выбора нового места и способа доставки
    courier_delivery_servieces = ManyWebElements(xpath='//div[@class="cdp-container"]')
    # Первая служба доставки "Курьер" в окне выбора нового места и способа доставки
    courier_delivery_first_courier_point = WebElement(
        xpath='/html/body/div[1]/div[6]/div[3]/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div[7]/div/div/div/div/div[1]/div[1]/div[1]/div[3]/div/ul/div[1]/li/div')
    #Чек-бокс "Нужна бесконтактная доставка" при выборе
    # Кнопка "Заберу отсюда"/"Выбрать эту доставку" в окне выбора способа доставки
    delivery_pick_up_run_button = WebElement(
        xpath='//div[@class="base-button set-min-width base-button--theme-red base-button--noselect no-hover-effect text-s padding-l font-weight-medium w-100-p text-nowrap"]')
    ordering_page_info_about_selfdelivery = WebElement(xpath='//div[@class="v-color--dark"]')
    #чек-бокс "Viber/CMC уведомления о статусе заказа" на странице "Оформление заказа"
    ordering_checkbox_notifications = WebElement(xpath='//*[@id="basket-delivery delivery"]/div[4]/label[1]/div/span[1]')
    # Кнопка выбора типа пользователя "Физическое лицо" на странице "Оформление заказа"(в случае если пользователь не авторизирован)
    ordering_phisical_type_user = WebElement(xpath='//li[@class="li-select margin-set user-type-li"]')
    # Кнопка выбора типа пользователя "Юридическое лицо" на странице "Оформление заказа"(в случае если пользователь не авторизирован)
    ordering_organisation_type_user = WebElement(xpath='//li[@class="li-select margin-set pointer user-type-li"]')
    # Поле для ввода Имени получателя на странице "Оформление заказа" нового пользователя
    ordering_field_name_new_user = WebElement(xpath='//input[@placeholder="Имя"]')
    # Поле для ввода Фамилии получателя на странице "Оформление заказа" нового пользователя
    ordering_field_surname_new_user = WebElement(xpath='//input[@placeholder="Фамилия"]')
    # Поле для ввода Фамилии получателя на странице "Оформление заказа" нового пользователя
    ordering_field_phone_new_user = WebElement(xpath='//input[@placeholder="Мобильный телефон"]')
    # Поле для ввода Электронной почты получателя на странице "Оформление заказа" нового пользователя
    ordering_field_email_new_user = WebElement(xpath='//input[@placeholder="Электронная почта"]')
    #сообщения об ошибках при заполнении полей
    ordering_error_message = WebElement(xpath='//div[@class="text-xs css-default"]')
    ordering_error_message_surname = WebElement(xpath='//div[contains(text(),"Заполните фамилию русскими буквами")]')
    ordering_error_message_phone = WebElement(xpath='//div[contains(text(),"Телефон обязателен")]')
    ordering_error_message_samephone = WebElement(xpath='//div[contains(text(),"Этот телефон уже есть в Лабиринте")]')
    ordering_error_message_wrongphone = WebElement(xpath='//*[contains(text(),"Ошибка в номере телефона")]')
    ordering_error_message_email = WebElement(xpath='//*[@id="app"]/div[2]/div[2]/div[1]/div[5]/div[3]/div/div[2]/div')
    #Поле для ввода Имени получателя на странице "Оформление заказа" в случае, если пользователь авторизирован
    ordering_text_field_name = WebElement(
        xpath='//input[@class="validator-error-input nice-input-text input-top-label padding-s w-100-p text-s" and @placeholder="Имя"]')
    # Поле для ввода Фамилии получателя на странице "Оформление заказа"
    ordering_text_field_surname = WebElement(
        xpath='//input[@class="validator-error-input nice-input-text input-top-label padding-s w-100-p text-s" and @placeholder="Фамилия"]')
    # Поле для ввода Мобильного номера телефона получателя на странице "Оформление заказа"
    ordering_text_field_mobile_phone = WebElement(xpath='//input[@class="vti__input"]')


    #кнопка "Подтвердить" появляющаяся с полем ввода номера телефона на странице "Оформление заказа"
    ordering_button_verify_phone = WebElement(xpath='//div[contains(text(), "Подтвердить")]')
    #Заголовок "Подтверждение телефона" в окне подтверждения телефона
    verify_phone_title = WebElement(xpath='//div[@class="verif-form__title"]')
    #Информационное сообщение "Необходимо подтвердить номер телефона" под полем ввода номера телефона
    ordering_message_verify_phone = WebElement(xpath='//span[@class="icon-xs icon icon-error error-informer__icon"]')
    #Поле ввода кода подтверждения в окне "Подтверждение телефона"
    verify_phone_field_code = WebElement(xpath='//input[@class="verif-form__input"]')
    #Кнопка "отправить еще раз" в окне "Подтверждение телефона"
    verify_phone_send_again = WebElement(xpath='//a[@class="js-verif-send-again verif-send-again__link"]')
    #Кнопка "Проверить код" в окне "Подтверждение телефона"
    verify_phone_run_button = WebElement(xpath='//button[@class="verif-form__button js-verif-form-submit verif-form__button__enabled"]')


    # кнопка "Добавить купоны" на странице "Оформление заказа"
    ordering_add_cupons_button = WebElement(xpath='//button[@class="button-link" and contains(text(),"Добавить купоны")]')
    # заголовок страницы "Купоны"
    page_title_cupons = WebElement(xpath='//div[@class="left-modal--block-for-search mb30"]/h2[@class="_title-secondary"]')
    # кнопка "Оплата при получении" на странице "Оформление заказа"
    ordering_payment_on_delivery = WebElement(xpath='//*[@id="app"]/div[2]/div[2]/div[1]/div[7]/ul/li[1]/div')
    # кнопка "Предоплата по QR" на странице "Оформление заказа"
    ordering_prepayment_by_QR = WebElement(xpath='//*[@id="app"]/div[2]/div[2]/div[1]/div[7]/ul/li[2]/div/div/div')
    # кнопка "Предоплата на сайте" на странице "Оформление заказа"
    ordering_prepayment_by_site = WebElement(xpath='//*[@id="app"]/div[2]/div[2]/div[1]/div[7]/ul/li[3]/div/div/div')
    #кнопка "ОФормить заказ" на странице "Оформление заказа"
    ordering_place_an_order_button = WebElement(xpath='//div[contains(text(), "Оформить заказ")]')


    #Страница оформленного заказа, надпись "заказ № ..."
    order_page_message_order = WebElement(xpath='//h1[@class="cabinet-header-h1"]')
    #Кнопка "Действия с заказом" на странице заказов
    order_page_actions_with_order = WebElement(xpath='//div[@class="mt20 fleft mb20 order-actions g-alttext-big-tight g-alttext-grey"]')
    #"Аннулировать заказ" в выпадающем списке кнопки "Действия с заказом" на странице заказов
    cancel_order = WebElement(xpath='//span[@class="js-annul-order-reason-show-btn  pointer g-alttext-grey analytics-click-js"]')
    # "Положить товары в корзину" в выпадающем списке кнопки "Действия с заказом" на странице заказов
    add_order_to_basket = WebElement(id='js-prods-to-basket')
    #Кнопка "Хочу изменить заказ" в окне "Нажмите на причину для отмены заказа" при аннулировании заказа
    cancel_change_order = WebElement(xpath='//div[@data-id_reason="2"]')
    # Кнопка "Передумал покупать эти товары" в окне "Нажмите на причину для отмены заказа" при аннулировании заказа
    cancel_change_my_mind_about_order = WebElement(xpath='//div[@data-id_reason="5"]')
    # Кнопка "Заказ был оформлен ошибочно" в окне "Нажмите на причину для отмены заказа" при аннулировании заказа
    cancel_mistake_order = WebElement(xpath='//*[@id="annul-reasons-overlay"]/div/div/div/div[3]/div[1]/div[6]')
    # Кнопка "Не отменять заказ"в окне "Нажмите на причину для отмены заказа" при аннулировании заказа
    not_cancel_button =WebElement(
        xpath='//div[@class="btn btn-primary btn-small b-annul-reasons-container-e-cancel-annul-order-btn js-cancel-annul-order-btn"]')
    #Надпись "Отменен клиентом" напротив отмененного заказа на странице личного кабинета пользователя
    my_Lab_message_about_cancel_order = WebElement(xpath='//td[contains(text(), "Отменен клиентом")]')
    #Кнопка "Восстановить" напротив отмененного заказа на странице личного кабинета пользователя
    my_Lab_restore_cancel_order_button = WebElement(xpath='//span[@class="btn btn-small btn-clear js-restore-annul-order analytics-click-js"]')


    #Ссылка на группу ВКонтакте в футере сайта
    footer_tests = WebElement(xpath='//a[@data-event-content="Тесты"]')
    tests_title_name = WebElement(xpath='//*[@id="contests"]/h1')
    #Ссылка на раздел "Как сделать заказ" в футере сайта
    footer_how_do_order = WebElement(xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and @href="/help/order/"]')
    #Ссылка "© Холдинг «Лабиринт»" в футере сайта
    footer_Lab_holding = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link b-rfooter-e-item-link-m-small analytics-click-js" and @data-event-content="Холдинг"]')
    #Логотип "лабиринта" в футере страницы
    footer_labirint_logo = WebElement(xpath='//div[@class="b-rfooter-e-item-e-logo"]')
    down_element = WebElement(xpath='//*[@id="bottom"]/div[24]/h2')
    #ссылка на группу "Вконтакте" в футере сайта
    footer_vk = WebElement(xpath='//*[@data-event-content="ВКонтакте"]')
    #ссылка на приложение "Лабиринт" в Google Play в футере сайта
    footer_google_play = WebElement(xpath='//*[@data-event-content="Google Play"]')

