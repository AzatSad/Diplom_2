import allure
import pytest
from utils.api_client import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
@allure.step('Зарегистрировать пользователя')
def registration_user_fixture(api_client):
    user = {}

    def register_user(data):
        nonlocal user
        response = api_client.create_new_user(
            endpoint='register',
            email=data['email'],
            password=data['password'],
            name=data['name']
        )
        user.update({
            "response": response,
            "accessToken": response.json().get('accessToken', '')
        })
        return user

    yield register_user

    if user.get("accessToken"):
        api_client.delete_user(authorization=user.get("accessToken"))
