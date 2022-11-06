import random
from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from faker import Faker
import factory
import pytest
from rest_framework import status
from account_book.models import Account
from account_book.utils.factory import AccountInvisibleFactory, AccountVisibleFactory, UserFactory
from user.models import User


@pytest.mark.django_db
class test_api_response(APITestCase):
    
    
    def change_authorization(self, client_user):
        res = self.client.post(
            self.url_login,
            {
                "email": client_user.email,
                "password": "qwer1234",
            },
            content_type="application/json",
        )
        temp = res.content
        access_token = res.content
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token['access_token']}")

    @pytest.fixture(autouse=True)
    def setUp(self):

        self.url_create = reverse("account:create")
        self.url_detail = reverse("account:details")
        self.url_update = reverse("account:update")
        self.url_delete = reverse("account:delete")
        self.url_recover = reverse("account:recover")
        self.url_list = reverse("account:list")
        self.url_register = reverse("user:signup")
        self.url_login = reverse("user:login")

        self.factory = APIRequestFactory()
        self.user = UserFactory()
        self.account_visible = AccountVisibleFactory()
        self.account_invisible = AccountInvisibleFactory()
        self.faker = Faker()

        AccountVisibleFactory.create_batch(1, user__name="test_name")
        host_user = User.objects.get(name="test_name")
        self.change_authorization(host_user)

    @pytest.mark.django_db
    def tearDown(self):
        User.objects.all().delete()
        Account.objects.all().delete()

    def test_create(self):
        # given
        data = {
            "expend": random.randrange(1000, 1000000),
            "memo": self.faker.text(1000),
        }
        print(self.user)
        # when
        # response = self.client.post(self.url_create, data=data, format="json", HTTP_AUTHORIZATION='JWT {}'.format(token))
        response = self.client.post(self.url_create, data=data, format="json")

        # then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @pytest.mark.django_db
    def test_read(self):
        # given
        self.account_visible.create_batch(9, sort_order=factory.Sequence(lambda n: 10 - n))

        # when

        # then
        pass

    # def test_read_list(self):
    #     pass

    # def test_update(self):
    #     pass

    # def test_soft_delete(self):
    #     pass

    # def test_recover(self):
    #     pass

    # # Exception response Test

    # def test_read_not_found(self):
    #     pass

    # def test_create_not_login(self):
    #     pass

    # def test_update_not_found(self):
    #     pass

    # def test_soft_delete_not_allowed(self):
    #     pass
