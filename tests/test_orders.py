import allure
from constants import USER_DATA
from conftest import registration_user_fixture, api_client


@allure.story('Создать заказ')
class TestCreateOrder:
    @allure.title('Создать заказ с авторизацией и ингредиентами')
    def test_create_order_with_authorization(self, registration_user_fixture, api_client):
        response_auth = api_client.auth_user(USER_DATA['email'], USER_DATA['password'])
        response_create = api_client.create_order(["61c0c5a71d1f82001bdaaa70"])
        assert response_create.status_code == 200
        assert response_create.json().get('name') == "Метеоритный бургер"

    @allure.title('Создать заказ без авторизации')
    def test_create_order_without_authorization(self, api_client):
        response_create = api_client.create_order(["61c0c5a71d1f82001bdaaa71"])
        assert response_create.status_code == 200
        assert response_create.json().get('name') == "Био-марсианский бургер"

    @allure.title('Создать заказ без ингредиентов')
    def test_create_order_without_ingredients(self, api_client):
        response_create = api_client.create_order([])
        assert response_create.status_code == 400
        assert response_create.json().get('message') == "Ingredient ids must be provided"

    @allure.title('Создать заказ с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredients(self, api_client):
        response_create = api_client.create_order(["incorrect"])
        assert response_create.status_code == 500
