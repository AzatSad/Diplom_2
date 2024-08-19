import allure
from conftest import registration_user_fixture, api_client
from constants import USER_DATA, USER_DATA_EXISTING, USER_DATA_INCOMPLETE


@allure.story('Регистрация пользователя')
class TestRegistrationUser:
    @allure.title('Создать уникального пользователя')
    def test_unique_user(self, registration_user_fixture):
        register_user = next(registration_user_fixture)
        user = register_user(USER_DATA)
        response = user['response']
        assert response.status_code == 200
        assert response.json().get('success') is True

    @allure.title('Создать пользователя, который уже зарегистрирован')
    def test_create_duplicate_user(self, registration_user_fixture):
        register_user = next(registration_user_fixture)
        user_1 = register_user(USER_DATA_EXISTING)
        response_1 = user_1['response']
        assert response_1.status_code == 403
        assert response_1.json()['message'] == "User already exists"

    @allure.title('Создать пользователя без заполнения одного из обязательных полей')
    def test_create_user_missing_one_field(self, registration_user_fixture):
        register_user = next(registration_user_fixture)
        user = register_user(USER_DATA_INCOMPLETE)
        response = user['response']
        assert response.status_code == 403
        assert response.json()['message'] == "Email, password and name are required fields"
