from account_book.models import Account
from account_book.serializer import AccountSerializer
from exceptions import NotFoundError


class AbstractAccountRepository:
    def __init__(self) -> None:
        self.model = Account
        self.serializer = AccountSerializer


class AccountRepository(AbstractAccountRepository):
    
    def get_account_by_user_id(self, user_id: int) -> dict:
        """유저가 가진 가계부 정보를 리턴"""
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

    def upsert_account(self, data: dict, user_id: int) -> dict:
        """upsert_account : 인자로 딕셔너리, 유저 아이디를 받습니다."""
        res = self.model.objects.update_or_create(user_id=user_id, defaults=data)
        return self.serializer(res).data

    def soft_delete_account(self,)