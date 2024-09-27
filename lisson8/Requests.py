import requests
from EmployeesApi import workersApi

api = workersApi("https://x-clients-be.onrender.com")

def test_add_new_employee():
      #Создать новую компанию
    name = "DavingShop"
    descr = "Diving equipment"
    result = api.create_company(name, descr)
    new_id = result["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # получить список сотрудников 
    body = api.get_employees_list(companyId)
    len_before = len(body)
     # добавить нового сотрудника
    firstName = "Artem"
    lastName = "Vologdin"
    middleName = "Leonidovich"
    company = companyId
    email = "ar_daving@gmail.com"
    url = "string"
    phone = "89999999999"
    birthdate = "1998-30-12"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании 
    body = api.get_employees_list(companyId)
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "Artem"
    assert body[-1]["lastName"] == "Vologdin"
    assert body[-1]["middleName"] == "Leonidovich"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "89999999999"
    assert body[-1]["birthdate"] == "1998-30-12"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_get_employees_id():
    #Создать новую компанию
    name = "Что то неизвестное"
    descr = "Просто расскажем"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании по ID
    new_company = api.get_company(new_id)
    companyId = new_company['id']
    # получить список сотрудников новой компании 
    body = api.get_employees_list(companyId)
    begin_list = len(body)
    # добавить нового сотрудника
    firstName = "Иван"
    lastName = "Медведев"
    middleName = "Сергеевич"
    company = companyId
    email = "midew346@mail.ru"
    url = "string"
    phone = "865837387609"
    birthdate = "1999-07-10"
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate,isActive=1)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании 
    body = api.get_employees_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    assert body[-1]["firstName"] == "Иван"
    assert body[-1]["lastName"] ==  "Медведев"
    assert body[-1]["middleName"] == "Сергеевич"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] ==  "865837387609"
    assert body[-1]["birthdate"] == "1999-07-10"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_patch_employee():
    #Создать новую компанию
    name = "ETS"
    descr = "Симулируем грузо-перевозки"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # добавить нового сотрудника
    firstName = "Артём"
    lastName = "Леонов"
    middleName = "Артёмович"
    company = companyId
    email = "gruz-rem@mail.ru"
    url = "string"
    phone = "86564567877"
    birthdate = "1986-12-12"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании 
    body = api.get_employees_list(companyId)
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    # Изменить информацию по сотруднику
    new_lastName = "Марков"
    new_email = "sana-x@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.edit_employee(employee_id, new_lastName, new_email, new_url, new_phone, new_isActive)
    assert edited["email"] == "sana-x@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] == False

def test_delete_employee():
    #Создать новую компанию
    name = "Окна"
    descr = "Видно всё"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # добавить нового сотрудника
    firstName = "Марина"
    lastName = "Перова"
    middleName = "Александровна"
    company = companyId
    email = "perova-mar@mail.ru"
    url = "string"
    phone = "865422377865"
    birthdate = "1980-05-06"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # удалить сотрудника
    del_emp = api.delete_employee(emp_id)

    # Проверить, что сотрудник был удален
    assert del_emp is not None, "Сотрудник не был удален"