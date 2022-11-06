"""
테스팅용 가짜 데이터를 만들기 위한 Factory
"""
    
    
import random
from account_book.models import Account
import factory
from faker import Faker
from django.contrib.auth.hashers import make_password
from user.models import User

faker = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = faker.name()
    # nickname = Faker().name()
    email = factory.lazy_attribute(lambda u: f"{u.name.split()[0]}@example.com")
    # phone = "01012345678"
    password = make_password("qwer1234")
    
class AccountVisibleFactory(factory.django.DjangoModelFactory):
    #보이는 임의의 데이터 생성
    class Meta:
        model = Account
    
    expend = random.randrange(1000, 1000000)
    memo = faker.sentense()
    is_deleted = "V"
    deleted_at = faker.date()
    recovered_at = faker.date()
    
class AccountInvisibleFactory(factory.django.DjangoModelFactory):
    #보이지 않는 임의의 데이터 생성
    class Meta:
        model = Account
    
    expend = random.randrange(1000, 1000000)
    memo = faker.sentense()
    is_deleted = "V"
    deleted_at = faker.date()
    recovered_at = faker.date()
    