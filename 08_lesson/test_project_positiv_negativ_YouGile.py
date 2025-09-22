from project_YouGile import ProjectYouGile

LOGIN = "ev.sherbacova@yandex.ru"
PASSWORD = "Shcherbachka93"
COMPANY_ID = "65797906-9c89-406b-a6b3-480d0e5206a5"

api = ProjectYouGile('https://ru.yougile.com/api-v2/', LOGIN, PASSWORD, COMPANY_ID)


def test_create_project_positive():
    # создание проекта
    title = 'ГосУслуги'
    users = {
        "62d0c983-8ffe-440f-b07a-700b31a2ba83": "admin"
    }

    result = api.create_project(title, users)

    # количество проектов после
    projects_after = api.get_project_list()

    assert result.status_code == 201
    assert projects_after[-1]['title'] == title


def test_get_project_with_id_positive():
    # создание проекта
    title = 'ГосУслуги'
    users = {
        "62d0c983-8ffe-440f-b07a-700b31a2ba83": "admin"
    }
    result = api.create_project(title, users)
    project_id = result.json()['id']

    # обращаемся к проекту
    new_project = api.get_project_with_id(project_id)

    assert new_project.json()['title'] == title
    assert new_project.json()['users'] == users


def test_edit_project_positive():
    title = 'Edit_ГосУслуги'
    users = {
        "62d0c983-8ffe-440f-b07a-700b31a2ba83": "admin"
    }
    result = api.create_project(title, users)

    project_id = result.json()['id']
    new_deleted = True
    new_title = 'Edited_ГосУслуги'

    edited = api.edit_project(project_id, new_deleted, new_title)
    new_project = api.get_project_with_id(project_id)

    assert edited.status_code == 200
    assert new_project.json()['title'] == new_title


def test_create_project_negative():
    # создание проекта
    title = ' '
    users = {
        "62d0c983-8ffe-440f-b07a-700b31a2ba83": "admin"
    }

    result = api.create_project(title, users)
    project_id = result.json()['id']

    assert result.status_code == 201
    assert project_id in result.text


def test_get_project_with_id_negative():
    title = 'ГосУслуги'
    users = {
        "62d0c983-8ffe-440f-b07a-700b31a2ba83": "admin"
    }
    result = api.create_project(title, users)
    project_id = result.json()['id']

    # обращаемся к проекту
    new_project = api.get_project_with_id(project_id)

    assert new_project.json()['title'] == title
    assert new_project.json()['users'] == users


def test_edit_project_negative():
    title = 'gltguyigtliuy'
    users = {
        "62d0c983-8ffe-440f-b07a-700b31a2ba83": "admin"
    }
    result = api.create_project(title, users)

    project_id = result.json()['id']
    new_deleted = True
    new_title = 'Edited_ГосУслуги'

    edited = api.edit_project(project_id, new_deleted, new_title)
    new_project = api.get_project_with_id(project_id)

    assert edited.status_code == 200
    assert new_project.json()['title'] == new_title

