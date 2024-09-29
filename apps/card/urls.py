from django.urls import path
from apps.card import views

# router = routers.DefaultRouter()
# router.register("", views.CardView)
urlpatterns = [
    # path("", include(router.urls)),
    path("list/", views.CardListView, name="List Card paginated"),
    path("create/", views.CardCreateAPIView.as_view(), name="Card create"),
    path("update/<pk>/", views.CardUpdateAPIView.as_view(), name="Card update"),
    path("disable/", views.CardDisableView, name="Card disable"),
    path("get/<pk>/", views.CardRetrieveAPIView.as_view(), name="Card retrieve"),
]
