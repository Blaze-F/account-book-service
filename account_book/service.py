from account_book.repository import AbstractAccountRepository
from account_book.serializer import AccountCreateReqSchema, AccountDataReqSchema


class AccountBookService:
    def __init__(self, account_book_repo : AbstractAccountRepository) -> None:
        self.account_book_repo = account_book_repo
        
    def create(self, data : dict, user_id : int) -> dict :
        params = AccountDataReqSchema(data=data)
        params.is_valid(raise_exception=True)
        res = self.account_book_repo.upsert_account(data,user_id)
        return res
        
    def update(self, data: dict, user_id :int, account_id : int ) -> dict:
        params = AccountDataReqSchema(data=data)
        params.is_valid(raise_exception=True)
        res = self.account_book_repo.upsert_account(data,user_id)
        return res
    
    def soft_delete(self, user_id : int, account_id)
    def get(self, user_id:int) -> dict:
        
        