from enum import Enum

from account_book_service.enums import BaseEnum


class AccountStatusType(BaseEnum):
    visible = "V" #보이는 상태 (작성, 복구됨)
    invisible = "I" #보이지 않는상태 (삭제됨)