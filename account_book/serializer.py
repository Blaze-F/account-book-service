from rest_framework import serializers

from account_book.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "user_id", "expend", "memo"]


class AccountCreateReqSchema(serializers.Serializer):
    """메모는 최대 2000자로 제한"""

    expend = serializers.IntegerField()
    memo = serializers.CharField(max_length=2000)


class AccountUpdateReqSchema(serializers.Serializer):
    """생성에 account_id가 포함된 요청입니다."""
    id = serializers.IntegerField()
    expend = serializers.IntegerField()
    memo = serializers.CharField(max_length=2000)


class AccountResSchema(serializers.Serializer):
    expend = serializers.IntegerField()
    memo = serializers.CharField(max_length=2000)
    is_deleted = serializers.CharField(max_length=1)
