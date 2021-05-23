from django.urls import path

from . import views

app_name = "pairs"

urlpatterns = [
    path('kvpair', views.DictKVPair.as_view(), name='generateNget'),
]