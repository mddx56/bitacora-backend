from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    ListAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Bank
from .serializers import BankSerializer


class BankCreateAPIView(CreateAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()


class BankUpdateAPIView(UpdateAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()


class BankListAPIView(ListAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()


@api_view(["GET"])
def BankListView(request):
    page = int(request.GET.get("page", 1))
    page_size = int(request.GET.get("page_size", 10))
    offset = (page - 1) * page_size
    limit = page * page_size
    banks = Bank.objects.all()[offset:limit]
    banks_data = BankSerializer(banks, many=True).data
    return Response(data=banks_data, status=status.HTTP_200_OK)


@api_view(["GET"])
def BankRetrieveView(request, id):
    try:
        bank = Bank.objects.get(id=id)
        bank_data = BankSerializer(bank).data
        return Response(data=bank_data, status=status.HTTP_200_OK)
    except Bank.DoesNotExist:
        return Response({"detail": "Bank not found"}, status=status.HTTP_404_NOT_FOUND)


class BankRetrieveAPIView(RetrieveAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()
