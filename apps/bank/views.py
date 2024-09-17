from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    ListAPIView,
)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Bank
from .serializers import Bankerializer


class BankCreateAPIView(CreateAPIView):
    serializer_class = Bankerializer
    queryset = Bank.objects.all()


class BankUpdateAPIView(UpdateAPIView):
    serializer_class = Bankerializer
    queryset = Bank.objects.all()


class BankListAPIView(ListAPIView):
    serializer_class = Bankerializer
    queryset = Bank.objects.all()

    @method_decorator(cache_page(60 * 3))  # Cache por 15 minutos
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BankRetrieveAPIView(RetrieveAPIView):
    serializer_class = Bankerializer
    queryset = Bank.objects.all()
