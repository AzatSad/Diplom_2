import allure
from constants import USER_DATA
from utils.api_client import APIClient
from conftest import registration_user_fixture, api_client


@allure.story('Получить заказы конкретного пользователя')
class TestGetOrders:
    @allure.title('Получить заказы авторизованным пользователем')
    def test_get_orders_with_authorized_user(self, registration_user_fixture):
        register_user = next(registration_user_fixture)
        user = register_user(USER_DATA)
        api = APIClient()
        response_auth = api.auth_user(USER_DATA['email'], USER_DATA['password'])
        authorization_token = response_auth.json().get('accessToken', '')
        get_response = api.get_orders(authorization_token)
        assert get_response.status_code == 200
        assert get_response.json()['success'] is True

    @allure.title('Получить заказ неавторизованным пользователем')
    def test_get_orders_with_unauthorized_user(self):
        api = APIClient()
        get_response = api.get_orders()
        assert get_response.status_code == 401
        assert get_response.json().get('message') == "You should be authorised"
