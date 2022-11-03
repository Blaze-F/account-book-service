from django.urls import path
from account_book.views import account_create


urlpatterns = [
    # path(
    #     "account/update",
    # ),
    path("account/create", account_create),
    #     path(
    #         "account/details/<int:order_id>",
    #     ),
    #     path(
    #         "account/status",
    #     ),
]
