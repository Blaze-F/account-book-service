import datetime
from account_book.models import Account
from account_book.serializer import (
    AccountCreateReqSchema,
    AccountListSerializer,
    AccountSerializer,
    AccountUpdateReqSchema,
)
from exceptions import NotAuthorizedError, NotFoundError


class AbstractAccountRepository:
    def __init__(self) -> None:
        self.model = Account
        self.serializer = AccountSerializer
        self.list_serializer = AccountListSerializer


class AccountRepository(AbstractAccountRepository):
    def get_account_by_id(self, account_id: int) -> dict:
        """유저가 가진 가계부 상세정보를 리턴"""
        try:
            return self.serializer(
                self.model.objects.select_related("user").filter(is_deleted="V").get(id=account_id)
            ).data
        except self.model.DoesNotExist:
            raise NotFoundError()

    def find_account_by_user_id(self, user_id: int) -> dict:
        """유저가 가진 가계부 정보를 리스트로 리턴"""
        temp = (
            self.model.objects.select_related("user")
            .filter(user__id=user_id)
            .filter(is_deleted="V")
        )
        try:
            return self.list_serializer(temp, many=True).data
        except self.model.DoesNotExist:
            raise NotFoundError()

    def create_account(self, data: dict, user_id: int) -> dict:
        """create_account : 인자로 딕셔너리 (expend, memo), 유저 아이디를 받습니다."""
        obj = self.model.objects.create(
            user_id=user_id, memo=data.pop("memo"), expend=data.pop("expend")
        )
        try:
            return self.serializer(obj).data
        except self.model.DoesNotExist:
            raise NotFoundError()

    def update_account(self, params: dict, user_id: int) -> dict:
        """update_account : 인자로 딕셔너리 (expend, memo, id), 유저 아이디를 받습니다."""
        get_obj = self.model.objects.get(id=params["id"])

        # 직렬화 이전 인스턴스만 따로 추출
        user_ins = get_obj.user

        data = self.serializer(get_obj).data
        # 다른 유저가 삭제를 요청했을경우 validate
        if data["user"] != user_id:
            raise NotAuthorizedError

        del data["user"], data["id"]
        data["memo"] = params["memo"]
        data["expend"] = params["expend"]

        updated, is_created = self.model.objects.update_or_create(
            user=user_ins,
            id=params["id"],
            defaults=data,
        )
        try:
            return self.serializer(updated).data
        except self.model.DoesNotExist:
            raise NotFoundError()

    def soft_delete_or_recover_account(self, user_id: int, account_id: int) -> str:
        """soft_delete_account : 인자로 user_id, account_id 를 받습니다."""
        get = self.model.objects.get(id=account_id)

        # 직렬화 이전 인스턴스만 따로 추출
        user_ins = get.user

        data = self.serializer(get).data
        # 다른 유저가 삭제를 요청했을경우 validate
        if data["user"] != user_id:
            raise NotAuthorizedError
        self.change_status(data)
        del data["user"]
        del data["id"]
        res, is_created = self.model.objects.update_or_create(
            id=account_id,
            user=user_ins,
            defaults=data,
        )
        return self.serializer(res).data

    def change_status(self, data: dict) -> None:

        if data["is_deleted"] == "V":
            data["is_deleted"] = "I"
            data["deleted_at"] = datetime.datetime.now()
        else:
            data["is_deleted"] = "V"
            data["recovered_at"] = datetime.datetime.now()
