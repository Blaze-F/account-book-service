from rest_framework import serializers

from account_book.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["user_id", "expend", "memo"]


class AccountDataReqSchema(serializers.Serializer):
    """메모는 최대 2000자로 제한"""

    expend = serializers.IntegerField()
    memo = serializers.CharField(max_length=2000)


class AccountDeleteReqSchema(serializers.Serializer):
    """메모는 최대 2000자로 제한"""

    order_id = serializers.IntegerField()
    expend = serializers.IntegerField()
    memo = serializers.CharField(max_length=2000)
    is_deleted = serializers.CharField(max_length=1)


class AccountDeleteReqSchema(serializers.Serializer):
    """삭제 요청에 대한 스키마"""


class AccountResSchema(serializers.Serializer):
    expend = serializers.IntegerField()
    memo = serializers.CharField(max_length=2000)
    is_deleted = serializers.CharField(max_length=1)


class PayReqSchema(serializers.Serializer):
    """
    service의 pay 기능 요청에 필요한 파라매터 정의 입니다.
    """

    order_id = serializers.IntegerField()
    payment_type = serializers.CharField(max_length=1)
    amount = serializers.IntegerField()
    cash_receipts = serializers.CharField(max_length=1, required=False, allow_null=True)
    cash_receipts_number = serializers.IntegerField(required=False, allow_null=True)
    deposit_number = serializers.IntegerField(required=False, allow_null=True)
    depositor = serializers.CharField(max_length=20, required=False, allow_null=True)

    # def validate_payment_type(self, value: str):
    #     if PaymentType.has_value(value):
    #         return value
    #     else:
    #         raise serializers.ValidationError("Unkwon payment type")

    # def validate_amount(self, value: int):
    #     if value > 0:
    #         return value
    #     else:
    #         raise serializers.ValidationError("amount must be bigger than 0")

    # def _validate_deposit_pay_required(self):
    #     if self.data["payment_type"] != PaymentType.DEPOSIT.value:
    #         return True
    #     else:
    #         return CashReciptsType.has_value(self.cash_receipts) and (
    #             None
    #             not in [
    #                 self.cash_receipts_number,
    #                 self.deposit_number,
    #                 self.depositor,
    #             ]
    #         )
