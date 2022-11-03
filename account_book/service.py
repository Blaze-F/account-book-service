from account_book.repository import AbstractAccountRepository
from account_book.serializer import AccountCreateReqSchema, AccountUpdateReqSchema


class AccountBookService:
    def __init__(self, account_book_repo : AbstractAccountRepository) -> None:
        self.account_book_repo = account_book_repo
        
    def create(self, data : dict, user_id : int) -> dict :
        params = AccountCreateReqSchema(data=data)
        params.is_valid(raise_exception=True)
        res = self.account_book_repo.create_account(params.data,user_id)
        return res
        
    def update(self, data: dict, user_id :int) -> dict:
        params = AccountUpdateReqSchema(data=data)
        params.is_valid(raise_exception=True)
        res = self.account_book_repo.update_account(params.data,user_id)
        return res
    
    def soft_delete(self, data: dict, user_id : int) -> str:
        
        
        pass
    def get(self, user_id:int) -> dict:
        
        
        
        pass
    def find(self, user_id:int) -> list:
        
        
        pass