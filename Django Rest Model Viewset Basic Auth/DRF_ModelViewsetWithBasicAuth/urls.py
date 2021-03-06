from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from Person.views import PersonModelViewSet

router = routers.DefaultRouter()
router.register('person',PersonModelViewSet,basename='person')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]

