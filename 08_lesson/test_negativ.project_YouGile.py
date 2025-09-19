from project_YouGile import ProjectYouGile

LOGIN = ""
PASSWORD = ""
COMPANY_ID = ""


api = ProjectYouGile('https://ru.yougile.com/api-v2/',LOGIN,PASSWORD,COMPANY_ID)


def test_create_project_():
    # количество проектов до
    projects_before = api.get_project_list()
    len_before = len(projects_before)
    # создание проекта
    title = '  '
    users = {
    "123":"admin"
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


def test_get_project_with_id():
    # создание проекта
    title = 'ГосУслуги'
    users = {
    "8087uhpds87=9-48u94":"admin"
  }
    result = api.create_project(title, users)
    project_id = result.json()['id']

    # обращаемся к проекту
    new_project = api.get_project_with_id(project_id)

    assert new_project.json()['title'] == title
    assert new_project.json()['users'] == users


def test_edit_project():
    title = ' '
    users = {
        "":"admin"
    }
    result = api.create_project(title, users)

    project_id = result.json()['id']
    new_deleted = True
    new_title = 'Edited_ГосУслуги'

    edited = api.edit_project(project_id, new_deleted, new_title)
    new_project = api.get_project_with_id(project_id)

    assert edited.status_code == 400
    assert new_project.json()['title'] == new_title
