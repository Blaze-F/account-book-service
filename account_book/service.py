from account_book.repository import AbstractAccountRepository
from account_book.serializer import AccountCreateReqSchema, AccountUpdateReqSchema


class AccountBookService:
    def __init__(self, account_book_repo: AbstractAccountRepository) -> None:
        self.account_book_repo = account_book_repo

    def create(self, data: dict, user_id: int) -> dict:
        params = AccountCreateReqSchema(data=data)
        params.is_valid(raise_exception=True)
        res = self.account_book_repo.create_account(params.data, user_id)
        return res

    def update(self, data: dict, user_id: int) -> dict:
        params = AccountUpdateReqSchema(data=data)
        params.is_valid(raise_exception=True)
        res = self.account_book_repo.update_account(params.data, user_id)
        return res

    def soft_delete(self, user_id: int, account_id: int) -> str:
        return self.account_book_repo.soft_delete_account(user_id=user_id, account_id=account_id)

    def recover(self, user_id: int, account_id: int) -> str:

        return self.account_book_repo.recover_account(user_id=user_id, account_id=account_id)

    def get(self, account_id: int) -> dict:
        return self.account_book_repo.get_account_by_id(account_id)

    def find(self, user_id: int) -> list:
        res = []
        res = self.account_book_repo.find_account_by_user_id(user_id)
        return res
