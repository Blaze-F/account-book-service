from django.db import models

from account_book_service.models import BaseModel
from user.models import User


    
class Account(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
    )
    expend = models.IntegerField()
    memo = models.TextField()
    password = models.CharField(max_length=255, null=False)
    is_deleted = models.CharField(max_length=1, null=False, default="V") #삭제 플래그는 (visual, V) (invisiual, I)
    deleted_at = models.DateTimeField()
    recovered_at = models.DateField()
    
    class Meta:
        db_table = "user"
