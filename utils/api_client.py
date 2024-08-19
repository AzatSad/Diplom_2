import allure
import requests
from utils.constants import (BASE_URL, ENDPOINT_UPDATE_USER, ENDPOINT_CREATE_USER, ENDPOINT_LOGIN_USER,
                             ENDPOINT_ORDER_URL)


class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.update_user = ENDPOINT_UPDATE_USER
        self.create_user = ENDPOINT_CREATE_USER
        self.login_user = ENDPOINT_LOGIN_USER
        self.order_url = ENDPOINT_ORDER_URL

    @allure.step('Создать пользователя')
    def create_new_user(self, endpoint, email=None, password=None, name=None):
        url = f"{self.base_url}{self.create_user}"
        data = {"email": email, "password": password, "name": name}
        response = requests.post(url, json=data)
        return response

    @allure.step('Удалить пользователя')
    def delete_user(self, authorization):
        url = f"{self.base_url}{self.update_user}"
        headers = {"Authorization": authorization}
        response = requests.delete(url, headers=headers)
        return response

    @allure.step('Авторизация пользователя')
    def auth_user(self, email=None, password=None):
        url = f"{self.base_url}{self.login_user}"
        data = {"email": email, "password": password}
        response = requests.post(url, json=data)
        return response

    @allure.step('Обновить данные пользователя')
    def update_user_data(self, updated_data, authorization=None):
        url = f"{self.base_url}{self.update_user}"
        headers = {"Authorization": authorization}
        response = requests.patch(url, headers=headers, json=updated_data)
        return response

    @allure.step('Создать новый заказ')
    def create_order(self, ingredients):
        url = f"{self.base_url}{self.order_url}"
        data = {"ingredients": ingredients}
        response = requests.post(url, json=data)
        return response

    @allure.step('Получить список заказов пользователя')
    def get_orders(self, authorization_token=None):
        url = f"{self.base_url}{self.order_url}"
        response = requests.get(url)
        headers = {"Authorization": authorization_token} if authorization_token else {}
        response = requests.get(url, headers=headers)
        return response
