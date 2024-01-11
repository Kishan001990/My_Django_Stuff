from django.conf.urls import url,include
from appTwo.views import help
from rest_framework import routers




urlpatterns = [
    (r'^$',appTwo.urls)
]