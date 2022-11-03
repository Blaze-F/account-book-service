from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from account_book.repository import AccountRepository
from account_book.service import AccountBookService
from decorater.auth_handler import must_be_user
from decorater.execption_handler import execption_hanlder
from provider.auth_provider import auth_provider

# 인스턴스 생성
account_book_repo = AccountRepository()
account_book_service = AccountBookService(account_book_repo=account_book_repo)


@api_view(["POST"])
@execption_hanlder()
@must_be_user()
@parser_classes([JSONParser])
def account_create(request):
    user_id = request.user["id"]
    created = account_book_service.create(user_id=user_id, data=request.data)

    return JsonResponse(created)

@api_view(["PUT"])
@execption_hanlder()
@must_be_user()
@parser_classes([JSONParser])
def account_update(request):
    user_id = request.user["id"]
    created = account_book_service.create(user_id=user_id, data=request.data)

    return JsonResponse(created)

@api_view(["D"])
@execption_hanlder()
@must_be_user()
@parser_classes([JSONParser])
def account_delete(request):
    user_id = request.user["id"]
    created = account_book_service.create(user_id=user_id, data=request.data)

    return JsonResponse(created)


# @api_view(["GET"])
# @execption_hanlder()
# @must_be_user()
# @parser_classes([JSONParser])  # json paser request를 구문분석
# def get_account(request):
#     auth_token = auth_provider.get_token_from_request(request)
#     return JsonResponse(payment_service.get(int(payment_id), request.user["id"], auth_token))


# @api_view(["GET"])
# @execption_hanlder()
# @must_be_user()
# @parser_classes([JSONParser])
# def get_account(request):
#     auth_token = auth_provider.get_token_from_request(request)
#     return JsonResponse(payment_service.get(int(payment_id), request.user["id"], auth_token))


# @api_view(["GET"])
# @execption_hanlder()
# @must_be_user()
# @parser_classes([JSONParser])
# def order_details(request, order_id: int):
#     return JsonResponse(order_management_service._get_order_detail(order_id))


# @api_view(["PUT"])
# @execption_hanlder()
# @parser_classes([JSONParser])
# def order_status_update(request):
#     params = OrderUpdateSchema(data=request.data)
#     params.is_valid(raise_exception=True)
#     order_id = params.data["order_id"]
#     status = params.data["status"]

#     a = params.data
#     return JsonResponse(order_management_service._deilvery_status_update(order_id, status))
