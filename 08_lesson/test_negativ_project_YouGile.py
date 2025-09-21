from project_YouGile import ProjectYouGile

LOGIN = "ev.sherbacova@yandex.ru"
PASSWORD = "Shcherbachka93"
COMPANY_ID = "65797906-9c89-406b-a6b3-480d0e5206a5"

api = ProjectYouGile('https://ru.yougile.com/api-v2/',LOGIN,PASSWORD,COMPANY_ID)


def test_negative_create_project_():
    # количество проектов до
    projects_before = api.get_project_list()
    len_before = len(projects_before)
    # создание проекта
    title = ' '
    users = {
        "62d0c983-8ffe-440f-b07a-700b31a2ba83": "admin"
  }

    result = api.create_project(title, users)
    new_id = result.json()['id']

    # количество проектов после
    projects_after = api.get_project_list()
    len_after = len(projects_after)

    assert result.status_code == 400
    assert len_after - len_before == 0
    assert projects_after[-1]['title'] == title
    assert projects_after[-1]['id'] == new_id


def test__negativ_get_project_with_id():

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


def test_negativ_edit_project():
    title = 'gltguyigtliuy'
    users = {
        "62d0c983-8ffe-440f-b07a-700b31a2ba83":"admin"
    }
    result = api.create_project(title, users)

    project_id = result.json()['id']
    new_deleted = True
    new_title = 'Edited_ГосУслуги'

    edited = api.edit_project(project_id, new_deleted, new_title)
    new_project = api.get_project_with_id(project_id)

    assert edited.status_code == 400
    assert new_project.json()['title'] == new_title
