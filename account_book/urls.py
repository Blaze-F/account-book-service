from django.urls import path
from account_book.views import (
    account_create,
    account_delete,
    account_find_all,
    account_get,
    account_recover,
    account_update,
)

app_name = 'account'
urlpatterns = [
    path("account/create", account_create, name="create"),
    path("account/details", account_get, name="details"),
    path("account/update", account_update, name="update"),
    path("account/delete", account_delete, name="delete"),
    path("account/list", account_find_all, name="list"),
    path("account/recover", account_recover, name="recover"),
]
