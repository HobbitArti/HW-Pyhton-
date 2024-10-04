import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from Class.Personal import PersonalDataPage

@allure.id("PersonalData")
@allure.epic("Персональные данные")
@allure.severity("blocker")
@allure.story("Заполнение персональных данных")
@allure.feature("CREATE")
@allure.title("Заполнить персональные данные")
@allure.suite("Тесты на работу формы с заполнением персональных данных")
def test_form_elements():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создание переменной, которая хранит экзампляр класса PersonalDataPage"):
        personal_data_page = PersonalDataPage(driver)

    personal_data_page.personal_data("Artem", "Vologdin", "Ugdanskay, -40", "test@skypro.com", "+79999999999", "Chita", "Russia", "QA", "SkyPro")
    personal_data_page.zip_code_red()
    personal_data_page.other_fields_green()
    personal_data_page.close_driver()
    
    # Утверждения для проверки ожидаемого поведения
    assert personal_data_page.zip_code_red(), "Поле Zip code не подсвечено красным"
    assert personal_data_page.other_fields_green(), "Не все остальные поля подсвечены зеленым"

    # Дополнительные утверждения для других проверок достоверности (при необходимости)
    assert personal_data_page.is_email_required(), "Поле email не помечено как обязательное"
    assert personal_data_page.is_city_required(), "Поле city не помечено как обязательное"
