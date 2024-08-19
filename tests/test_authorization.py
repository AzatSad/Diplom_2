import allure
from conftest import registration_user_fixture, api_client
from constants import USER_DATA, USER_DATA_DEFECTIVE


@allure.story('Авторизация пользователя')
class TestLoginUser:
    @allure.title('Авторизация под существующим пользователем')
    def test_authorization_existing_user(self, registration_user_fixture, api_client):
        response = api_client.auth_user(USER_DATA['email'], USER_DATA['password'])
        assert response.status_code == 200
        assert response.json().get('success') is True

    @allure.title('Авторизация с неверным логином и паролем')
    def test_authorization_with_invalid_login_and_password(self, api_client):
        response = api_client.auth_user(USER_DATA_DEFECTIVE['email'], USER_DATA_DEFECTIVE['password'])
        assert response.status_code == 401
        assert response.json().get('message') == "email or password are incorrect"
