"""
테스팅용 가짜 데이터를 만들기 위한 Factory
"""
    
    
import random

import bcrypt
from account_book.models import Account
import factory
from faker import Faker
from django.contrib.auth.hashers import make_password
from user.models import User

faker = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Faker("name")
    # nickname = Faker().name()
    email = factory.lazy_attribute(lambda u: f"{u.name.split()[0]}@example.com")
    # phone = "01012345678"
    password = bcrypt.hashpw('qwer1234'.encode('utf-8'), bcrypt.gensalt()).decode("utf8")

class AccountUserIdFixedFactory(factory.django.DjangoModelFactory):
    #보이는 임의의 데이터 생성
    class Meta:
        model = Account
    user_id = 1
    expend = random.randrange(1000, 1000000)
    memo = faker.sentence()
    is_deleted = "V"
    deleted_at = faker.date()
    recovered_at = faker.date()
    
class AccountUserIdFixedInvisibleFactory(factory.django.DjangoModelFactory):
    #보이는 임의의 데이터 생성
    class Meta:
        model = Account
    user_id = 1
    expend = random.randrange(1000, 1000000)
    memo = faker.sentence()
    is_deleted = "I"
    deleted_at = faker.date()
    recovered_at = faker.date()

class AccountVisibleFactory(factory.django.DjangoModelFactory):
    #보이는 임의의 데이터 생성
    class Meta:
        model = Account
    user = factory.SubFactory(UserFactory)
    expend = random.randrange(1000, 1000000)
    memo = faker.sentence()
    is_deleted = "V"
    deleted_at = faker.date()
    recovered_at = faker.date()
    
class AccountInvisibleFactory(factory.django.DjangoModelFactory):
    #보이지 않는 임의의 데이터 생성
    class Meta:
        model = Account
    
    user = factory.SubFactory(UserFactory)
    expend = random.randrange(1000, 1000000)
    memo = faker.sentence()
    is_deleted = "V"
    deleted_at = faker.date()
    recovered_at = faker.date()
    