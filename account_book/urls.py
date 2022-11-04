from django.urls import path
from account_book.views import account_create, account_delete_or_recover, account_find_all, account_get, account_update


urlpatterns = [
    path("account/create", account_create),
    path("account/details", account_get),
    path("account/update", account_update),
    path("account/delete", account_delete_or_recover),
    path("account/list", account_find_all),
    
]
