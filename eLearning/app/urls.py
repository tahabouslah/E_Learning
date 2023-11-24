from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(
    r"InteractionHistories", InteractionHistoryViewSet, basename="InteractionHistories"
)
router.register(
    r"InteractionHistories", InteractionHistoryViewSet, basename="InteractionHistories"
)
router.register(
    r"InteractionHistories", InteractionHistoryViewSet, basename="InteractionHistories"
)
router.register(
    r"InteractionHistories", InteractionHistoryViewSet, basename="InteractionHistories"
)
router.register(
    r"InteractionHistories", InteractionHistoryViewSet, basename="InteractionHistories"
)
router.register(
    r"InteractionHistories", InteractionHistoryViewSet, basename="InteractionHistories"
)


urlpatterns = [path("", include(router.urls))]
