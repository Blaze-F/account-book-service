from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from account_book.repository import AccountRepository
from account_book.serializer import AccountCreateReqSchema, AccountListSerializer, AccountSerializer, AccountUpdateReqSchema
from account_book.service import AccountBookService
from decorator.auth_handler import must_be_user
from decorator.execption_handler import execption_hanlder
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_QUERY

# 인스턴스 생성
account_book_repo = AccountRepository()
account_book_service = AccountBookService(account_book_repo=account_book_repo)

@swagger_auto_schema(method="post", responses={200: AccountSerializer}, request_body=AccountCreateReqSchema)
@must_be_user()
@api_view(["POST"])
@execption_hanlder()
@parser_classes([JSONParser])
def account_create(request):
    user_id = request.user["id"]
    created = account_book_service.create(user_id=user_id, data=request.data)

    return JsonResponse(created, status=201)

@swagger_auto_schema(method="put", responses={200: AccountSerializer}, request_body=AccountUpdateReqSchema)
@api_view(["PUT"])
@execption_hanlder()
@must_be_user()
@parser_classes([JSONParser])
def account_update(request):
    user_id = request.user["id"]
    created = account_book_service.update(user_id=user_id, data=request.data)

    return JsonResponse(created, status=200)


@swagger_auto_schema(method="delete",manual_parameters=[
            Parameter('account_id', IN_QUERY,
                      '생성 아이디 입니다.',
                      type='int'),
            # Parameter('share_id', IN_PATH, type='uuid')
        ], responses={200: AccountSerializer})
@api_view(["DELETE"])
@execption_hanlder()
@must_be_user()
@parser_classes([JSONParser])
def account_delete(request):
    user_id = request.user["id"]
    account_id = request.GET["account_id"]
    res = account_book_service.soft_delete(user_id=user_id, account_id=account_id)
    
    return JsonResponse(res, status=200)

@swagger_auto_schema(method="get",manual_parameters=[
            Parameter('account_id', IN_QUERY,
                      '생성 아이디 입니다. 쿼리스트링입니다.',
                      type='int'),
        ], responses={200: AccountSerializer})
@api_view(["GET"])
@execption_hanlder()
@must_be_user()
@parser_classes([JSONParser])
def account_get(request):
    user_id = request.user["id"]
    account_id = request.GET["account_id"]
    res = account_book_service.get(account_id=account_id, user_id=user_id)

    return JsonResponse(res, status=200)

@swagger_auto_schema(method="get",manual_parameters=[
            Parameter('account_id', IN_QUERY,
                      '생성 아이디 입니다.',
                      type='int'),
        ], responses={200: AccountSerializer})
@api_view(["GET"])
@execption_hanlder()
@must_be_user()
@parser_classes([JSONParser])
def account_find_all(request):
    user_id = request.user["id"]
    res = account_book_service.find(user_id=user_id)

    return JsonResponse(res, safe=False, status=200)

@swagger_auto_schema(method="get",manual_parameters=[
            Parameter('account_id', IN_QUERY,
                      '생성 아이디 입니다. 쿼리스트링입니다.',
                      type='int'),
        ], responses={200: AccountSerializer})
@api_view(["GET"])
@execption_hanlder()
@must_be_user()
@parser_classes([JSONParser])
def account_recover(request):
    user_id = request.user["id"]
    account_id = request.GET["account_id"]
    res = account_book_service.recover(user_id=user_id, account_id=account_id)
    return JsonResponse(res, status=200)
