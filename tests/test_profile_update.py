import allure
import pytest
from constants import USER_DATA
from conftest import registration_user_fixture, api_client


@allure.story('Изменить данные профиля')
class TestProfileUpdate:
    @allure.title('Изменить пользователя без авторизации')
    @pytest.mark.parametrize("field_to_update, new_value", [("name", "Azat1"),
                                                            ("email", "mail@mail.ru"), ("password", "password")])
    def test_update_user_without_authorization(self, field_to_update, new_value, api_client):
        updated_user_data = {field_to_update: new_value}
        response_update = api_client.update_user_data(updated_user_data)
        assert response_update.status_code == 401
        assert response_update.json()['message'] == "You should be authorised"

    @allure.title('Изменить данные пользователя с авторизацией')
    @pytest.mark.parametrize("updated_name, updated_password", [("UpdateName", "UpdatePassword"),
                                                                ("AnotherName", "AnotherPassword")])
    def test_update_user_with_authorization(
            self,
            registration_user_fixture,
            updated_name,
            updated_password,
            api_client
    ):
        response_auth = api_client.auth_user(USER_DATA['email'], USER_DATA['password'])
        authorization_token = response_auth.json().get('accessToken', '')
        updated_user_data = {"name": updated_name, "password": updated_password}
        response_update = api_client.update_user_data(updated_user_data, authorization=authorization_token)
        assert response_update.status_code == 200
        assert response_update.json()['success'] is True

    @allure.title('Изменить данные на зарезервированную почту пользователя с авторизацией')
    def test_update_user_with_authorization_with_mail_used(self, registration_user_fixture, api_client):
        response_auth = api_client.auth_user(USER_DATA['email'], USER_DATA['password'])
        authorization_token = response_auth.json().get('accessToken', '')
        updated_user_data = {"email": "sadertdinov_4@gmail.com"}
        response_update = api_client.update_user_data(updated_user_data, authorization=authorization_token)
        assert response_update.status_code == 403
        assert response_update.json()['message'] == "User with such email already exists"
