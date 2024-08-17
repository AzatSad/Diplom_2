import allure
from conftest import registration_user_fixture, api_client
from constants import USER_DATA, USER_DATA_DEFECTIVE
from utils.api_client import APIClient


@allure.story('Авторизация пользователя')
class TestLoginUser:
    @allure.title('Авторизация под существующим пользователем')
    def test_authorization_existing_user(self, registration_user_fixture):
        register_user = next(registration_user_fixture)
        user = register_user(USER_DATA)
        api = APIClient()
        response = api.auth_user(USER_DATA['email'], USER_DATA['password'])
        print(f"Auth response: {response.json()}")
        assert response.status_code == 200
        assert response.json().get('success') is True

    @allure.title('Авторизация с неверным логином и паролем')
    def test_authorization_with_invalid_login_and_password(self):
        api = APIClient()
        response = api.auth_user(USER_DATA_DEFECTIVE['email'], USER_DATA_DEFECTIVE['password'])
        assert response.status_code == 401
        assert response.json().get('message') == "email or password are incorrect"
