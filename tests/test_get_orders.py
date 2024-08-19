import allure
from constants import USER_DATA
from conftest import registration_user_fixture, api_client


@allure.story('Получить заказы конкретного пользователя')
class TestGetOrders:
    @allure.title('Получить заказы авторизованным пользователем')
    def test_get_orders_with_authorized_user(self, registration_user_fixture, api_client):
        response_auth = api_client.auth_user(USER_DATA['email'], USER_DATA['password'])
        authorization_token = response_auth.json().get('accessToken', '')
        get_response = api_client.get_orders(authorization_token)
        assert get_response.status_code == 200
        assert get_response.json()['success'] is True

    @allure.title('Получить заказ неавторизованным пользователем')
    def test_get_orders_with_unauthorized_user(self, api_client):
        get_response = api_client.get_orders()
        assert get_response.status_code == 401
        assert get_response.json().get('message') == "You should be authorised"
