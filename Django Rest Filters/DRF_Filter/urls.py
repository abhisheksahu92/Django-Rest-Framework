from django.contrib import admin
from django.urls import path,include
from Person.views import PersonViews,PersonSearchView
from rest_framework import routers

router = routers.DefaultRouter()

router.register('person',PersonViews,basename='person')
router.register('personsearch',PersonSearchView,basename='person-search')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
