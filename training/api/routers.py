from django.urls import include, path
from rest_framework.routers import DefaultRouter

from training.api.viewsets import TrainingDataViewSet

router = DefaultRouter()
router.register(r"training_data", TrainingDataViewSet, basename="training_data")

urlpatterns = [
    path("", include(router.urls)),
]
