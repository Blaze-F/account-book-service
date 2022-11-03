import datetime
from account_book.models import Account
from account_book.serializer import (
    AccountCreateReqSchema,
    AccountListSerializer,
    AccountSerializer,
    AccountUpdateReqSchema,
)
from exceptions import NotFoundError


class AbstractAccountRepository:
    def __init__(self) -> None:
        self.model = Account
        self.serializer = AccountSerializer
        self.list_serializer = AccountListSerializer


class AccountRepository(AbstractAccountRepository):
    def get_account_by_user_id(self, user_id: int) -> dict:
        """유저가 가진 가계부 상세정보를 리턴"""
        try:
            return self.serializer(
                self.model.objects.select_related("user").get(user__id=user_id)
            ).data
        except self.model.DoesNotExist:
            raise NotFoundError()

    def find_account_by_user_id(self, user_id: int) -> dict:
        """유저가 가진 가계부 정보를 리스트로 리턴"""
        try:
            return self.serializer(
                self.model.objects.select_related("user").filter(user__id=user_id), many=True
            ).data
        except self.model.DoesNotExist:
            raise NotFoundError()

    def create_account(self, data: dict, user_id: int) -> dict:
        """create_account : 인자로 딕셔너리 (expend, memo), 유저 아이디를 받습니다."""
        data["user_id"] = user_id
        obj, is_created = self.model.objects.update_or_create(defaults=data)
        try:
            return self.serializer(obj).data
        except self.model.DoesNotExist:
            raise NotFoundError()

    def update_account(self, data: dict, user_id: int) -> dict:
        """update_account : 인자로 딕셔너리 (expend, memo, id), 유저 아이디를 받습니다."""
        obj, is_created = self.model.objects.update_or_create(user_id=user_id, defaults=data)
        try:
            return self.serializer(obj).data
        except self.model.DoesNotExist:
            raise NotFoundError()

    def soft_delete_or_recover_account(self, user_id: int, account_id: int) -> str:
        """soft_delete_account : 인자로 user_id, account_id 를 받습니다."""
        get = self.serializer(self.model.objects.get(id=account_id)).data
        # is_deleted의 상태를 반전
        if get["is_deleted"] == "V":
            get["is_deleted"] == "I"
            get["deleted_at"] == datetime.datetime.now()
        else:
            get["is_deleted"] == "V"
            get["recovered_at"] == datetime.datetime.now()
        #제대로 나오는지 확인 필요
        update = AccountUpdateReqSchema(data=get)
        update.is_valid(raise_exception=True)
        return self.serializer(
            self.model.objects.update_or_create(user_id=user_id, defaults=update)
        ).data
