import requests

class ProjectYouGile:
    # Инициализация
    def __init__(self, url,login, password, company_id) -> None:
        self.url = url
        self.token = self.get_token(login, password, company_id)

    # Получить список проектов компании
    def get_project_list(self):
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }


        resp = requests.get(self.url + 'projects', headers=headers)
        return resp.json()['content']

    # Получить ключ авторизации
    def get_token(self, login, password, company_id):
        payload = {
            "login": login,
            "password": password,
            "companyId": company_id
        }
        resp = requests.post(self.url + 'auth/keys/get', json=payload)
        response_data = resp.json()
        print(response_data)


        # Извлекаем токен из ответа
        if 'key' in response_data[0]:
            return response_data[0]['key']
        else:
            raise ValueError("Токен не найден в ответе API")
    # Добавить компанию:
    def create_project(self, title, users):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        project = {
            "title": title,
            "users": users
        }
        resp = requests.post(self.url + 'projects',
                             headers=headers,
                             json=project)
        return resp

        # Получить проект по id
    def get_project_with_id(self, project_id):
        key = self.token

        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json; charset=utf-8'
        }
        resp = requests.get(self.url + f'projects/{project_id}',
                            headers=headers)
        return resp

    # Изменить название проекта
    def edit_project(self, project_id, new_deleted, new_title):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        project = {
            "deleted": new_deleted,
            "title": new_title

        }
        resp = requests.put(self.url + f'projects/{project_id}',
                            headers=headers, json=project)
        return resp
