from  django.urls import path

from .views import SeiyuViewSet

urlpatterns = [
  path('', SeiyuViewSet)
]