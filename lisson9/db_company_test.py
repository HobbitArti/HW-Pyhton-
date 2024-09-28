import allure
import random
from faker import Faker
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable

api = CompanyApi("https://x-clients-be.onrender.com/docs/")
db = CompanyTable("postgresql://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")

fake = Faker("ru_RU")

@allure.step("Метод для генерации названия организации")
def generate_random_company_data():
    name = fake.name()
    description = fake.text(max_nb_chars=20)
    return name, description

@allure.step("Метод для генерации названия при редактировании организации")
def generate_random_update_company():
    new_name = fake.name()
    new_description = fake.text(max_nb_chars=20)
    return new_name, new_description

@allure.id("SKYPRO-1")
@allure.epic("компании")
@allure.severity("blocker")
@allure.suite("Тесты на работу с организациями")
@allure.story("получение списка компаний")
@allure.feature("READ")
@allure.title("Получение полного списка компании")
def test_get_companies():

    api_result = api.get_company_list()

    db_result = db.get_company_list()

    with allure.step("Сравнить размеры 2х списков"):
        assert len(api_result) < len(db_result)

@allure.id("SKYPRO-1")
@allure.epic("компании")
@allure.severity("blocker")
@allure.suite("Тесты на работу с организациями")
@allure.story("получение списка компаний")
@allure.feature("READ")
@allure.title("Получение полного списка активных компании")
@allure.description("Получение организации с параметром isActive = True")
def test_get_active_companies():

    filtered_list = api.get_company_list(params_to_add={'active': 'true'})

    db_list = db.get_active_company()

    with allure.step("Сравнить размеры 2х списков"):
        assert len(filtered_list) < len(db_list)

@allure.id("SKYPRO-1")
@allure.epic("компании")
@allure.severity("blocker")
@allure.suite("Тесты на работу с организациями")
@allure.story("создание компании")
@allure.feature("CREATE")
@allure.title("Создание организации")
def test_add_company():

    api_result_before = api.get_company_list()

    db_result_before = db.get_company_list()

    with allure.step("Создать организацию"):
        name, description = generate_random_company_data()

        db.create_comp(name, description)

    max_id = db.get_max_id_comp(id)

    api_result_after = api.get_company_list()

    db_result_after = db.get_company_list()

    with allure.step("Проверить, что списки ДО в API и БД равны"):
        assert len(api_result_before) < len(db_result_before)

    with allure.step("Проверить, что списки ПОСЛЕ в API и БД равны"):
        assert len(api_result_after) < len(db_result_after)

    with allure.step("Проверить, что список ДО меньше списка ПОСЛЕ в БД на 1"):
        assert len(db_result_after) - len(db_result_before) == 1

    with allure.step("Проверить, что список ДО меньше списка ПОСЛЕ в API на 1"):
        assert len(api_result_after) - len(api_result_before) == 1

    with allure.step("Проверить, поля новой организации. Корректно заполнены"):
        assert api_result_after[-1]["name"] == name
        assert api_result_after[-1]["description"] == description
        assert api_result_after[-1]["id"] == max_id

    db.delete_company(max_id)

@allure.id("SKYPRO-1")
@allure.epic("компании")
@allure.severity("blocker")
@allure.suite("Тесты на работу с организациями")
@allure.story("обращение к компании по id")
@allure.title("Получение организации по id")
def test_get_one_company():
    with allure.step("Создать организацию"):
        name, description = generate_random_company_data()

        db.create_comp(name, description)

    max_id = db.get_max_id_comp(id)

    new_company = api.get_company(max_id)

    with allure.step("Проверить, что поля новой организации. Корректно заполнены"):
        assert new_company["id"] == max_id
        assert new_company["name"] == name
        assert new_company["description"] == description
        assert new_company["isActive"]

    db.delete_company(max_id)

@allure.id("SKYPRO-1")
@allure.epic("компании")
@allure.severity("blocker")
@allure.suite("Тесты на работу с организациями")
@allure.story("изменение данных в компании")
@allure.feature("UPDATE")
def test_edit():
    with allure.step("Создать организацию"):
        name, description = generate_random_company_data()

        db.create_comp(name, description)

    max_id = db.get_max_id_comp(id)

    with allure.step("Редактировать название организации"):
        new_name, new_description = generate_random_update_company()

        edited = api.edit(max_id, new_name, new_description)

    with allure.step("Проверить что поля организации поменялись на новые"):
        assert edited['name'] == new_name
        assert edited['description'] == new_description
        assert edited['isActive'] == True

    with allure.step("Проверить что 'id организации не изменился"):
        assert edited["id"] == max_id

    db.delete_company(max_id)

@allure.id("SKYPRO-1")
@allure.epic("компании")
@allure.severity("blocker")
@allure.suite("Тесты на работу с организациями")
@allure.story("удаление компании")
@allure.feature("DELETE")
def test_delete():
    with allure.step("Создать организацию"):
        name, description = generate_random_company_data()

        db.create_comp(name, description)

    max_id = db.get_max_id_comp(id)

    deleted = api.delete(max_id)

    db.delete_company(max_id)

    with allure.step("Проверить что организация удалилась"):
        assert deleted["id"] == max_id
        assert deleted["name"] == name
        assert deleted["description"] == description
        assert deleted["isActive"] == True

    rows = db.get_company_by_id(max_id)

    with allure.step("Проверить, что максимальное id = 0"):
        assert len(rows) == 0

@allure.id("SKYPRO-1")
@allure.epic("компании")
@allure.severity("blocker")
@allure.suite("Тесты на работу с организациями")
@allure.story("изменение статуса компании")
@allure.feature("UPDATE")
@allure.description("Изменение статуса организации с параметром isActive = True на параметр False")
def test_deactivate():
    with allure.step("Создать организацию"):
        name, description = generate_random_company_data()

        db.create_comp(name, description)

    max_id = db.get_max_id_comp(id)

    body = api.set_active_state(max_id, False)

    with allure.step("Проверить, что данные isActive поменялись"):
        assert body["isActive"] == False

    db.delete_company(max_id)

@allure.id("SKYPRO-1")
@allure.epic("компании")
@allure.severity("blocker")
@allure.suite("Тесты на работу с организациями")
@allure.story("изменение статуса компании")
@allure.feature("UPDATE")
@allure.description("Изменение статуса организации с параметром isActive = True на параметр False и наоборот")
def test_deactivate_and_activate_back():
    with allure.step("Создать организацию"):
        name, description = generate_random_company_data()

        db.create_comp(name, description)

    max_id = db.get_max_id_comp(id)

    api.set_active_state(max_id, False)
    body = api.set_active_state(max_id, True)

    with allure.step("Проверить, что данные isActive поменялись True"):
        assert body["isActive"] == True

    db.delete_company(max_id)