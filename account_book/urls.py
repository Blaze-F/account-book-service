from django.urls import path
from account_book.views import (
    account_create,
    account_delete,
    account_find_all,
    account_get,
    account_recover,
    account_update,
)


urlpatterns = [
    path("account/create", account_create),
    path("account/details", account_get),
    path("account/update", account_update),
    path("account/delete", account_delete),
    path("account/list", account_find_all),
    path("account/recover", account_recover),
]
